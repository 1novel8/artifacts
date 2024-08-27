from src.common.dto import BaseDto


class GEItemSchema(BaseDto):
    code: str
    stock: int
    sell_price: int
    buy_price: int
    max_quantity: int


class GEItemListSchema(BaseDto):
    data: list[GEItemSchema]
