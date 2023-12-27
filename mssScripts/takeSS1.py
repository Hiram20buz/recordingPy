import mss
import time
from PIL import Image
import io

# Create an mss object
with mss.mss() as sct:
    # Set the screen recording parameters
    SCREEN_SIZE = sct.monitors[0]
    FPS = 12
    RECORD_SECONDS = 10
    
    # Calculate the total number of frames to capture
    total_frames = FPS * RECORD_SECONDS
    
    # Create a list to store frames
    frames = []

    for _ in range(total_frames):
        # Capture a screenshot
        screenshot = sct.shot(output='pil')
        
        # Append the PIL Image to the frames list
        frames.append(screenshot)
        
        time.sleep(1 / FPS)  # Wait for the desired frame rate

    # Save the frames as a video
    frames[0].save(
        "output.mp4",
        save_all=True,
        append_images=frames[1:],
        duration=1/FPS,
        loop=0
    )

print("Video saved as output.mp4")

