import imageio
from PIL import ImageGrab
import numpy as np

# Define the file name and frame rate for the output video
output_file = 'screenshot_video.mp4'
fps = 10

# Capture a certain number of screenshots and save them to the video
num_frames = 100  # Change the number of frames as needed
frames = []

for _ in range(num_frames):
    # Capture the screen using PIL
    screenshot = ImageGrab.grab()
    
    # Append the screenshot to the frames list
    frames.append(np.array(screenshot))

# Save the frames as a video using imageio
imageio.mimsave(output_file, frames, fps=fps)
