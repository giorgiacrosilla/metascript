import os
import pandas as pd
import imageio
from concurrent.futures import ThreadPoolExecutor

def convert_to_seconds(time_str):
    h, m, s = map(float, time_str.split(':'))
    return h * 3600 + m * 60 + s

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

def extract_frames(frame_range):
    start_frame, end_frame = frame_range

    extracted_frames = 0  # Counter for extracted frames
    
    for frame_counter, frame in enumerate(vid):
        if frame_counter < start_frame:
            continue
        if frame_counter > end_frame:
            break
        
        name = f'./frames/frame_{frame_counter}.jpg'
        print(f'Creating... {name}')
        imageio.imwrite(name, frame)
        
        extracted_frames += 1
        if extracted_frames >= 3:  # Stop after extracting 3 frames
            break

# Specify the desired index from the CSV
desired_index = "SUB357"  # Change this to the desired index value

row = df[df['index'] == desired_index].iloc[0]

start_time_str = row.line_start
end_time_str = row.line_end

# Convert timestamp strings to seconds and frames
start_time = convert_to_seconds(start_time_str)
end_time = convert_to_seconds(end_time_str)

start_frame = int(start_time * vid.get_meta_data()['fps'])
end_frame = int(end_time * vid.get_meta_data()['fps'])

# Extract frames using multithreading
with ThreadPoolExecutor(max_workers=1) as executor:  # Use one thread for simplicity
    executor.submit(extract_frames, (start_frame, end_frame))

# Release the video capture object and close the window
vid.close()
