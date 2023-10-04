import pygetwindow as gw

# Define the VLC title
vlc_title = "VLC media player"

# Get a list of all open windows
windows = gw.getAllTitles()

# Search for the VLC window title in the list
vlc_window_title = None
for window_title in windows:
    if vlc_title in window_title:
        vlc_window_title = window_title
        break

# Check if the VLC window title was found
if vlc_window_title:
    print("VLC window title:", vlc_window_title)
else:
    print("VLC window not found")
