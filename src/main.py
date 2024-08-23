from src.character.api.endpoints import characters__all, character__move, character__fight
import asyncio


async def main():
    characters = await characters__all()
    tasks = [
        character__move(name=character.name, data={'x': 0, 'y': 1}) for character in characters
    ]
    await asyncio.gather(*tasks)
    tasks = [
        character__fight(name=character.name) for character in characters
    ]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
