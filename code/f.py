import cv2

# Define the screen dimensions based on your captured frames
SCREEN_SIZE = (1920, 1080)  # Replace with your actual screen dimensions

# Read the binary frames from the file
input_file = "frames.bin"
binary_frames = []
with open(input_file, 'rb') as f:
    while True:
        binary_frame = f.read(SCREEN_SIZE[0] * SCREEN_SIZE[1] * 4)  # Assuming RGBA format
        if not binary_frame:
            break
        binary_frames.append(binary_frame)

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 12, SCREEN_SIZE)

# Convert and write the binary frames to the video
for binary_frame in binary_frames:
    numpy_frame = bytearray(binary_frame)
    frame = numpy_frame
    frame = numpy_frame.reshape(SCREEN_SIZE[1], SCREEN_SIZE[0], 4)
    frame = frame[:, :, :3]  # Remove alpha channel
    out.write(frame)

# Release the VideoWriter object
out.release()

print("Video saved as output.mp4")

