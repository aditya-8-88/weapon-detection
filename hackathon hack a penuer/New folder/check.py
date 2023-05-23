from moviepy.editor import VideoFileClip

# Set the path to your video file
video_file_path = r"Z:\New folder\youtube audio saves\₹2000 Note Banned In India shorts  money rbi bank.3gpp"

# Set the output audio file path
audio_output_path = "output_audio_file.wav"

# Load the video file
video = VideoFileClip(video_file_path)

# Extract the audio from the video
audio = video.audio

# Write the audio to a file
audio.write_audiofile(audio_output_path, codec='pcm_s16le')
