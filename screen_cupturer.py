import os

import mss
import pygetwindow as gw
import time

interval = 1  # seconds
total_shots = 2
folder = 'screenshots'

def capture_screenshot(window_title):
    # Create screenshots folder if not exists
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Find the window
    win = gw.getWindowsWithTitle(window_title)[0]
    bbox = {'top': win.top, 'left': win.left, 'width': win.width, 'height': win.height}

    counter = 1
    try:
        with mss.mss() as sct:
            while True:
                img = sct.grab(bbox)
                mss.tools.to_png(img.rgb, img.size, output=f"screenshots/screenshot_{counter:08d}.png")
                counter += 1
                time.sleep(interval)
    except KeyboardInterrupt:
        print("\nExiting. Goodbye!")

def list_windows():
    windows = gw.getAllWindows()
    for window in windows:
        print(window.title)
    return [window.title for window in windows if window.title.strip()]

if __name__ == '__main__':
    window_titles = list_windows()

    print('List of available windows:')
    for idx, title in enumerate(window_titles):
        print(f"{idx}: {title}")

    try:
        selection = int(input("Enter the number of the window to process: "))
        if 0 <= selection < len(window_titles):
            print("Press Ctrl+C to quit.")
            capture_screenshot(window_titles[selection])
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")
    # capture_screenshot('Shared with me - Google Drive - Google Chrome')
