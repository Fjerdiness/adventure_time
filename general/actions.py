import sys
from general import npcs

from . import inventory, locations


class Actions:
    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self):
        return f"{self.name}"

actions_dict = {
    "west": Actions("west"),
    "east": Actions("east"),
    "north": Actions("north"),
    "south": Actions("south"),
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
        user_input = str(input(f"Where do you wanna go? {list(actions_dict.keys())} ")).strip().lower()
        if user_input in actions_dict:
            return user_input
        else:
            print("Wrong input. Retry.")
            what_to_do()

def process_user_input(where_to):

        if where_to == actions_dict["inventory"].name:
            inventory.check_inventory()
        elif where_to in [actions_dict["east"].name, actions_dict["north"].name, actions_dict["south"].name, actions_dict["west"].name]:
            location = locations.select_location()
            locations.whats_around_you(location)
            locations.is_should_search()
        elif where_to == actions_dict["attack"].name:
            npc_name = npcs.get_npc_name()
            npcs.npc_fight(npcs.npc_dict[npc_name])
        elif where_to == "stop":
            print(f"Bye-bye! Have a nice day!")
            sys.exit()
        else:
            print("Invalid action, please retry")
            process_user_input()