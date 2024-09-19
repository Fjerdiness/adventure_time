import sys
from general import npcs

from . import inventory, locations

LOCATION_LIST = locations.select_three_random_locations()
current_location = None

class Actions:
    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self):
        return f"{self.name}"

actions_dict = {
    "inventory": Actions("inventory"),
    "stop": Actions("stop"),
    "attack":Actions("attack")
}

yes_no_dict = {
     "yes": Actions("yes"),
     "no": Actions("no"),
}

def input_to_play():
    user_input = str(input(f"Hello. Do you wanna to play? {list(yes_no_dict.keys())} ")).lower().strip()
    if user_input == yes_no_dict["yes"].name:
        print("Nice, lets go!")
    elif user_input == yes_no_dict["no"].name:
        print("As you wish")
        sys.exit()
    else:
        print("wrong input, retry")
        input_to_play()

def what_to_do() -> str:
        global LOCATION_LIST
        while True:
            user_input = str(input(f"Where do you wanna go? {LOCATION_LIST} or {list(actions_dict.keys())} "))
            if user_input in LOCATION_LIST or user_input in actions_dict.keys():
                return user_input
            else:
                print("Wrong input. Retry.")

def process_user_input(where_to):
        global LOCATION_LIST
        global current_location
        if where_to == actions_dict["inventory"].name:
            inventory.check_inventory()
        elif where_to in LOCATION_LIST:
            print(locations.locations_dict[where_to])
            current_location = locations.locations_dict[where_to]
            locations.is_should_search()
        elif where_to == actions_dict["attack"].name:
            try:
                npc = npcs.get_npc(current_location.npc.name)
                is_npc_dead = npcs.npc_fight(npcs.npc_dict[npc.name])
                current_location = update_npc_location_list(current_location.name, is_npc_dead)
            except AttributeError: print("There is no one to fight with!")
        elif where_to == "stop":
            print(f"Bye-bye! Have a nice day!")
            sys.exit()
        else:
            print("Invalid action, please retry")
            process_user_input()

def update_npc_location_list(where_to, is_npc_dead):
    where_to = where_to.lower()
    if is_npc_dead == True and where_to in LOCATION_LIST:
        current_location = locations.locations_dict[where_to]
        new_location = locations.Locations(
                    name=current_location.name,
                    npc=None,  # Set npc to None after defeating it
                    description=current_location.description
                )
        locations.locations_dict.update({where_to: new_location})
        return locations.locations_dict[where_to]