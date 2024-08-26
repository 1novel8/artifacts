import datetime
import typing

from src.character.enum import CooldownReason, FightResult
from src.common.dto import BaseDto
from src.map.api.schema import MapSchema


class InventorySlot(BaseDto):
    slot: int
    code: str
    quantity: int


class CharacterSchema(BaseDto):
    name: str
    skin: str
    level: int
    xp: int
    max_xp: int
    gold: int
    speed: int
    mining_level: int
    mining_xp: int
    mining_max_xp: int
    woodcutting_level: int
    woodcutting_xp: int
    woodcutting_max_xp: int
    fishing_level: int
    fishing_xp: int
    fishing_max_xp: int
    weaponcrafting_level: int
    weaponcrafting_xp: int
    weaponcrafting_max_xp: int
    gearcrafting_level: int
    gearcrafting_xp: int
    gearcrafting_max_xp: int
    jewelrycrafting_level: int
    jewelrycrafting_xp: int
    jewelrycrafting_max_xp: int
    cooking_level: int
    cooking_xp: int
    cooking_max_xp: int
    hp: int
    haste: int
    critical_strike: int
    stamina: int
    attack_fire: int
    attack_earth: int
    attack_water: int
    attack_air: int
    dmg_fire: int
    dmg_earth: int
    dmg_water: int
    dmg_air: int
    res_fire: int
    res_earth: int
    res_water: int
    res_air: int
    x: int
    y: int
    cooldown: int
    cooldown_expiration: datetime.datetime
    weapon_slot: str
    shield_slot: str
    helmet_slot: str
    body_armor_slot: str
    leg_armor_slot: str
    boots_slot: str
    ring1_slot: str
    ring2_slot: str
    amulet_slot: str
    artifact1_slot: str
    artifact2_slot: str
    artifact3_slot: str
    consumable1_slot: str
    consumable1_slot_quantity: int
    consumable2_slot: str
    consumable2_slot_quantity: int
    task: str
    task_type: str
    task_progress: int
    task_total: int
    inventory_max_items: int
    inventory: list[InventorySlot]


class CooldownSchema(BaseDto):
    total_seconds: int
    remaining_seconds: int
    started_at: datetime.datetime
    expiration: datetime.datetime
    reason: CooldownReason


class BlockedHitsSchema(BaseDto):
    fire: int
    earth: int
    water: int
    air: int
    total: int


class DropSchema(BaseDto):
    code: str
    quantity: int


class FightSchema(BaseDto):
    xp: int
    gold: int
    drops: list[DropSchema]
    turns: int
    monster_blocked_hits: BlockedHitsSchema
    player_blocked_hits: BlockedHitsSchema
    logs: list[str]
    result: FightResult


class CharacterFightDataSchema(BaseDto):
    cooldown: CooldownSchema
    fight: FightSchema
    character: CharacterSchema


class SkillInfoSchema(BaseDto):
    xp: int
    items: list[DropSchema]


class SkillDataSchema(BaseDto):
    cooldown: CooldownSchema
    details: SkillInfoSchema
    character: CharacterSchema


class CharacterMovementDataSchema(BaseDto):
    cooldown: CooldownSchema
    destination: MapSchema
    character: CharacterSchema


class CraftingRequestSchema(BaseDto):
    code: str
    quantity: int


class EquipResponseSchema(BaseDto):
    cooldown: CooldownSchema
    slot: str
    item: typing.Any  #TODO: add schema
    character: CharacterSchema


class EquipRequestSchema(BaseDto):
    code: str
    slot: str
    quantity: int


class UnequipRequestSchema(BaseDto):
    slot: str
    quantity: int


class CharacterMoveSchema(BaseDto):
    x: int
    y: int
