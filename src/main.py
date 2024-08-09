from src.character.logic.interactors import character__fight, character__move
from src.character.logic.selectors import characters__all

if __name__ == '__main__':
    characters = characters__all()
    for character in characters:
        character__move(character_name=character.name, x=0, y=1)
        character__fight(character_name=character.name)

