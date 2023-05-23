from pytube import YouTube

# Enter the URL of the YouTube video you want to download
video_url = "https://www.youtube.com/watch?v=op12tJXVx6o"

# Create a YouTube object
yt = YouTube(video_url)

# Get the first available video format (usually the highest quality)
video = yt.streams.get_highest_resolution()

# Specify the output path for the downloaded video
output_path = "Z:\New folder (2)\youtube audio saves"

# Download the video
video.download(output_path)
