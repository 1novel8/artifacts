import asyncio

from src.map.api.endpoints import maps__get_page
from src.map.api.schema import MapListSchema
from src.map.enum import MapContentType


async def maps__all(
    content_type: MapContentType | None = None, content_code: str | None = None
) -> MapListSchema:
    start_maps = await maps__get_page(size=100, content_type=content_type, content_code=content_code)

    group = [
        maps__get_page(size=100, page=page, content_type=content_type, content_code=content_code)
        for page in range(1, start_maps.pages + 1)
    ]
    results: tuple[MapListSchema] = await asyncio.gather(*group)

    maps = start_maps.data
    for result in results:
        maps.extend(result.data)
    return MapListSchema(data=maps)