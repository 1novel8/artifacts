from src.common.dto import BaseDto, PaginatedDto


class DropRateSchema(BaseDto):
    code: str
    rate: int
    min_quantity: int
    max_quantity: int


class MonsterSchema(BaseDto):
    name: str
    code: str
    level: int
    hp: int

    attack_fire: int
    attack_earth: int
    attack_water: int
    attack_air: int

    res_fire: int
    res_earth: int
    res_water: int
    res_air: int

    min_gold: int
    max_gold: int

    drops: list[DropRateSchema]


class MonsterListSchema(PaginatedDto):
    data: list[MonsterSchema]
