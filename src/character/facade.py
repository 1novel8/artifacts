import asyncio
import typing

from src.character.api.endpoints import (character__equip, character__fight,
                                         character__gather, character__move,
                                         characters__all)
from src.character.api.schema import (CharacterMoveSchema, CharacterSchema,
                                      EquipRequestSchema)
from src.character.enum import ItemCode


async def character__fight_forever(name: str) -> typing.Any:
    result = await character__move(name=name, request=CharacterMoveSchema(x=-1, y=0))
    await asyncio.sleep(result.cooldown.remaining_seconds)
    while True:
        result = await character__fight(name=name)
        await asyncio.sleep(result.cooldown.remaining_seconds)


async def character__gather_forever(name: str) -> typing.Any:
    while True:
        result = await character__gather(name=name)
        await asyncio.sleep(result.cooldown.remaining_seconds)


async def character__gather_items(name: str, item_code: ItemCode, count: int) -> typing.Any:
    result = await character__move(name=name, request=CharacterMoveSchema(x=-1, y=0))
    await asyncio.sleep(result.cooldown.remaining_seconds)
    item_quantity = {item.code: item.quantity for item in result.character.inventory}
    while item_quantity.get(item_code, 0) < count:
        result = await character__gather(name=name)
        await asyncio.sleep(result.cooldown.remaining_seconds)


async def character__craft_item(name: str, item_code: str, quantity: int) -> typing.Any:
    # result = await character__move(name=name, data={'x': 2, 'y': 1})
    # await asyncio.sleep(result.cooldown.remaining_seconds)
    # result = await character__unequip(name=name, data={'slot': 'weapon', 'quantity': quantity})
    # await asyncio.sleep(result.cooldown.remaining_seconds)

    # result = await character__craft(name=name, data={'code': item_code, 'quantity': quantity})
    # await asyncio.sleep(result.cooldown.remaining_seconds)

    result = await character__equip(
        name=name, request=EquipRequestSchema(code=item_code, quantity=quantity, slot='weapon')
    )
    await asyncio.sleep(result.cooldown.remaining_seconds)


async def character__revive(character: CharacterSchema) -> typing.Any:
    ...


async def characters__revive() -> None:
    characters = await characters__all()

    tasks = [character__revive(character) for character in characters]
    await asyncio.gather(*tasks)
