package capturer;

import com.sun.jna.Pointer;
import com.sun.jna.platform.win32.User32;
import com.sun.jna.platform.win32.WinDef.HWND;
import com.sun.jna.platform.win32.WinDef.RECT;
import com.sun.jna.platform.win32.WinUser;

import javax.imageio.ImageIO;
import java.awt.AWTException;
import java.awt.Rectangle;
import java.awt.Robot;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.text.DecimalFormat;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.Date;
import java.util.List;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;
import java.util.function.Consumer;

public class WindowCaptureService {

    private ScheduledExecutorService scheduler;
    private Robot robot;
    private SimpleDateFormat subfolderDateFormat = new SimpleDateFormat("yyyyMMdd_HHmmss");
    private File currentCaptureFolder;
    private long screenshotCount = 0;
    private Consumer<Long> screenshotCounterCallback; // Callback to update GUI counter
    private Consumer<String> statusUpdateCallback; // Callback to update GUI status
    private boolean isCapturing = false;

    public WindowCaptureService() {
        try {
            robot = new Robot();
        } catch (AWTException e) {
            System.err.println("Error: Could not create Robot instance. Ensure proper permissions.");
            throw new RuntimeException("Failed to initialize Robot", e);
        }
    }

    /**
     * Starts the continuous screenshot capture process.
     * @param targetWindow The WindowInfo object of the target application.
     * @param outputBaseDir The base directory to save screenshots.
     * @param fps Frames per second for capture.
     * @param removeShadow If true, adjusts capture area to remove shadows.
     * @param counterCallback Callback for updating screenshot count.
     * @param statusCallback Callback for updating status messages.
     */
    public void startCapture(WindowInfo targetWindow, File outputBaseDir, int fps, boolean removeShadow,
                             Consumer<Long> counterCallback, Consumer<String> statusCallback) {
        if (isCapturing) {
            statusCallback.accept("Capture already running.");
            return;
        }

        this.screenshotCounterCallback = counterCallback;
        this.statusUpdateCallback = statusCallback;
        this.screenshotCount = 0; // Reset counter for new session
        counterCallback.accept(0L); // Update GUI to 0

        // Create a new timestamped subfolder for this capture session
        String timestamp = subfolderDateFormat.format(new Date());
        currentCaptureFolder = new File(outputBaseDir, timestamp);
        if (!currentCaptureFolder.exists()) {
            if (!currentCaptureFolder.mkdirs()) {
                statusCallback.accept("Failed to create output subfolder: " + currentCaptureFolder.getAbsolutePath());
                return;
            }
        }

        long captureIntervalMs = 1000 / fps; // Interval in milliseconds

        scheduler = Executors.newSingleThreadScheduledExecutor();
        isCapturing = true;
        statusCallback.accept("Capture started for: " + targetWindow.title + " @ " + fps + " FPS");

        scheduler.scheduleAtFixedRate(() -> {
            if (!isCapturing) { // Check if stopped internally or externally
                Thread.currentThread().interrupt(); // Ensure termination
                return;
            }

            try {
                // Check if the window still exists and is visible
                if (!User32.INSTANCE.IsWindow(targetWindow.hWnd) || !User32.INSTANCE.IsWindowVisible(targetWindow.hWnd)) {
                    statusCallback.accept("Target window closed or became invisible. Stopping capture.");
                    stopCapture();
                    return;
                }

                RECT rect = new RECT();
                if (!User32.INSTANCE.GetWindowRect(targetWindow.hWnd, rect)) {
                    statusCallback.accept("Could not get window dimensions. Skipping screenshot.");
                    return;
                }

                int x = rect.left;
                int y = rect.top;
                int width = rect.right - rect.left;
                int height = rect.bottom - rect.top;

                if (removeShadow) {
                    // Adjust coordinates to remove typical Windows 10/11 shadows
                    x += 8;
                    y += 0; // Top shadow removal not typically needed or is part of frame
                    width -= 16; // 8 pixels from left + 8 pixels from right
                    height -= 8; // 7 pixels from bottom
                }

                // Ensure dimensions are positive
                if (width <= 0 || height <= 0) {
                    statusCallback.accept("Window dimensions are invalid after adjustment. Skipping screenshot.");
                    return;
                }

                Rectangle captureRect = new Rectangle(x, y, width, height);
                BufferedImage screenshot = robot.createScreenCapture(captureRect);

                screenshotCount++;
                DecimalFormat df = new DecimalFormat("00000000"); // Format for 8 digits
                String fileName = "screenshot_" + df.format(screenshotCount) + ".png";
                File outputFile = new File(currentCaptureFolder, fileName);

                ImageIO.write(screenshot, "PNG", outputFile);

                if (screenshotCount % 10 == 0) {
                    counterCallback.accept(screenshotCount); // Update GUI every 10 screenshots
                }

            } catch (IOException e) {
                statusCallback.accept("Error saving screenshot: " + e.getMessage());
                e.printStackTrace();
            } catch (Exception e) { // Catch any unexpected exceptions
                statusCallback.accept("An unexpected error occurred: " + e.getMessage());
                e.printStackTrace();
            }
        }, 0, captureIntervalMs, TimeUnit.MILLISECONDS);
    }

