
import random
from typing import Optional
from general.tuples import items
from general import stats
from general import inventory


class NPC:
    def __init__(self, 
                 name: str, 
                 hit_points: int, 
                 mana_points: int,
                 armor: int,
                 hostility: int,
                 items: list,
                 ) -> None:
        
        self.name = name
        self.hit_points = hit_points
        self.mana_points = mana_points
        self.armor = armor
        self.hostility = hostility
        self.items = items

    def __repr__(self) -> str:
        return (f"NPC(Name: {self.name}, "
                f"Hit Points: {self.hit_points}, "
                f"Mana Points: {self.mana_points}, "
                f"Armor: {self.armor}, "
                f"Hostility: {self.hostility}, "
                f"Items: {self.items})")

# Define the NPCs
npc_dict = {
    'Gorath': NPC(
        name="Gorath",
        hit_points=120,
        mana_points=30,
        armor=15,
        hostility=80,
        items=[items.get_item('weapon'), items.get_item('armor')]
    ),
    'Eldara': NPC(
        name="Eldara",
        hit_points=100,
        mana_points=50,
        armor=5,
        hostility=30,
        items=[items.get_item('weapon')]
    ),
    'Thorin': NPC(
        name="Thorin",
        hit_points=150,
        mana_points=10,
        armor=20,
        hostility=60,
        items=[items.get_item('weapon'), items.get_item('armor'), items.get_item('armor'), items.get_item('armor')]
    ),
    'Lyra': NPC(
        name="Lyra",
        hit_points=90,
        mana_points=70,
        armor=8,
        hostility=20,
        items=[items.get_item('potion') for _ in range(20)]
    ),
}

def get_random_npc(npc_name = random.choice(list(npc_dict.keys()))) -> NPC | str:
    # Check if the specified NPC name exists in the npc_dict
    if npc_name in npc_dict:
        return npc_dict[npc_name]
    else:
        print(f"NPC '{npc_name}' not found.")
        return None  # or raise an exception
    

def get_npc(npc_name: str)-> NPC | str:
    # Check if the specified NPC name exists in the npc_dict
    if npc_name in npc_dict:
        return npc_dict[npc_name]
    else:
        print(f"NPC '{npc_name}' not found.")
        return None  # or raise an exception

def get_npc_armor_points(npc: NPC) -> int:
    npc_ap_points = npc.armor
    for item in npc.items:
        if isinstance(item, items.Armor):
            npc_ap_points += item.armor_points
    return npc_ap_points


def player_attack_npc(npc: NPC, weapon_name: str) -> int:
    if weapon_name is not None:
        weapon_dmg = weapon_name.damage() if callable(getattr(weapon_name, 'damage', None)) else weapon_name.damage
    else:
        weapon_dmg = 2 
    weapon_dmg = weapon_name.damage
    weapon_name = weapon_name.name
    player_dmg = stats.stats_dict['strength'].amount_of_points_in * 4 + weapon_dmg
    npc_armor_points = get_npc_armor_points(npc)

    effective_damage = max(player_dmg - npc_armor_points, 1)
    npc.hit_points -= effective_damage

    print(f"Player attacks {npc.name} (AP: {npc_armor_points}) with {weapon_name} for {effective_damage} damage. {npc.name} has {npc.hit_points} HP left.")
    return npc.hit_points

def npc_fight(npc: NPC) -> bool:
    npc_hp = npc.hit_points
    weapon_name = items.get_item('weapon')
    while True:
        npc_hp = player_attack_npc(npc, weapon_name)
        if npc_hp <= 0:
            print(f"Player won! {npc.name} is defeated.")
            inventory.add_items_to_inventory(npc.items)
            return True