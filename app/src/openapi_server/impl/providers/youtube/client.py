import asyncio
from yt_dlp import YoutubeDL


class YouTubeClient:
    _ytdlp: YoutubeDL
    _locks: dict[str, asyncio.Event]

    def __init__(self):
        self._ytdlp = YoutubeDL({"progress": [self.__on_update]})
        self._locks = {}

    async def download_video(self, video_url: str):
        if not video_url in self._locks:
            self._locks[video_url] = asyncio.Event()

        self._ytdlp.download([video_url])

        await self._locks[video_url].wait()

    def __on_update(self, info: dict):
        if info["status"] != "finished":
            return

        clean_info = self._ytdlp.sanitize_info(info["info_dict"])
        print(clean_info)

        # TODO: Release lock

    def __enter__(self):
        return self

    def __exit__(self):
        self._ytdlp.__exit__()
