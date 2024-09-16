from general.tuples import items

hotbar = [
    
]

inventory_dict = {

}


def switch_to_item_from_hotbar(item_to_take: str) -> None:
    index = hotbar.index(item_to_take)
    item = hotbar.pop(index)
    hotbar.insert(0, item)
    print(f"""
You took {item_to_take} in hand. 
{item} now is stored on the belt
""")
    
def add_items_to_inventory(item_list: list) -> None:
    global gold_amount
    for item in item_list:
        # Directly add the Item object to the dictionary
            item_name = item.name
            inventory_dict[item_name] = item
            print(f"\n{item_name} now is stored in your inventory")
    check_inventory()
            
def move_item_to_hotbar(item_to_move: str) -> None: 
    try:
        index = inventory_dict.index(item_to_move)
        if item_to_move in hotbar:
            print(f"You already have {item_to_move} on your belt")
        else:
            item = inventory_dict.pop(index)
            hotbar.insert(0, item)
            print(f"""
You moved {item_to_move} to hand. 
{item} was removed from your inventory {inventory_dict}
""")
    except ValueError:
        print(f"You don't have {item_to_move} in your inventory {inventory_dict}")

def check_inventory() -> None:
    print("\nList of items in your inventory: ")
    for item in inventory_dict.items():
        print(f"{item}")

def do_smthng_with_inventory() -> str:
    input: str = input(f"""Do you want to do something in inventory? 
""")
    return input

if __name__ == "__main__":
    add_items_to_inventory(items.get_treasures())
    gold_amount = items.get_item("gold")