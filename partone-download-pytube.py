import os
from pytube import YouTube

def download_youtube_video(url, output_path):
    try:
        yt = YouTube(url)
        video_stream = yt.streams.filter(progressive=True, file_extension='mp4').first()

        if video_stream:
            print(f"Downloading: {yt.title}")
            video_stream.download(output_path)
            print("Download completed!")
        else:
            print("No progressive stream (mp4) available for this video.")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    # Provide the URL of the YouTube video you want to download
    youtube_url = "PUT_YOUR_YOUTUBE_VIDEO_URL_HERE"

    # Provide the output path where the video will be saved
    output_directory = "C:/Code/Web_Scrapper/raw_videos"

    # Check if the output directory exists, if not, create it
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    download_youtube_video(youtube_url, output_directory)
