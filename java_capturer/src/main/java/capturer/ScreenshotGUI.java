package capturer;

import javax.swing.*;
import javax.swing.filechooser.FileSystemView;
import java.awt.*;
import java.io.File;
import java.util.List;
import java.util.concurrent.TimeUnit;

public class ScreenshotGUI extends JFrame {

    private JComboBox<WindowInfo> windowComboBox;
    private JTextField fpsField;
    private JTextField outputDirField;
    private JButton browseButton;
    private JCheckBox removeShadowCheckbox;
    private JButton startButton;
    private JButton stopButton;
    private JLabel statusLabel;
    private JLabel screenshotCounterLabel;
    private JButton refreshButton;

    private WindowCaptureService captureService;
    private List<WindowInfo> availableWindows;

    // Default values
    private static final int DEFAULT_FPS = 20;
    private static final String DEFAULT_OUTPUT_DIR = "Screenshots";

    public ScreenshotGUI() {
        super("External Application Screenshot Taker");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout(10, 10)); // Add some padding

        captureService = new WindowCaptureService();

        // --- Panel for Input Controls ---
        JPanel inputPanel = new JPanel(new GridBagLayout());
        inputPanel.setBorder(BorderFactory.createTitledBorder("Settings"));
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(5, 5, 5, 5); // Padding around components
        gbc.fill = GridBagConstraints.HORIZONTAL;

        // Window Selection
        gbc.gridx = 0;
        gbc.gridy = 0;
        inputPanel.add(new JLabel("Select Window:"), gbc);
        gbc.gridx = 1;
        gbc.weightx = 1.0; // Take extra horizontal space
        windowComboBox = new JComboBox<>();
        inputPanel.add(windowComboBox, gbc);
        gbc.weightx = 0; // Reset weight

        gbc.gridx = 2;
        refreshButton = new JButton("Refresh List");
        refreshButton.addActionListener(e -> populateWindowList());
        inputPanel.add(refreshButton, gbc);


        // FPS
        gbc.gridx = 0;
        gbc.gridy = 1;
        inputPanel.add(new JLabel("FPS (Frames per second):"), gbc);
        gbc.gridx = 1;
        fpsField = new JTextField(String.valueOf(DEFAULT_FPS));
        inputPanel.add(fpsField, gbc);

