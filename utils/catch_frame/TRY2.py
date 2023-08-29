import cv2
import os
import pandas as pd

# Load the CSV file
csv_path = 'output.csv'
df = pd.read_csv(csv_path)

# Set video file path of input video with name and extension
video_path = 'EWS_movie.mp4'
print(f"Video Path: {video_path}")

vid = cv2.VideoCapture(video_path)

# Check if the video file can be opened
if not vid.isOpened():
    print("Error: Could not open the video file.")
    exit()

# Create 'images' directory if it doesn't exist
if not os.path.exists('images'):
    os.makedirs('images')

# For frame identity
index = 0

def convert_to_seconds(time_str):
    h, m, s = map(float, time_str.split(':'))
    return h * 3600 + m * 60 + s

for row in df.itertuples():
    start_time_str = row.line_start
    end_time_str = row.line_end

    # Convert timestamp strings to seconds
    start_time = convert_to_seconds(start_time_str)
    end_time = convert_to_seconds(end_time_str)

    start_frame = int(start_time * vid.get(cv2.CAP_PROP_FPS))
    end_frame = int(end_time * vid.get(cv2.CAP_PROP_FPS))

    frame_interval = (end_frame - start_frame) // 1  # Choose the desired number of frames

    frame_counter = 0

    while True:
        ret, frame = vid.read()

        if not ret:
            break

        if frame_counter >= start_frame and frame_counter <= end_frame:
            if frame_counter % frame_interval == 0:
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
