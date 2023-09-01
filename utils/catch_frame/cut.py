from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import pandas as pd
import os 

# Specify the input video file path
input_video_path = 'EWS_movie.mp4'

# Load the CSV file
csv_path = 'output.csv'
df = pd.read_csv(csv_path)

def convert_to_seconds(time_str):
    h, m, s = map(float, time_str.split(':'))
    return h * 3600 + m * 60 + s

# Specify the desired index from the CSV
desired_index = "SUB357"  # Change this to the desired index value

row = df[df['index'] == desired_index].iloc[0]

start_time_str = row.line_start
end_time_str = row.line_end

# Convert timestamp strings to seconds and frames
start_time = convert_to_seconds(start_time_str)
end_time = convert_to_seconds(end_time_str)

# Specify the name of the new folder
output_folder = 'output_clips'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Specify the output video file path within the output folder
output_video_path = os.path.join(output_folder, 'output_clip.mp4')

# Extract the clip
ffmpeg_extract_subclip(input_video_path, start_time, end_time, targetname=output_video_path)


print(f"Clip extracted from {start_time} to {end_time} seconds and saved to {output_video_path}")
