# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from openapi_server.models.providers_you_tube_download_request import ProvidersYouTubeDownloadRequest


class BaseDefaultApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseDefaultApi.subclasses = BaseDefaultApi.subclasses + (cls,)
    def you_tube_download(
        self,
        providers_you_tube_download_request: ProvidersYouTubeDownloadRequest,
    ) -> file:
        ...