    /**
     * Stops the current screenshot capture process.
     */
    public void stopCapture() {
        if (!isCapturing) {
            statusUpdateCallback.accept("No capture is currently running.");
            return;
        }
        isCapturing = false; // Set flag to stop the loop
        if (scheduler != null && !scheduler.isShutdown()) {
            scheduler.shutdownNow(); // Attempt to stop all actively executing tasks
            try {
                if (!scheduler.awaitTermination(1, TimeUnit.SECONDS)) {
                    System.err.println("Scheduler did not terminate in time.");
                }
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt(); // Restore interrupt status
            } finally {
                scheduler = null;
                statusUpdateCallback.accept("Capture stopped. Total screenshots: " + screenshotCount);
                screenshotCounterCallback.accept(screenshotCount); // Final update
            }
        }
    }

    public boolean isCapturing() {
        return isCapturing;
    }

    /**
     * Lists all open top-level windows on Windows OS.
     * Uses JNA to call Windows API functions EnumWindows and GetWindowText.
     * @return A list of WindowInfo objects containing HWND and title for each found window.
     */
    public List<WindowInfo> listOpenWindows() {
        final List<WindowInfo> windows = new ArrayList<>();
        final int MAX_TITLE_LENGTH = 512; // Maximum length for a window title

        User32.INSTANCE.EnumWindows(new WinUser.WNDENUMPROC() {
            @Override
            public boolean callback(HWND hWnd, Pointer arg) {
                char[] windowText = new char[MAX_TITLE_LENGTH];
                User32.INSTANCE.GetWindowText(hWnd, windowText, MAX_TITLE_LENGTH);
                String wText = new String(windowText).trim();

                // Filter out empty titles, invisible windows, and console windows (often useless to screenshot)
                if (!wText.isEmpty() && User32.INSTANCE.IsWindowVisible(hWnd) &&
                        !wText.matches(".*\\b(cmd|Command Prompt|PowerShell|Terminal|N/A|Program Manager)\\b.*")) {
                    // Get parent window (if any)
                    HWND parentHwnd = User32.INSTANCE.GetParent(hWnd);
                    // Only add top-level windows (those without a parent, or whose parent is the desktop)
                    if (parentHwnd == null || parentHwnd.equals(User32.INSTANCE.GetDesktopWindow())) {
                        windows.add(new WindowInfo(hWnd, wText));
                    }
                }
                return true; // Continue enumeration
            }
        }, null);

        // Sort the list alphabetically by window title for easier selection
        windows.sort(Comparator.comparing(w -> w.title.toLowerCase()));
        return windows;
    }
}