from src.character.api.schemas import CharacterSchema, CharacterListSchema, CharacterMoveSchema
from src.common.router import route


@route(url='/my/characters', method='GET', request_dto=None, response_dto=CharacterListSchema)
async def characters__all() -> list[CharacterSchema]:
    ...


@route(url='/my/{name}/action/move', method='POST', request_dto=CharacterMoveSchema, response_dto=None)
async def character__move(*, name: str, data: dict[str, int]) -> None:
    ...


@route(url='/my/{name}/action/fight', method='POST', request_dto=CharacterMoveSchema, response_dto=None)
async def character__fight(name: str) -> None:
    ...