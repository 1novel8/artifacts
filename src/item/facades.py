import asyncio

from src.item.api.endpoints import items__get_page
from src.item.api.schema import ItemListSchema


async def items__all(
    max_level: int | None = None, min_level: int | None = None
) -> ItemListSchema:
    start_maps = await items__get_page(size=100, max_level=max_level, min_level=min_level)

    group = [
        items__get_page(size=100, page=page, max_level=max_level, min_level=min_level)
        for page in range(1, start_maps.pages + 1)
    ]
    results: tuple[ItemListSchema] = await asyncio.gather(*group)

    maps = start_maps.data
    for result in results:
        maps.extend(result.data)
    return ItemListSchema(data=maps)