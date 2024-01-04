import mss
import imageio
import os


# Create a folder to store screenshots
# Directory to store captured frames
def createDir(outputFolder: str = 'captured_frames'):
    if not os.path.exists(outputFolder):
        os.makedirs(outputFolder)

# Capture screen and save frames as images
def captureSS(outputFolder: str = 'captured_frames', num_frames: int = 100):
    #num_frames = 100  # Change this to capture desired number of frames
    with mss.mss() as sct:
        for i in range(num_frames):
            filename = f'{outputFolder}/frame_{i}.png'
            # Capture screen
            sct_img = sct.grab(sct.monitors[0])
            # Save frame as an image
            imageio.imwrite(filename, sct_img)

# Create MP4 video from captured frames
def createMP4(output_video: str = 'captured_screen.mp4', outputFolder: str = 'captured_frames', num_frames: int = 100):
    images = [f'{outputFolder}/frame_{i}.png' for i in range(num_frames)]
    with imageio.get_writer(output_video, fps=24) as writer:
        for img in images:
            frame = imageio.imread(img)
            writer.append_data(frame)