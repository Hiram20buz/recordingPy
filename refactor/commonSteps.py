import os
import time
import imageio
import moviepy.editor as mp


# Create a folder to store screenshots
def createDir(outputFolder: str = "screenshots"):
    os.makedirs(outputFolder, exist_ok=True)

# Calculate number of frames based on duration and FPS
# Capture screenshots
def captureSS(numScreenshots: int, delay: float, fps: int, outputFolder: str = "screenshots"):
    with imageio.get_writer(outputFolder + '/temp.mp4', fps=fps) as writer:
        with imageio.get_writer(outputFolder + '/temp.gif', mode='I', fps=fps) as gif_writer:
            with imageio.get_reader("<screen>") as reader:
                for i in range(numScreenshots):
                    output_filename = f"{outputFolder}/screenshot_{i:04d}.png"
                    reader.get_next_data()
                    writer.append_data(reader.get_next_data())
                    time.sleep(delay)
                    gif_writer.append_data(reader.get_next_data())

# Convert GIF to MP4 using moviepy
def gifToMp4(inputFileName: str = "screenshots/temp.gif", outputFileName: str = "screenshots/output_video.mp4"):
    clip = mp.VideoFileClip(inputFileName)
    clip.write_videofile(outputFileName)
