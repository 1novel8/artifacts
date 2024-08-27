from pydantic import TypeAdapter

from src.character.api.schema import (CharacterFightDataSchema,
                                      CharacterMovementDataSchema,
                                      CharacterMoveSchema, CharacterSchema,
                                      CraftingRequestSchema,
                                      EquipRequestSchema, EquipResponseSchema,
                                      SkillDataSchema, UnequipRequestSchema)
from src.common import status_code
from src.common.client import ArtifactsAPIClient
from src.common.exception import UnexpectedStatusCode


async def characters__all() -> list[CharacterSchema]:
    response = await ArtifactsAPIClient().call_api(url='/my/characters', method='GET')

    if response.status_code != status_code.OK:
        raise UnexpectedStatusCode(response)
    return TypeAdapter(list[CharacterSchema]).validate_python(response.data)


async def character__move(*, name: str, request: CharacterMoveSchema) -> CharacterMovementDataSchema:
    response = await ArtifactsAPIClient.call_api(url=f'/my/{name}/action/move', method='POST', request=request)

    if response.status_code != status_code.OK:
        raise UnexpectedStatusCode(response)
    return CharacterMovementDataSchema.model_validate(response.data)


async def character__fight(name: str) -> CharacterFightDataSchema:
    response = await ArtifactsAPIClient().call_api(url=f'/my/{name}/action/fight', method='POST')

    if response.status_code != status_code.OK:
        raise UnexpectedStatusCode(response)
    return CharacterFightDataSchema.model_validate(response.data)


async def character__gather(*, name: str) -> SkillDataSchema:
    response = await ArtifactsAPIClient().call_api(url=f'/my/{name}/action/gathering', method='POST')

    if response.status_code != status_code.OK:
        raise UnexpectedStatusCode(response)
    return SkillDataSchema.model_validate(response.data)


async def character__craft(name: str, request: CraftingRequestSchema) -> SkillDataSchema:
    response = await ArtifactsAPIClient().call_api(url=f'/my/{name}/action/crafting', method='POST', request=request)

    if response.status_code != status_code.OK:
        raise UnexpectedStatusCode(response)
    return SkillDataSchema.model_validate(response.data)


async def character__unequip(*, name: str, request: UnequipRequestSchema) -> EquipResponseSchema:
    response = await ArtifactsAPIClient().call_api(url=f'/my/{name}/action/unequip', method='POST', request=request)

    if response.status_code != status_code.OK:
        raise UnexpectedStatusCode(response)
    return EquipResponseSchema.model_validate(response.data)


async def character__equip(*, name: str, request: EquipRequestSchema) -> EquipResponseSchema:
    response = await ArtifactsAPIClient().call_api(url=f'/my/{name}/action/equip', method='POST', request=request)

    if response.status_code != status_code.OK:
        raise UnexpectedStatusCode(response)
    return EquipResponseSchema.model_validate(response.data)
