import cv2
import numpy as np
import mss
import pygetwindow as gw
import time

from screen_cupturer import list_windows


def record_application_window(app_window_title, output_filename="application_capture.mp4", fps=20, duration=10):
    """
    Records a video of a specific application window.

    Args:
        window_title (str): The exact title of the application window to record.
        output_filename (str): The name of the output video file (e.g., "my_app_video.mp4").
        fps (int): Frames per second for the output video.
        duration (int): The duration of the recording in seconds. Set to 0 for continuous recording until stopped.
    """
    try:
        windows = gw.getWindowsWithTitle(app_window_title)
        if len(windows) == 0:
            print("No window found for title: ", app_window_title, ". Stop capturing.")
            return

        app_window = windows[0]

        print(f"Found window: {app_window.title} at {app_window.left},{app_window.top},{app_window.width},{app_window.height}")

        sct = mss.mss()

        # Define the codec and create VideoWriter object
        # You might need to experiment with codecs depending on your system and desired output.
        # Examples:
        #   - 'mp4v' for .mp4 (MPEG-4)
        #   - 'XVID' for .avi
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_filename, fourcc, fps, (app_window.width, app_window.height))

        if not out.isOpened():
            print(f"Error: Could not open video writer for {output_filename}")
            return

        print(f"Recording '{app_window.title}' to '{output_filename}' at {fps} FPS for {duration} seconds...")

        start_time = time.time()
        frame_count = 0

        while True:
            if duration > 0 and (time.time() - start_time) > duration:
                print(f"Recording finished after {duration} seconds.")
                break

            # Define the screen region to capture
            monitor = {
                "top": app_window.top,
                "left": app_window.left,
                "width": app_window.width,
                "height": app_window.height,
            }

            # Capture a screenshot of the specified monitor region
            sct_img = sct.grab(monitor)

            # Convert to numpy array and then to BGR for OpenCV
            frame = np.array(sct_img)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR) # Convert RGBA to BGR

            out.write(frame)
            frame_count += 1

            # Optional: Add a small delay to control FPS more accurately,
            # though mss.grab() and cv2.write() take time themselves.
            # time.sleep(1 / fps)

            # You can also add a way to stop the recording, e.g., by pressing 'q'
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     print("Recording stopped by user.")
            #     break

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'out' in locals() and out.isOpened():
            out.release()
            print(f"Video saved as {output_filename}")
        # cv2.destroyAllWindows()

if __name__ == "__main__":
    # --- IMPORTANT: BEFORE RUNNING ---
    # 1. Open the application you want to record.
    # 2. Get its exact window title. You can use a tool like Spy++ (Windows)
    #    or simply print all window titles using gw.getAllTitles() (as shown
    #    in the error message if the window is not found).
    #    For example, if you want to record a Chrome window, its title might be
    #    "New Tab - Google Chrome" or "Your Page Title - Google Chrome".

    # Example usage:
    # Let's say you want to record a Notepad window titled "Untitled - Notepad"
    # or a browser window.
    # Replace "Your Application Window Title" with the actual title.

    # Example 1: Record a Notepad window for 15 seconds
    # Make sure a Notepad window is open and its title matches exactly.
    # If it's "Untitled - Notepad", use that.
    # record_application_window("Untitled - Notepad", output_filename="notepad_capture.mp4", duration=15)

    # Example 2: Record a specific browser window (e.g., Google Chrome)
    # Open a Chrome tab and make sure its title is accurate.
    # e.g., "New Tab - Google Chrome" or "Python - Google Search - Google Chrome"
    # record_application_window("New Tab - Google Chrome", output_filename="chrome_capture.mp4", duration=20, fps=30)

    # Example 3: Record a window continuously until you manually stop the script (Ctrl+C)
    # or implement a key press to stop (uncomment the waitKey part in the loop)
    # record_application_window("VLC media player", output_filename="vlc_capture.mp4", duration=0, fps=25)


    # Example 4: A dummy recording of the active window for 10 seconds (might be unpredictable if window changes)
    # It's better to specify a precise title.
    # active_window = gw.getActiveWindow()
    # if active_window:
    #     print(f"Attempting to record active window: {active_window.title}")
    #     record_application_window(active_window.title, output_filename="active_window_capture.mp4", duration=10, fps=20)
    # else:
    #     print("No active window found to record.")

    window_titles = list_windows()

    print('List of available windows:')
    for idx, title in enumerate(window_titles):
        print(f"{idx}: {title}")

    try:
        selection = int(input("Enter the number of the window to process: "))
        if 0 <= selection < len(window_titles):
            print("Press Ctrl+C or close target window to quit.")
            record_application_window(window_titles[selection], output_filename="screenshots/active_window_capture.mp4", duration=20, fps=20)
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")
    # capture_screenshot('Shared with me - Google Drive - Google Chrome')

    print("\n--- To run this, uncomment one of the example calls in the __main__ block ---")
    print("--- Make sure the target application is running and its window title is exact ---")
    print("--- If you don't know the title, temporarily uncomment `gw.getAllTitles()` inside the function for debugging ---")

    # Debugging tip: To find window titles, you can temporarily add this outside the function:
    # for title in gw.getAllTitles():
    #     if title:
    #         print(f"Found Window Title: '{title}'")