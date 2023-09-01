import os
import random
import imageio
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.video.io.VideoFileClip import VideoFileClip

# Specify the folder containing the input MP4 files
input_folder = 'output_clips'

# List all MP4 files in the input folder
mp4_files = [f for f in os.listdir(input_folder) if f.endswith('.mp4')]

# Check if there are any MP4 files in the folder
if not mp4_files:
    print("No MP4 files found in the input folder.")
else:
    # Choose a random MP4 file from the list
    random_mp4_file = random.choice(mp4_files)

    # Specify the input video file path
    input_video_path = os.path.join(input_folder, random_mp4_file)

    # Specify the number of frames to extract
    num_frames = 3

    # Specify the name of the new folder
    output_folder = 'frames'

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Open the input video
    video = VideoFileClip(input_video_path)

    # Get the duration of the video in seconds
    video_duration = video.duration

    # Calculate the time interval between frames
    time_interval = video_duration / (num_frames + 1)

    # Generate random times to extract frames
    random_times = [random.uniform(time_interval, video_duration - time_interval) for _ in range(num_frames)]

    # Sort the random times in ascending order
    random_times.sort()

    for i, time in enumerate(random_times):
        # Get the frame at the specified time
        frame = video.get_frame(time)

        # Specify the output frame file path within the output folder
        output_frame_path = os.path.join(output_folder, f'frame_{i + 1}.jpg')

        # Save the frame as an image using imageio
        imageio.imsave(output_frame_path, frame)

print(f"Random frames extracted from '{random_mp4_file}' and saved to {output_folder}")
