import asyncio

from src.monster.api.endpoints import monsters__get_page
from src.monster.api.schema import MonsterListSchema


async def monsters__all(
    max_level: int | None = None, min_level: int | None = None
) -> MonsterListSchema:
    start_maps = await monsters__get_page(size=100, max_level=max_level, min_level=min_level)

    group = [
        monsters__get_page(size=100, page=page, max_level=max_level, min_level=min_level)
        for page in range(1, start_maps.pages + 1)
    ]
    results: tuple[MonsterListSchema] = await asyncio.gather(*group)

    maps = start_maps.data
    for result in results:
        maps.extend(result.data)
    return MonsterListSchema(data=maps)