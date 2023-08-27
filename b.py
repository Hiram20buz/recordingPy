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

for i in range(int(record_seconds * fps)):
    # Make a screenshot
    img = pyautogui.screenshot()
    
    # Convert these pixels to a proper numpy array to work with OpenCV
    frame = np.array(img)
    
    # Convert colors from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Write the frame
    out.write(frame)
    
    # Show the frame
    cv2.imshow("screenshot", frame)
    
    # If the user clicks 'q', exit the loop
    if cv2.waitKey(1) == ord("q"):
        break

# Make sure everything is closed when exited
cv2.destroyAllWindows()
out.release()

