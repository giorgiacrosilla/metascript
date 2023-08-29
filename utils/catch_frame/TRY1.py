import cv2
import os

# Set video file path of input video with name and extension
video_path = 'trailer.mp4'
print(f"Video Path: {video_path}")

vid = cv2.VideoCapture(video_path)

# Check if the video file can be opened
if not vid.isOpened():
    print("Error: Could not open the video file.")
    exit()

# Timestamps in seconds
start_time = 10  # Start timestamp in seconds
end_time = 20    # End timestamp in seconds
frame_interval = 3  # Interval between frames in seconds

# Calculate frame numbers corresponding to timestamps
start_frame = int(start_time * vid.get(cv2.CAP_PROP_FPS))
end_frame = int(end_time * vid.get(cv2.CAP_PROP_FPS))

# Create 'images' directory if it doesn't exist
if not os.path.exists('images'):
    os.makedirs('images')

# For frame identity
index = 0
frame_counter = 0

while True:
    ret, frame = vid.read()
    
    if not ret:
        break
    
    if frame_counter >= start_frame and frame_counter <= end_frame:
        if frame_counter % int(frame_interval * vid.get(cv2.CAP_PROP_FPS)) == 0:
            name = f'./images/frame_{index}.jpg'
            print(f'Creating... {name}')
            cv2.imwrite(name, frame)
            index += 1
    
    if frame_counter > end_frame:
        break
    
    frame_counter += 1

# Release the video capture object and close the window
vid.release()
cv2.destroyAllWindows()

