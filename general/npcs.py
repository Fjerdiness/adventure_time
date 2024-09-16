
import random
from general.tuples import items
from general import stats


class NPCs:
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

# Define the NPCs
npc_dict = {
    'Gorath': NPCs(
        name="Gorath",
        hit_points=120,
        mana_points=30,
        armor=15,
        hostility=80,
        items=[items.get_item('weapon'), items.get_item('armor')]
    ),
    'Eldara': NPCs(
        name="Eldara",
        hit_points=100,
        mana_points=50,
        armor=5,
        hostility=30,
        items=[items.get_item('weapon')]
    ),
    'Thorin': NPCs(
        name="Thorin",
        hit_points=150,
        mana_points=10,
        armor=20,
        hostility=60,
        items=[items.get_item('weapon'), items.get_item('armor'), items.get_item('armor'), items.get_item('armor')]
    ),
    'Lyra': NPCs(
        name="Lyra",
        hit_points=90,
        mana_points=70,
        armor=8,
        hostility=20,
        items=[items.get_item('potion') for _ in range(20)]
    ),
}

def get_npc_name() -> str:
    return random.choice(list(npc_dict.keys()))

def get_npc():
    key = get_npc_name()
    npc = npc_dict.get(key)
    print(npc.name)
    return npc

def get_npc_armor_points(npc: NPCs) -> int:
    points = 1
    for item in npc.items:
        if isinstance(item, items.Armor):
            points += item.armor_points
    print(f"NPC AP: {points}")
    return points


def player_attack_npc(npc: NPCs) -> int:
    weapon_dmg = items.get_item('weapon').damage
    player_dmg = stats.stats_dict['strength'].amount_of_points_in * 4 + weapon_dmg
    npc_armor_points = get_npc_armor_points(npc)
    return f"{npc.name}{npc.hit_points - int(player_dmg / npc_armor_points)}"