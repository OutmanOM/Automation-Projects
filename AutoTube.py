import pytube

# Ask the user to enter the link of the video to download
video_url = input("Enter the link of the YouTube video you want to download: ")

# Create a YouTube object from the video URL
yt = pytube.YouTube(video_url)

# Get the highest resolution stream available for the video
stream = yt.streams.get_highest_resolution()

# Download the video to the current working directory
print("Downloading...")
stream.download()
print("Download complete!")
