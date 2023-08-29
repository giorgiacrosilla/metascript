import os
import pandas as pd
import imageio

# Load the CSV file
csv_path = 'output.csv'
df = pd.read_csv(csv_path)

# Set video file path of input video with name and extension
video_path = 'EWS_movie.mp4'
print(f"Video Path: {video_path}")

# Open the video file using imageio
vid = imageio.get_reader(video_path)

# Create 'images' directory if it doesn't exist
if not os.path.exists('frames'):
    os.makedirs('frames')

# For frame identity
index = 0

def convert_to_seconds(time_str):
    h, m, s = map(float, time_str.split(':'))
    return h * 3600 + m * 60 + s

# Specify the desired index from the CSV
desired_index = "SUB2"  # Change this to the desired index value

row = df[df['index'] == desired_index].iloc[0]

start_time_str = row.line_start
end_time_str = row.line_end

# Convert timestamp strings to seconds
start_time = convert_to_seconds(start_time_str)
end_time = convert_to_seconds(end_time_str)

start_frame = int(start_time * vid.get_meta_data()['fps'])
end_frame = int(end_time * vid.get_meta_data()['fps'])

frame_interval = (end_time - start_time) / 3  # Ensure exactly 3 frames

frame_counter = 0
frame_num = 0

for _ in range(start_frame):
    vid.get_next_data()

for frame_counter, frame in enumerate(vid):
    if frame_counter >= start_time * vid.get_meta_data()['fps'] and frame_counter <= end_time * vid.get_meta_data()['fps']:
        if frame_num % int(vid.get_meta_data()['fps'] * frame_interval) == 0:
            name = f'./frames/frame_{index}.jpg'
            print(f'Creating... {name}')
            imageio.imwrite(name, frame)
            index += 1
    
    if frame_counter > end_time * vid.get_meta_data()['fps']:
        break
    
    frame_counter += 1
    frame_num += 1

# Release the video capture object and close the window
vid.close()
