# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.default_api_base import BaseDefaultApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from openapi_server.models.providers_you_tube_download_request import ProvidersYouTubeDownloadRequest


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/providers/youtube",
    responses={
        200: {"model": file, "description": "The request has succeeded."},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def you_tube_download(
    providers_you_tube_download_request: ProvidersYouTubeDownloadRequest = Body(None, description=""),
) -> file:
    ...
