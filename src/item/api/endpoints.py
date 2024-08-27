from src.character.enum import Skill
from src.common import status_code
from src.common.client import ArtifactsAPIClient
from src.common.exception import UnexpectedStatusCode
from src.item.api.schema import ItemListSchema, SingleItemSchema
from src.item.enum import ItemType


async def items__get_page(
        *,
        page: int = 1,
        size: int = 10,
        craft_material: int | None = None,
        craft_skill: Skill | None = None,
        max_level: int | None = None,
        min_level: int | None = None,
        name: str | None = None,
        item_type: ItemType | None = None,
) -> ItemListSchema:
    params = {
        'page': page,
        'size': size,
    }
    if craft_material:
        params['craft_material'] = craft_material
    if craft_skill:
        params['craft_skill'] = craft_skill
    if max_level:
        params['max_level'] = max_level
    if min_level:
        params['min_level'] = min_level
    if name:
        params['name'] = name
    if item_type:
        params['type'] = item_type

    response = await ArtifactsAPIClient().call_api(url='/items', method='GET', params=params)

    if response.status_code != status_code.OK:
        raise UnexpectedStatusCode(response)
    return ItemListSchema.model_validate(response.model_dump())


async def item__get(*, code: str) -> SingleItemSchema:
    response = await ArtifactsAPIClient().call_api(url=f'/item/{code}', method='GET')

    if response.status_code != status_code.OK:
        raise UnexpectedStatusCode(response)
    return SingleItemSchema.model_validate(response.data)
