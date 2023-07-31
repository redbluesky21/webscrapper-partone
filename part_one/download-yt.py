import os
from pytube import YouTube

def download_youtube_videos(search_query, save_path):
    try:
        # Create the directory if it doesn't exist
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        # Search for videos based on the given query
        search_results = YouTube(f"ytsearch:{search_query}")

        # Get the first video from the search results
        video = search_results.streams.filter(progressive=True).first()

        # Download the video
        print(f"Downloading video: '{video.title}'...")
        video.download(save_path)
        print("Download completed!")

    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    search_query = input("Enter your YouTube search query: ")
    save_path = "C:\\Code\\Web_Scrapper\\raw_videos"
    download_youtube_videos(search_query, save_path)
