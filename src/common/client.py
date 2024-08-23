import typing
import logging

import httpx
import requests

from src.common.dto import ResponseDto
from src.settings import settings

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class ArtifactsAPIClient:
    base_url = settings.artifacts.api_base_url
    api_token = settings.artifacts.api_token
    default_headers = {
        'Authorization': f'Bearer {settings.artifacts.api_token}',
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }

    async def request(
            self,
            url: str,
            method: str,
            data: str | None = None,
            headers: dict[str, typing.Any] | None = None,
    ) -> ResponseDto:
        headers = headers if headers else self.default_headers
        url = self.base_url + url
        logger.info(f' REQUEST: [{method}] {url} {data}, {headers}')

        response = await self._async_request(
            method=method, url=url, data=data, headers=headers
        )

        logger.error(f' RESPONSE: {response.content.decode("utf-8")}')
        return ResponseDto.model_validate(response)

    async def _async_request(self, **kwargs) -> httpx.Response:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.request(**kwargs)
                return response
            except httpx.HTTPError as exc:
                raise exc

    @classmethod
    def is_healthy(cls) -> bool:
        response = requests.request(method='GET', url=cls.base_url)
        return response.status_code == 200
