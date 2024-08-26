import asyncio

from src.map.facades import maps__all


async def main():
    maps = await maps__all()
    for map in maps.data:
        print(map)

    # characters = await characters__all()
    # print(characters)
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
