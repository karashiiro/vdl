import pytest
from openapi_server.impl.providers.youtube.client import YouTubeClient


@pytest.mark.asyncio
async def test_youtube_download():
    with YouTubeClient() as yt:
        await yt.download_video("https://www.youtube.com/watch?v=G5hScSFkib4")
