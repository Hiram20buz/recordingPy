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



# Create MP4 video from captured frames
output_video = 'captured_screen.mp4'
images = [f'{output_directory}/frame_{i}.png' for i in range(60)]
with imageio.get_writer(output_video, fps=24) as writer:
    for img in images:
        frame = imageio.imread(img)
        writer.append_data(frame)

print(f"Video created: {output_video}")