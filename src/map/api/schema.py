from src.common.dto import BaseDto, PaginatedDto
from src.map.enum import MapContentType


class MapContentSchema(BaseDto):
    type: MapContentType
    code: str


class MapSchema(BaseDto):
    name: str
    skin: str
    x: int
    y: int
    content: MapContentSchema | None = None


class MapListSchema(PaginatedDto):
    data: list[MapSchema]
