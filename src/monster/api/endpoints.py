
from src.common import status_code
from src.common.client import ArtifactsAPIClient
from src.common.exception import UnexpectedStatusCode
from src.monster.api.schema import MonsterListSchema, MonsterSchema


async def monsters__get_page(
        *,
        page: int = 1,
        size: int = 10,
        max_level: int | None = None,
        min_level: int | None = None,
) -> MonsterListSchema:
    params = {
        'page': page,
        'size': size,
    }
    if max_level:
        params['max_level'] = max_level
    if min_level:
        params['min_level'] = min_level

    response = await ArtifactsAPIClient().call_api(url='/monsters', method='GET', params=params)

    if response.status_code != status_code.OK:
        raise UnexpectedStatusCode(response)
    return MonsterListSchema.model_validate(response.model_dump())


async def monster__get(*, code: str) -> MonsterSchema:
    response = await ArtifactsAPIClient().call_api(url=f'/monster/{code}', method='GET')

    if response.status_code != status_code.OK:
        raise UnexpectedStatusCode(response)
    return MonsterSchema.model_validate(response.data)
