
class Actions:
    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self):
        return f"{self.name}"

go_west = Actions("west")
go_east = Actions("east")
go_north = Actions("north")
go_south = Actions("south")
go_to_inventory = Actions("inventory")
# go_to_char_stats = Actions("Not implemented yet")

actions = [go_west.name, go_east.name, go_north.name, go_south.name, go_to_inventory]

def what_to_do() -> str:
    while True:
        user_input = str(input(f"Where do you wanna go? {actions} ")).strip().lower()
        if user_input in actions:
            return user_input
        else:
            print("Wrong input. Retry.")
            continue