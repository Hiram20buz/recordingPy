import os
import time
import imageio
from moviepy.editor import ImageSequenceClip

output_folder = 'screenshots'
video_filename = 'output_video.mp4'
fps = 10  # Adjust the frames per second as needed

# Create a folder to store screenshots
os.makedirs(output_folder, exist_ok=True)

# Capture screenshots
num_screenshots = 100  # Change as needed
with imageio.get_writer(output_folder + '/temp.mp4', fps=fps) as writer:
    with imageio.get_writer(output_folder + '/temp.gif', mode='I', fps=fps) as gif_writer:
        with imageio.get_reader("<screen>") as reader:
            for i in range(num_screenshots):
                output_filename = f"{output_folder}/screenshot_{i:04d}.png"
                reader.get_next_data()
                writer.append_data(reader.get_next_data())
                time.sleep(1 / fps)
                gif_writer.append_data(reader.get_next_data())

# Convert GIF to MP4 using moviepy
gif_filename = output_folder + '/temp.gif'
clip = ImageSequenceClip([imageio.imread(gif_filename)], fps=fps)
clip.write_videofile(video_filename, codec='libx264', fps=fps)

# Clean up temporary files
os.remove(output_folder + '/temp.mp4')
os.remove(output_folder + '/temp.gif')

print(f"Video created: {video_filename}")