        // Output Directory
        gbc.gridx = 0;
        gbc.gridy = 2;
        inputPanel.add(new JLabel("Output Directory:"), gbc);
        gbc.gridx = 1;
        outputDirField = new JTextField(DEFAULT_OUTPUT_DIR);
        outputDirField.setEditable(false); // Make it read-only
        inputPanel.add(outputDirField, gbc);
        gbc.gridx = 2;
        browseButton = new JButton("Browse...");
        browseButton.addActionListener(e -> {
            JFileChooser fileChooser = new JFileChooser(FileSystemView.getFileSystemView().getHomeDirectory());
            fileChooser.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY);
            int returnValue = fileChooser.showOpenDialog(ScreenshotGUI.this);
            if (returnValue == JFileChooser.APPROVE_OPTION) {
                File selectedDir = fileChooser.getSelectedFile();
                outputDirField.setText(selectedDir.getAbsolutePath());
            }
        });
        inputPanel.add(browseButton, gbc);

        // Remove Shadow Checkbox
        gbc.gridx = 0;
        gbc.gridy = 3;
        gbc.gridwidth = 2; // Span two columns
        removeShadowCheckbox = new JCheckBox("Remove Window Shadow (adjust capture area)");
        removeShadowCheckbox.setSelected(false); // Default to false
        inputPanel.add(removeShadowCheckbox, gbc);
        gbc.gridwidth = 1; // Reset to 1

        add(inputPanel, BorderLayout.NORTH);

        // --- Panel for Controls and Status ---
        JPanel controlPanel = new JPanel(new FlowLayout(FlowLayout.CENTER, 10, 10));
        startButton = new JButton("Start Screenshots");
        stopButton = new JButton("Stop Screenshots");
        stopButton.setEnabled(false); // Disabled by default

        startButton.addActionListener(e -> startScreenshotProcess());
        stopButton.addActionListener(e -> stopScreenshotProcess());

        controlPanel.add(startButton);
        controlPanel.add(stopButton);
        add(controlPanel, BorderLayout.CENTER);

        // --- Panel for Status and Counter ---
        JPanel statusPanel = new JPanel(new BorderLayout(5, 5));
        statusPanel.setBorder(BorderFactory.createEmptyBorder(5, 10, 10, 10)); // Padding

        statusLabel = new JLabel("Ready", SwingConstants.CENTER);
        statusLabel.setFont(statusLabel.getFont().deriveFont(Font.BOLD, 14f));
        statusPanel.add(statusLabel, BorderLayout.NORTH);

        screenshotCounterLabel = new JLabel("Screenshots Taken: 0", SwingConstants.CENTER);
        screenshotCounterLabel.setFont(screenshotCounterLabel.getFont().deriveFont(Font.PLAIN, 12f));
        statusPanel.add(screenshotCounterLabel, BorderLayout.SOUTH);


        add(statusPanel, BorderLayout.SOUTH);

        populateWindowList(); // Populate on startup

        // Finalize frame
        pack(); // Adjusts window size based on components
        setLocationRelativeTo(null); // Center the window
        setVisible(true);
    }

    private void populateWindowList() {
        statusLabel.setText("Refreshing window list...");
        // Use SwingWorker to prevent freezing GUI during JNA calls
        new SwingWorker<List<WindowInfo>, Void>() {
            @Override
            protected List<WindowInfo> doInBackground() throws Exception {
                return captureService.listOpenWindows();
            }

            @Override
            protected void done() {
                try {
                    availableWindows = get(); // Get the result from doInBackground
                    windowComboBox.removeAllItems();
                    if (availableWindows.isEmpty()) {
                        windowComboBox.addItem(new WindowInfo(null, "No Windows Found"));
                        windowComboBox.setEnabled(false);
                    } else {
                        for (WindowInfo info : availableWindows) {
                            windowComboBox.addItem(info);
                        }
                        windowComboBox.setEnabled(true);
                    }
                    statusLabel.setText("Window list refreshed.");
                } catch (Exception e) {
                    statusLabel.setText("Error refreshing window list.");
                    JOptionPane.showMessageDialog(ScreenshotGUI.this,
                            "Failed to refresh window list: " + e.getMessage(),
                            "Error", JOptionPane.ERROR_MESSAGE);
                }
            }
        }.execute();
    }

    private void startScreenshotProcess() {
        if (captureService.isCapturing()) {
            JOptionPane.showMessageDialog(this, "Capture is already running.", "Info", JOptionPane.INFORMATION_MESSAGE);
            return;
        }

        // Validate inputs
        if (windowComboBox.getSelectedItem() == null || ((WindowInfo)windowComboBox.getSelectedItem()).hWnd == null) {
            JOptionPane.showMessageDialog(this, "Please select a valid window.", "Input Error", JOptionPane.WARNING_MESSAGE);
            return;
        }
        WindowInfo targetWindow = (WindowInfo) windowComboBox.getSelectedItem();

        int fps;
        try {
            fps = Integer.parseInt(fpsField.getText());
            if (fps <= 0) {
                throw new IllegalArgumentException("FPS must be greater than 0.");
            }
        } catch (IllegalArgumentException e) {
            JOptionPane.showMessageDialog(this, "Invalid FPS: " + e.getMessage(), "Input Error", JOptionPane.WARNING_MESSAGE);
            return;
        }

        File outputDir = new File(outputDirField.getText());
        if (!outputDir.exists()) {
            int confirm = JOptionPane.showConfirmDialog(this,
                    "Output directory '" + outputDir.getAbsolutePath() + "' does not exist. Create it?",
                    "Create Directory?", JOptionPane.YES_NO_OPTION);
            if (confirm == JOptionPane.YES_OPTION) {
                if (!outputDir.mkdirs()) {
                    JOptionPane.showMessageDialog(this, "Failed to create output directory.", "Directory Error", JOptionPane.ERROR_MESSAGE);
                    return;
                }
            } else {
                return; // User chose not to create, so cancel
            }
        }
        if (!outputDir.isDirectory()) {
            JOptionPane.showMessageDialog(this, "Output path is not a directory.", "Input Error", JOptionPane.WARNING_MESSAGE);
            return;
        }
        if (!outputDir.canWrite()) {
            JOptionPane.showMessageDialog(this, "Output directory is not writable. Check permissions.", "Input Error", JOptionPane.WARNING_MESSAGE);
            return;
        }

        boolean removeShadow = removeShadowCheckbox.isSelected();

        // Give user time to switch to the application (optional, but good for starting)
        statusLabel.setText("Starting capture in 3 seconds. Please switch to your target application.");
        setControlsEnabled(false);
        stopButton.setEnabled(false); // Temp disable stop until the 3-sec wait is done.

        // Use a separate SwingWorker for the initial delay
        new SwingWorker<Void, Void>() {
            @Override
            protected Void doInBackground() throws Exception {
                TimeUnit.SECONDS.sleep(3);
                return null;
            }

            @Override
            protected void done() {
                // This runs on EDT after delay
                stopButton.setEnabled(true); // Re-enable stop button
                captureService.startCapture(targetWindow, outputDir, fps, removeShadow,
                        // Callback for screenshot count (updates GUI)
                        (count) -> SwingUtilities.invokeLater(() -> screenshotCounterLabel.setText("Screenshots Taken: " + count)),
                        // Callback for status updates (updates GUI)
                        (status) -> SwingUtilities.invokeLater(() -> statusLabel.setText(status))
                );
            }
        }.execute();
    }

    private void stopScreenshotProcess() {
        captureService.stopCapture();
        setControlsEnabled(true);
        stopButton.setEnabled(false);
        screenshotCounterLabel.setText("Screenshots Taken: 0"); // Reset display
    }

    private void setControlsEnabled(boolean enabled) {
        windowComboBox.setEnabled(enabled);
        fpsField.setEnabled(enabled);
        outputDirField.setEnabled(enabled);
        browseButton.setEnabled(enabled);
        removeShadowCheckbox.setEnabled(enabled);
        startButton.setEnabled(enabled);
        refreshButton.setEnabled(enabled);
        // stopButton state is managed separately
    }
}