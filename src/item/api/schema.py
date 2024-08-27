from src.character.enum import Skill
from src.common.dto import BaseDto, PaginatedDto
from src.grand_exchange.api.schema import GEItemSchema
from src.item.enum import ItemType


class SimpleItemSchema(BaseDto):
    code: str
    quantity: int


class ItemEffectSchema(BaseDto):
    name: str
    value: int


class CraftSchema(BaseDto):
    skill: Skill
    level: int
    items: list[SimpleItemSchema]
    quantity: int


class ItemSchema(BaseDto):
    name: str
    code: str
    level: int
    type: ItemType
    subtype: str
    description: str

    effects: list[ItemEffectSchema]
    craft: CraftSchema | None


class ItemListSchema(PaginatedDto):
    data: list[ItemSchema]


class SingleItemSchema(BaseDto):
    item: ItemSchema
    ge: GEItemSchema
