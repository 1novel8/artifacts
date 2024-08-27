import logging
import typing

import httpx
import requests
from pydantic import BaseModel

from src.common import status_code
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
            params: dict[str, typing.Any] | None = None,
            **kwargs,
    ) -> httpx.Response:
        headers = headers if headers else self.default_headers
        url = self.base_url + url

        response = await self._async_request(
            method=method, url=url, data=data, headers=headers, params=params
        )

        return response

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
        return response.status_code == status_code.OK

    async def call_api(
            self,
            url: str,
            method: str,
            request: BaseModel | None = None,
            params: dict[str, typing.Any] | None = None,
            **kwargs: typing.Any,
    ) -> ResponseDto:
        request_data = None
        if request:
            request_data = request.model_dump_json()

        response = await self.request(url=url, data=request_data, method=method, params=params, **kwargs)
        response = ResponseDto.model_validate(response)

        return response
