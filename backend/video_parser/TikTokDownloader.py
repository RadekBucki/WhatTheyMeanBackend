import json
import os
import requests
from bs4 import BeautifulSoup

from backend.exceptions.video_parsing_exception import VideoParsingException
from backend.video_parser.FormatConverter import FormatConverter

headers = {'Accept-Encoding': 'gzip, deflate, sdch',
           'Accept-Language': 'en-US,en;q=0.8',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive'}


class TikTokDownloader:

    @staticmethod
    def download(url: str) -> str:
        video_file_path = FormatConverter.get_video_path()
        audio_file_path = FormatConverter.get_audio_path()
        tt = requests.get(url, headers=headers, timeout=20)
        cookies = tt.cookies
        soup = BeautifulSoup(tt.text, "html.parser")
        tt_script = soup.find('script', attrs={'id': "SIGI_STATE"})
        tt_json = json.loads(tt_script.string)
        video_id = list(tt_json['ItemModule'].keys())[0]
        if 'imagePost' in tt_json['ItemModule'][video_id]:
            raise VideoParsingException("Image post cannot be downloaded!")
        tt_video_url = tt_json['ItemModule'][video_id]['video']['downloadAddr']
        headers['referer'] = 'https://www.tiktok.com/'
        tt_video = requests.get(tt_video_url, allow_redirects=True, headers=headers, cookies=cookies)
        with open(video_file_path, 'wb') as fn:
            fn.write(tt_video.content)
        audio_base64 = FormatConverter.convert()
        os.remove(video_file_path)
        os.remove(audio_file_path)
        return audio_base64
