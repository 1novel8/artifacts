class BaseStatusCode:
    code: int
    message: str

    def __init__(self, code: int) -> None:
        self.code = code

    def __eq__(self, other: object) -> bool:
        if isinstance(other, BaseStatusCode):
            return self.code == other.code and self.message == other.message
        elif isinstance(other, int):
            return self.code == other

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)


OK = BaseStatusCode(200)
CharacterCooldown = BaseStatusCode(499)
CharacterAlreadyAtDestination = BaseStatusCode(490)
