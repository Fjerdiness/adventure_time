import sys
from general import npcs
from general import stats
import tkinter as tk
from tkinter import ttk
import gui

from . import inventory, locations

LOCATION_LIST = locations.select_three_random_locations()
CURRENT_LOCATION = None

class Actions:
    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self):
        return f"{self.name}"

actions_dict = {
    "inventory": Actions("inventory"),
    "stop": Actions("stop"),
    "attack": Actions("attack"),
    "character": Actions("character"),
}

yes_no_dict = {
     "yes": Actions("yes"),
     "no": Actions("no"),
}

def input_to_play(window):
    button_yes = tk.Button(window, text="Yes", command=lambda: (print("Nice, lets go!"), gui.clear_window(window), stats.set_character_stats(window)))
    button_no = tk.Button(window, text="No", command=lambda: (print("As you wish"), sys.exit()))
    button_yes.pack(pady=10)
    button_no.pack(pady=10)

def what_to_do(window) -> str:
        global LOCATION_LIST
        label = tk.Label(window, text=f"Where do you wanna go? {LOCATION_LIST} or {list(actions_dict.keys())} ")
        label.pack()
        
        entry = tk.Entry(window)
        entry.pack()
        # user_input = str(entry.get())
        
        submit_button = tk.Button(window, text="Submit", command=lambda: (process_user_input(entry.get(), window)))
        submit_button.pack()
        
        # if user_input in LOCATION_LIST or user_input in actions_dict.keys():
        #     process_user_input(user_input)
        # else:
        #     print("Wrong input. Retry.")

def process_user_input(where_to, window):
        global LOCATION_LIST
        global CURRENT_LOCATION
        if where_to == actions_dict["inventory"].name:
            inventory.check_inventory()
        elif where_to in LOCATION_LIST:
            print(locations.locations_dict[where_to])
            CURRENT_LOCATION = locations.locations_dict[where_to]
            locations.is_should_search(window)
        elif where_to == actions_dict["attack"].name:
            if hasattr(CURRENT_LOCATION, 'npc') and CURRENT_LOCATION.npc:
                npc = npcs.get_npc(CURRENT_LOCATION.npc.name)
                is_npc_dead = npcs.npc_fight(npcs.npc_dict[npc.name])
                CURRENT_LOCATION = update_npc_location_list(CURRENT_LOCATION.name, is_npc_dead)
            else:
                print("There is no one to fight with!")
        elif where_to == actions_dict["character"].name:
            print(stats.character_dict["player"])
        elif where_to == actions_dict["stop"].name:
            print(f"Bye-bye! Have a nice day!")
            sys.exit()

def update_npc_location_list(where_to, is_npc_dead):
    where_to = where_to.lower()
    if is_npc_dead and where_to in LOCATION_LIST:
        current_location = locations.locations_dict[where_to]
        new_location = locations.Locations(
                    name=current_location.name,
                    npc=None,  # Set npc to None after defeating it
                    description=current_location.description
                )
        locations.locations_dict.update({where_to: new_location})
        return locations.locations_dict[where_to]