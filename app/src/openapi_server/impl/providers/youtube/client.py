import asyncio
import logging
from typing import cast
from urllib.parse import parse_qs, urlparse
from yt_dlp import YoutubeDL


class YouTubeClient:
    _ytdlp: YoutubeDL
    _locks: dict[str, asyncio.Event]
    _files: dict[str, str]

    def __init__(self):
        self._ytdlp = YoutubeDL({"progress_hooks": [self.__on_update]})
        self._locks = {}
        self._files = {}

    async def download_video(self, video_url: str):
        print("Downloading YouTube video at %s" % video_url)

        parsed_url = urlparse(video_url)
        parsed_query = parse_qs(parsed_url.query)
        video_id = parsed_query["v"].pop()

        print("YouTube video ID: %s" % video_id)

        if not video_id in self._locks:
            self._locks[video_id] = asyncio.Event()

        self._ytdlp.download([video_url])

        # Wait for the download to complete, up to 5 minutes
        await asyncio.wait_for(self._locks[video_id].wait(), timeout=300)

        print("Downloaded YouTube video to %s" % self._files[video_id])
        return self._files[video_id]

    def __on_update(self, info: dict):
        if info["status"] != "finished":
            return

        clean_info = self._ytdlp.sanitize_info(info["info_dict"])
        video_id = cast(str, cast(dict, clean_info)["id"])

        self._files[video_id] = info["filename"]

        # Release the lock
        self._locks[video_id].set()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._ytdlp.__exit__()
