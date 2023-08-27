import mss
import time
import io

# Create an mss object
with mss.mss() as sct:
    # Set the screen recording parameters
    FPS = 12
    RECORD_SECONDS = 10
    
    # Calculate the total number of frames to capture
    total_frames = FPS * RECORD_SECONDS
    
    # Create a list to store binary frames
    binary_frames = []

    for _ in range(total_frames):
        # Capture a screenshot
        screenshot = sct.shot(output='bytes')
        
        # Append the binary frame to the list
        binary_frames.append(screenshot)
        
        time.sleep(1 / FPS)  # Wait for the desired frame rate

    # Write the binary frames to a file
    output_file = "frames.bin"
    with open(output_file, 'wb') as f:
        for binary_frame in binary_frames:
            f.write(binary_frame)
    
print(f"Binary frames saved as {output_file}")

