# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.providers_you_tube_download_request import ProvidersYouTubeDownloadRequest  # noqa: F401


def test_you_tube_download(client: TestClient):
    """Test case for you_tube_download

    
    """
    providers_you_tube_download_request = openapi_server.ProvidersYouTubeDownloadRequest()

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/providers/youtube",
    #    headers=headers,
    #    json=providers_you_tube_download_request,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

