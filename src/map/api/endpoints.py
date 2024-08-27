
from src.common import status_code
from src.common.client import ArtifactsAPIClient
from src.common.exception import UnexpectedStatusCode
from src.map.api.schema import MapListSchema, MapSchema
from src.map.enum import MapContentType


async def maps__get_page(
        *,
        page: int = 1,
        size: int = 10,
        content_type: MapContentType | None = None,
        content_code: str | None = None
) -> MapListSchema:
    params = {
        'page': page,
        'size': size,
    }
    if content_type:
        params['content_type'] = content_type
    if content_code:
        params['content_code'] = content_code

    response = await ArtifactsAPIClient().call_api(url='/maps', method='GET', params=params)

    if response.status_code != status_code.OK:
        raise UnexpectedStatusCode(response)
    return MapListSchema.model_validate(response.model_dump())


async def map__get(*, x: int, y: int) -> MapSchema:
    response = await ArtifactsAPIClient().call_api(url=f'/maps{x}/{y}', method='GET')

    if response.status_code != status_code.OK:
        raise UnexpectedStatusCode(response)
    return MapSchema.model_validate(response.data)
