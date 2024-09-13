import random
from general import stats

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
    
def can_you_find_item(position: int) -> bool:
    if not LOCATIONS[position].treasures == None:
        probability = stats.luck.amount_of_points_in * 4 + random.randint(0, 100)
        if 75 < probability <= 100:
            print(f"Great success! You`ve found {LOCATIONS[position].treasures} And {random.randint(0, 100)} gold near it")
            print(f"Item and gold was added to inventory")
        elif 25 < probability <= 75:
            print(f"Not so great success, but still ok. You`ve found {LOCATIONS[position].treasures}")
            print(f"Item was added to your inventory")
        elif probability <= 25:
            print(f"Critical failure and you dead")
            quit()
    else:
        print("There are no items around here for sure, stop looking")
