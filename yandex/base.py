import asyncio
from pprint import pp

import xmltodict

from httpx import AsyncClient

from yandex_music import ClientAsync
from settings import settings


class YaClient:
    def __init__(self):
        self.client = ClientAsync(settings.YM_KEY)
        self.httpx_client = AsyncClient()
        asyncio.run(self.client.init())

    async def get_sound_url(self, url: str):
        track_id = url.split('/')[-1]
        info = await self.client.tracks_download_info(track_id)
        download_url = info[0]['download_info_url']
        print(download_url)
        track_stream_url = await self.httpx_client.get(download_url)
        track_stream_info = xmltodict.parse(track_stream_url.content)
        pp(track_stream_info)
        track_stream_info_dict = track_stream_info['download-info']
        host = track_stream_info_dict["host"]
        path = track_stream_info_dict["path"]
        s = track_stream_info_dict["s"]
        ts = track_stream_info_dict["ts"]
        result_url = f'https://{host}/get-mp3/{s}/{ts}{path}/?track_id={track_id}&play=false'
        print(result_url)
        return result_url


ya_client = YaClient()
# asyncio.run(ya_client.get_sound_url('https://music.yandex.ru/album/5838243/track/43779930'))
