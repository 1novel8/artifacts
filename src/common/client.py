import json
import typing
import logging
import requests

from src.settings import settings

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class ArtifactsAPIClient:
    base_url = settings.ARTIFACTS.API_BASE_URL
    api_token = settings.ARTIFACTS.API_TOKEN
    default_headers = {
        'Authorization': f'Bearer {settings.ARTIFACTS.API_TOKEN}',
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }

    @classmethod
    def request(
            cls,
            url: str,
            method: str,
            data: typing.Any | None = None,
            headers: dict[str, typing.Any] | None = None,
            **kwargs: typing.Any,
    ) -> requests.Response:
        headers_ = headers
        if headers is None:
            headers_ = cls.default_headers

        url = cls.base_url + url
        logger.info(f' REQUEST: [{method}] {url} {data}, {headers_}')

        response = requests.request(method=method, url=url, data=json.dumps(data), headers=headers_, **kwargs)
        logger.error(f' RESPONSE: {response.content.decode("utf-8")}')
        return response

    @classmethod
    def is_healthy(cls) -> bool:
        response = requests.request(method='GET', url=cls.base_url)
        return response.status_code == 200
