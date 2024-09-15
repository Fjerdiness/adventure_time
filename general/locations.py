import random
import sys

from general.tuples import items
from . import actions, stats, inventory

class Locations:

    def __init__(self, name: str, enemies: str, description: str, treasures_list: list[str, int, str]) -> None:
        self.name = name
        self.enemies = enemies
        self.description = description
        self.treasures_list = treasures_list

    def __repr__(self) -> str:
        treasures_str = ', '.join(f"{name} (Quantity: {quantity}, Type: {type_})" for name, quantity, type_ in self.treasures_list)
        return f"Location(name={self.name}, enemies={self.enemies}, description={self.description}, treasures=[{treasures_str}])"

# sword = Weapons("Sword", 10, "Sharp")
    
locations_dict = {
    "forest" : Locations("Forest", "Orc", "its dark here", None),
    "castle" : Locations("Castle", "Old guard", "you can feel thousands of years of history here", None),
    "dungeon" : Locations("Dungeon", "Dragon", "skeleton in chain is looking at you", None),
    "house" : Locations("House", None, "just cozy house with nothing really useful inside of it", None),
    "river" : Locations("River", "Siren", "beatiful song is calling you to swim in waters", None),
    "lake" : Locations("Lake", "Merman", "you can fish here if you want", None),
}

def select_location() -> str:
    location = random.choice(list(locations_dict.keys()))
    return location

def whats_around_you(user_input: str) -> None:
    if user_input in locations_dict:
        location = locations_dict[user_input]
        print(f"""You're at {location.name} {location.description}
""")
    else:
        print("Location not found.")

def is_should_search() -> None:
    input_str = input(f"Do you wanna to search here for item? {list(actions.yes_no_dict.keys())} ")
    if input_str == actions.yes_no_dict["yes"].name:
        items.can_you_find_an_item()
    else: 
        print("Ok, moving further then")

def is_sword_here() -> bool:
    probability = stats.stats_dict['luck'].amount_of_points_in * 2 + random.randint(0, 100)
    if probability >= 500:
        print("Gratz! You`ve found legendary sword and won!")
        sys.exit()