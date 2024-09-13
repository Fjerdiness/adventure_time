import random
import sys
from general import actions, inventory, stats, inventory

class Locations:

    def __init__(self, name: str, enemies: str, description: str, treasures: str) -> None:
        self.name = name
        self.enemies = enemies
        self.description = description
        self.treasures = treasures

    def __repr__(self):
        return f"{self.name}: {self.enemies} ({self.description})"

forest = Locations("Forest", "Orc", "Its dark here", None)
castle = Locations("Castle", "Old guard", "You can feel thousands of years of history here", "Sword")
dungeon = Locations("Dungeon", "Dragon", "Skeleton in chain looking at you", "Skeleton_hand")
house = Locations("House", None, "Just cozy house with nothing really useful inside of it", "Fork")
river = Locations("River", "Siren", "Beatiful song is calling you to swim in waters", "Shield")
lake = Locations("Lake", "Merman", "You can fish here if you want", "Fish")

LOCATIONS = [forest, castle, dungeon, house, river, lake]

def whats_around_you() -> int:
    random_position = random.randrange(0, len(LOCATIONS))
    print(f"""You`re at {LOCATIONS[random_position].name}.
{LOCATIONS[random_position].description}
""")
    return random_position

def is_should_search(position) -> None:
    if str(input("Do you wanna to search here for item? ") == "y"):
        can_you_find_an_item(position)
    else: 
        print("Ok, moving further then")
    
def can_you_find_an_item(position: int) -> bool:
    is_sword_here()
    if not LOCATIONS[position].treasures == None:
        probability = stats.luck.amount_of_points_in * 4 + random.randint(0, 100)
        gold_amount = random.randint(0, 100)
        if 75 < probability <= 100:
            print(f"Great success! You`ve found {LOCATIONS[position].treasures} And {gold_amount}g gold near it")
            items = [LOCATIONS[position].treasures, gold_amount]
            inventory.add_items_to_inventory(items)
            actions.what_to_do()
        elif 25 < probability <= 75:
            print(f"Not so great success, but still ok. You`ve found {LOCATIONS[position].treasures}")
            print(f"{LOCATIONS[position].treasures} was added to your inventory")
            items = [LOCATIONS[position].treasures, gold_amount]
            inventory.add_items_to_inventory(items)
            actions.what_to_do()
        elif probability <= 25:
            print(f"Critical failure and now you are dead")
            sys.exit()
    else:
        print("There are no items around here for sure, stop looking")
        actions.what_to_do()

def is_sword_here() -> bool:
    probability = stats.luck.amount_of_points_in * 2 + random.randint(0, 100)
    if probability >= 500:
        print("Gratz! You`ve found legendary sword and won!")
        sys.exit()
