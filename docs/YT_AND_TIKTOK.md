# YOUTUBE AND TIKTOK DOWNLOAD

## Youtube

Video is fetched using pytube library (downloaded as mp4 with video and converted to mp3 audio), all required operations are performed in YouTubeDownloader class.

Usage:
```python
from backend.video_parser.YouTubeDownloader import YouTubeDownloader

res = YouTubeDownloader.download("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
```
Response returned from method is base64 encoded mp3 file.

## TikTok

TikTok (TikTokDownloader) downloading is based on pyktok library. It's implementation was not enough and it was not working (it required using webdriver as well). We made the implementation simpler to just download mp4 video files for us. Later the file is converted to mp3 audio as in YoutubeDownloader

Usage:
```python
from backend.video_parser.TikTokDownloader import TikTokDownloader

res = TikTokDownloader.download("https://www.tiktok.com/@tiktok/video/7106594312292453675?is_copy_url=1&is_from_webapp=v1")
```
Response returned from method is base64 encoded mp3 file.
