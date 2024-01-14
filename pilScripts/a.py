import cv2
from PIL import ImageGrab
import numpy as np


# Capture the screen using PIL
screenshot = ImageGrab.grab()

# Convert the PIL image to a NumPy array (OpenCV format)
screenshot_cv = np.array(screenshot)

# Convert the image from RGB to BGR (OpenCV uses BGR)
screenshot_cv = cv2.cvtColor(screenshot_cv, cv2.COLOR_RGB2BGR)

# Display the screenshot using OpenCV (optional)
cv2.imshow('Screenshot', screenshot_cv)
cv2.waitKey(0)
cv2.destroyAllWindows()
