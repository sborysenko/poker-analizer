import datetime
import os

import mss
import pyautogui
import pygetwindow as gw
import time

from PIL import ImageGrab

interval = 1  # seconds
total_shots = 2
folder = 'screenshots'
subfolder = ''
library = 'mss'

def capture_screenshot(window_title):
    # Create screenshots folder if not exists
    if not os.path.exists(folder):
        os.makedirs(folder)

    global subfolder
    subfolder = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
    os.makedirs(os.path.join(folder, subfolder))

    counter = 1
    try:
        while True:
            # Find the window
            windows = gw.getWindowsWithTitle(window_title)
            if len(windows) == 0:
                print("No window found for title: ", window_title, ". Stop capturing.")
                return

            win = windows[0]
            bbox = {'top': win.top, 'left': win.left, 'width': win.width, 'height': win.height}

            match library:
                case 'mss':
                    capture_screenshot_mss(bbox, counter)
                case 'pyautogui':
                    capture_screenshot_pyautogui(bbox, counter)
                case 'pillow':
                    capture_screenshot_pillow(bbox, counter)

            counter += 1
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nExiting. Goodbye!")

def capture_screenshot_mss(bbox, counter):
    with mss.mss() as sct:
        img = sct.grab(bbox)
        mss.tools.to_png(img.rgb, img.size, output=f"{folder}/{subfolder}/screenshot_{counter}.png")

def capture_screenshot_pyautogui(bbox, counter):
    screenshot = pyautogui.screenshot(region=(bbox.left, bbox.top, bbox.width, bbox.height))
    screenshot.save(f"{folder}/{subfolder}/screenshot_{counter}.png")

def capture_screenshot_pillow(bbox, counter):
    screenshot = ImageGrab.grab(bbox=bbox)
    screenshot.save(f"{folder}/{subfolder}/screenshot_{counter}.png", format="PNG")

def list_windows():
    windows = gw.getAllWindows()
    return [window.title for window in windows if window.title.strip()]

if __name__ == '__main__':
    window_titles = list_windows()

    print("Libraries for screen capturing:")
    print(" 0 - mss (used in previous version)")
    print(" 1 - pyautogui")
    print(" 2 - pillow")
    print("")
    try:
        choice = int(input("Please select library to screen capture: "))
        match choice:
            case '0':
                library = 'mss'
            case '1':
                library = 'pyautogui'
            case '2':
                library = 'pillow'
    except ValueError:
        print("Please enter a valid number.")
        exit(1)

    print('List of available windows:')
    for idx, title in enumerate(window_titles):
        print(f"{idx}: {title}")

    try:
        selection = int(input("Enter the number of the window to process: "))
        if 0 <= selection < len(window_titles):
            print("Press Ctrl+C or close target window to quit.")
            capture_screenshot(window_titles[selection])
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")
    # capture_screenshot('Shared with me - Google Drive - Google Chrome')
