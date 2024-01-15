import mss
import imageio
import os


# Directory to store captured frames
output_directory = 'captured_frames'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Screen dimensions
screen_width = 1920  # Change this according to your screen resolution
screen_height = 1080  # Change this according to your screen resolution

# Capture screen and save frames as images
num_frames = 100  # Change this to capture desired number of frames
with mss.mss() as sct:
    for i in range(num_frames):
        filename = f'{output_directory}/frame_{i}.png'
        # Capture screen
        sct_img = sct.grab(sct.monitors[0])
        # Save frame as an image
        imageio.imwrite(filename, sct_img)

# Create MP4 video from captured frames
output_video = 'captured_screen.mp4'
images = [f'{output_directory}/frame_{i}.png' for i in range(num_frames)]
with imageio.get_writer(output_video, fps=24) as writer:
    for img in images:
        frame = imageio.imread(img)
        writer.append_data(frame)

print(f"Video created: {output_video}")
