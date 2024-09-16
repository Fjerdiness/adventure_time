
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

def get_NPC_name() -> str:
    return random.choice(list(npc_dict.keys()))

def get_NPC():
    key = get_NPC_name()
    npc_of_select = npc_dict.get(key)
    print(npc_of_select.name)
    return npc_of_select

def attack_npc() -> int:
    npc = get_NPC()
    weapon_dmg = items.get_item('weapon').damage
    player_dmg = stats.stats_dict['strength'].amount_of_points_in * 4 + weapon_dmg
    return npc.hit_points - player_dmg