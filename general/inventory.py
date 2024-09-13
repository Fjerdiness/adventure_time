
hotbar = [
    'Torch',
    'Rock',
    'Potion',
]

inventory = []

gold_amount = 0


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
        if isinstance(item, int):
            gold_amount += item
            print(f"""Now you have {gold_amount}g in your pocket
                  """)
        else:
            inventory.append(item)
            print(f"""
{item} now is stored in your inventory

List of items in your inventory: 
{inventory}
""")
            
def move_item_to_hotbar(item_to_move: str) -> None: 
    try:
        index = inventory.index(item_to_move)
        if item_to_move in hotbar:
            print(f"You already have {item_to_move} on your belt")
        else:
            # Remove the item from the inventory
            item = inventory.pop(index)
            # Add the item to the hotbar
            hotbar.insert(0, item)
            print(f"""
You moved {item_to_move} to hand. 
{item} was removed from your inventory {inventory}
""")
    except ValueError:
        print(f"You don't have {item_to_move} in your inventory {inventory}")
