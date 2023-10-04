import pygetwindow as gw
import time
import pyautogui

# Define the name of the process or window title you want to focus on
window_title = "VLC media player"

# Get a list of all open windows
windows = gw.getAllTitles()

# Find the window with the specified title
found = False
for window_title_candidate in gw.getAllTitles():
    if window_title.lower() in window_title_candidate.lower():
        found = True
        # Activate the window
        vlc=gw.getWindowsWithTitle(window_title_candidate)[0]
        if vlc.isMaximized:
            vlc.activate()
        else:
            vlc.maximize()
        pyautogui.press('space')
        break
if not found:
    print(f"No window with the title '{window_title}' found.")
else:
    # Give some time for the window to become active
    time.sleep(1)


