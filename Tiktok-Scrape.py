from TikTokApi import TikTokApi
import requests
import os

def download_video(video_url, save_path):
    response = requests.get(video_url, stream=True)
    with open(save_path, 'wb') as out_file:
        for chunk in response.iter_content(chunk_size=8192):
            out_file.write(chunk)

def main():
    api = TikTokApi.get_instance()

    hashtag = "your_specified_hashtag"
    count = 100  # number of videos to download

    # Get videos with the specified hashtag
    tiktoks = api.by_hashtag(hashtag, count=count)

    # Create directory to save videos
    if not os.path.exists("downloaded_videos"):
        os.mkdir("downloaded_videos")

    # Download each video
    for tiktok in tiktoks:
        video_url = tiktok['video']['downloadAddr']
        video_name = tiktok['id'] + ".mp4"
        save_path = os.path.join("downloaded_videos", video_name)
        download_video(video_url, save_path)
        print(f"Downloaded video {video_name}")

if __name__ == "__main__":
    main()
