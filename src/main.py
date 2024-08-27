import asyncio

from src.character.api.endpoints import characters__all
from src.item.facades import items__all
from src.map.facades import maps__all
from src.monster.facades import monsters__all


async def main():
    maps = await maps__all()
    for map in maps.data:
        print(map)

    monsters = await monsters__all()
    for monster in monsters.data:
        print(monster)

    items = await items__all()
    for items in items.data:
        print(items)

    characters = await characters__all()
    print(characters)
    # await asyncio.gather(*(character__move(name=character.name, x=0, y=1) for character in characters))
    # tasks = [character__craft_item(name=character.name, item_code='wooden_staff', quantity=1) for character in characters]
    # await asyncio.gather(*tasks)
    # tasks = [
    #     character__gather_items(name=character.name, item_code=ItemCode.ash_tree, count=4)
    #     for character in characters
    # ]
    # await asyncio.gather(*tasks)
    # tasks = [character__fight_forever(name=character.name) for character in characters]
    # await asyncio.gather(*tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
