import random
import sys
import tkinter as tk
from general.tuples import items
from . import actions, stats, npcs

class Locations:

    def __init__(self, name: str, npc, description: str) -> None:
        self.name = name
        self.npc = npc
        self.description = description

    def __repr__(self) -> str:
        if self.npc is not None:
            return f"You arrived at {self.name}, {self.description}. And {self.npc.name} is standing in front of you."
        else:
            return f"You arrived at {self.name}, {self.description}. There is no one here."

    
locations_dict = {
    "forest": Locations("Forest", npcs.get_random_npc(), "It's dark here, the trees whisper secrets."),
    "castle": Locations("Castle", npcs.get_random_npc(), "You can feel thousands of years of history here."),
    "dungeon": Locations("Dungeon", npcs.get_random_npc(), "A skeleton in chains is looking at you."),
    "house": Locations("House", None, "Just a cozy house with nothing really useful inside of it."),
    "river": Locations("River", npcs.get_random_npc(), "A beautiful song is calling you to swim in the waters."),
    "lake": Locations("Lake", npcs.get_random_npc(), "You can fish here if you want."),
    "mountain": Locations("Mountain", None, "The peak is shrouded in clouds, and the air is thin."),
    "cave": Locations("Cave", npcs.get_random_npc(), "Echoes of dripping water create a haunting melody."),
    "village": Locations("Village", npcs.get_random_npc(), "A quaint village where everyone knows each other."),
    "ruins": Locations("Ruins", None, "Ancient stones tell the tale of a lost civilization."),
    "swamp": Locations("Swamp", npcs.get_random_npc(), "The air is thick with mist and the smell of decay."),
    "beach": Locations("Beach", None, "Soft sands stretch as far as the eye can see, with gentle waves lapping at the shore."),
    "temple": Locations("Temple", npcs.get_random_npc(), "An ancient temple filled with mysterious relics."),
    "hill": Locations("Hill", None, "From here, you can see the entire valley spread out below."),
    "city_square": Locations("City Square", npcs.get_random_npc(), "A bustling area filled with merchants and townsfolk."),
    "tavern": Locations("Tavern", npcs.get_random_npc(), "The smell of ale and roasting meat fills the air."),
    "plains": Locations("Plains", None, "Wide open fields stretch in every direction, a gentle breeze rustling the grass."),
    "fortress": Locations("Fortress", npcs.get_random_npc(), "A stronghold that has withstood the test of time."),
    "glen": Locations("Glen", None, "A hidden glen filled with vibrant flowers and chirping birds."),
    "graveyard": Locations("Graveyard", npcs.get_random_npc(), "The air is heavy with the memories of the past."),
    "marketplace": Locations("Marketplace", npcs.get_random_npc(), "Vendors shout their wares, and the smell of spices fills the air."),
    "crystal_cave": Locations("Crystal Cave", None, "Glittering crystals reflect the light in mesmerizing patterns."),
    "meadow": Locations("Meadow", npcs.get_random_npc(), "A sunlit meadow where butterflies dance among wildflowers."),
    "snowy_tundra": Locations("Snowy Tundra", None, "Endless white stretches before you, cold and desolate."),
    "abandoned_ship": Locations("Abandoned Ship", npcs.get_random_npc(), "The old ship creaks, telling tales of adventures long past."),
    "sacred_grove": Locations("Sacred Grove", npcs.get_random_npc(), "A tranquil grove where the air feels charged with magic."),
    "hidden_path": Locations("Hidden Path", None, "A narrow path winding through thick underbrush, leading who knows where."),
    "fishing_hole": Locations("Fishing Hole", npcs.get_random_npc(), "A peaceful spot perfect for casting a line and relaxing."),
    "burnt_forest": Locations("Burnt Forest", None, "Charred remains tell the tale of a fierce fire that swept through."),
    "whirlpool": Locations("Whirlpool", npcs.get_random_npc(), "A swirling vortex in the water, rumored to lead to another realm."),
}


def select_three_random_locations() -> list[str]:
    location = [random.choice(list(locations_dict.keys())) for _ in range(3)] 
    return location


def is_should_search(window, secondary_frame) -> None:
    input_label = tk.Label(window, text=f"Do you wanna to search here for item? {list(actions.yes_no_dict.keys())}")
    input_label.pack()
    search_btn = tk.Button(window, text="Yes, I wanna search for an item", command=lambda: (items.can_you_find_an_item(secondary_frame), clear_btns(button_list), input_label.destroy()))
    no_search_btn = tk.Button(window, text="No, lets skip searching", command=lambda:(print("Ok, moving further then"), clear_btns(button_list), input_label.destroy()))
    button_list = [search_btn, no_search_btn]
    search_btn.pack()
    no_search_btn.pack()

def clear_btns(button_list: list):
    for button in button_list:
        button.destroy()
        

def is_sword_here() -> bool:
    probability = stats.stats_dict['luck'].amount_of_points_in * 2 + random.randint(0, 100)
    if probability >= 500:
        print("Gratz! You`ve found legendary sword and won!")
        sys.exit()