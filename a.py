import cv2
import pyautogui
import numpy as np
# Display screen resolution, get it using pyautogui itself
SCREEN_SIZE = tuple(pyautogui.size())

# Define the codec
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# Frames per second
fps = 12.0

# Create the video write object
out = cv2.VideoWriter('output.avi', fourcc, fps, SCREEN_SIZE)

# The time you want to record in seconds
record_seconds = 10

# Calculate the total number of frames to capture
total_frames = int(fps * record_seconds)

for _ in range(total_frames):
    screenshot = pyautogui.screenshot()
    frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    out.write(frame)

out.release()
cv2.destroyAllWindows()

