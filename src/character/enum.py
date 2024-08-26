from strenum import StrEnum


class CooldownReason(StrEnum):
    movement = 'movement'
    fight = 'fight'
    crafting = 'crafting'
    gathering = 'gathering'
    buy_ge = 'buy_ge'
    sell_ge = 'sell_ge'
    delete_item = 'delete_item'
    deposit_bank = 'deposit_bank'
    withdraw_bank = 'withdraw_bank'
    equip = 'equip'
    unequip = 'unequip'
    task = 'task'
    recycling = 'recycling'


class FightResult(StrEnum):
    win = 'win'
    lose = 'lose'


class ItemCode(StrEnum):
    ash_tree = 'ash_wood'

