import random
import sys
from typing import Optional

from general import actions
from general import stats
from general import inventory

class Item:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self) -> str:
        return self.name

class Currency(Item):
    def __init__(self, name: str, shortened_name: str, amount: int) -> None:
        super().__init__(name)
        self.shortened_name = shortened_name
        self.amount = amount

    def __repr__(self) -> str | int:
        return f"Currency: {self.name}, Amount: {self.amount}{self.shortened_name}"


class Weapons(Item):
    def __init__(self, name: str, damage: int, weapon_type: str):
        super().__init__(name)
        self.damage = damage
        self.weapon_type = weapon_type

    def __repr__(self) -> int | str:
        return f"Weapon: {self.name}, Type: {self.weapon_type}, Damage: {self.damage}"
    
class Armor(Item):
    def __init__(self, name: str, body_part: str, armor_points: int, armor_type: str) -> None:
        super().__init__(name)
        self.body_part = body_part
        self.armor_points = armor_points
        self.armor_type = armor_type

    def __repr__(self) -> str:
        return f"{self.armor_type} {self.name}, For {self.body_part}, Gives {self.armor_points} armor points"


class Potions(Item):
    def __init__(self, name: str, effect: str, quantity: int) -> None:
        super().__init__(name)
        self.effect = effect
        self.quantity = quantity

    def __repr__(self) -> str | int:
        return f"Potion: {self.name}, Effect: {self.effect}, Quantity: {self.quantity}"

class Others(Item):
    def __init__(self, name: str, effect: str) -> None:
        super().__init__(name)
        self.effect = effect

    def __repr__(self) -> str | int:
        return f"Other: {self.name}, Effect: {self.effect}"
    
weapons_dict = {
    'Fire Sword': Weapons("Fire Sword", 10, "Fire"),
    'Ice Dagger': Weapons("Ice Dagger", 5, "Ice"),
    'Thunder Hammer': Weapons("Thunder Hammer", 15, "Lightning"),
    'Holy Crossbow': Weapons("Holy Crossbow", 8, "Holy"),
    'Flaming Whip': Weapons("Flaming Whip", 7, "Fire"),
    'Venomous Dagger': Weapons("Venomous Dagger", 6, "Poison"),
    'Mystic Staff': Weapons("Mystic Staff", 12, "Magic"),
    'Giant\'s Club': Weapons("Giant's Club", 20, "Blunt"),
    'Elven Bow': Weapons("Elven Bow", 9, "Ranged"),
    'Lightning Rod': Weapons("Lightning Rod", 11, "Lightning"),
    'Frost Mace': Weapons("Frost Mace", 13, "Ice"),
    'Darkblade': Weapons("Darkblade", 16, "Dark"),
    'Runic Hammer': Weapons("Runic Hammer", 18, "Magic"),
    'Spectral Dagger': Weapons("Spectral Dagger", 8, "Spectral"),
    'Ice Staff': Weapons("Ice Staff", 9, "Ice"),
    'Shadow Blade': Weapons("Shadow Blade", 11, "Shadow"),
    'Celestial Bow': Weapons("Celestial Bow", 12, "Celestial"),
    'Thunder Spear': Weapons("Thunder Spear", 14, "Lightning"),
}


potions_dict = {
    'Health Potion': Potions("Health Potion", "Healing", 3),
    'Mana Potion': Potions("Mana Potion", "Restores MP", 5),
    'Strength Potion': Potions("Strength Potion", "Increases Strength", 2),
    'Healing Herb': Potions("Healing Herb", "Restores HP", 7),
    'Elixir of Wisdom': Potions("Elixir of Wisdom", "Increases Intelligence", 1),
    'Mana Elixir': Potions("Mana Elixir", "Restores MP", 4),
    'Potion of Speed': Potions("Potion of Speed", "Increases Speed", 3),
    'Healing Talisman': Potions("Healing Talisman", "Restores HP", 6),
    'Elixir of Strength': Potions("Elixir of Strength", "Increases Strength", 2),
    'Mystic Potion': Potions("Mystic Potion", "Grants Magic Power", 2),
}

armor_dict = {
    # Heavy Armor
    'Steel Shield': Armor("Steel Shield", "Shield", 5, "Heavy"),
    'Iron Helmet': Armor("Iron Helmet", "Head", 3, "Heavy"),
    'Dragon Scale Armor': Armor("Dragon Scale Armor", "Body", 10, "Heavy"),
    'Heavy Plate Shield': Armor("Heavy Plate Shield", "Shield", 7, "Heavy"),
    'Steel Pauldrons': Armor("Steel Pauldrons", "Shoulders", 4, "Heavy"),
    'Golden Breastplate': Armor("Golden Breastplate", "Body", 8, "Heavy"),
    'Plate Leggings': Armor("Plate Leggings", "Legs", 7, "Heavy"),
    'Rune-etched Shield': Armor("Rune-etched Shield", "Shield", 8, "Heavy"),
    
    # Medium Armor
    'Leather Chestplate': Armor("Leather Chestplate", "Body", 6, "Medium"),
    'Chainmail Sleeves': Armor("Chainmail Sleeves", "Arms", 4, "Medium"),
    'Iron Greaves': Armor("Iron Greaves", "Legs", 5, "Medium"),
    'Plated Helmet': Armor("Plated Helmet", "Head", 5, "Medium"),
    'Mystic Shield': Armor("Mystic Shield", "Shield", 5, "Medium"),
    'Chainmail Vest': Armor("Chainmail Vest", "Body", 7, "Medium"),
    'Reinforced Leggings': Armor("Reinforced Leggings", "Legs", 6, "Medium"),
    'Iron Bracers': Armor("Iron Bracers", "Arms", 4, "Medium"),
    
    # Light Armor
    'Elven Boots': Armor("Elven Boots", "Legs", 2, "Light"),
    'Woolen Gloves': Armor("Woolen Gloves", "Gloves", 1, "Light"),
    'Mage Robe': Armor("Mage Robe", "Body", 2, "Light"),
    'Leather Gloves': Armor("Leather Gloves", "Gloves", 2, "Light"),
    'Elven Helm': Armor("Elven Helm", "Head", 4, "Light"),
    'Mystic Gauntlets': Armor("Mystic Gauntlets", "Gloves", 3, "Light"),
    'Leather Helm': Armor("Leather Helm", "Head", 2, "Light"),
    'Gilded Gauntlets': Armor("Gilded Gauntlets", "Gloves", 5, "Light"),
    'Steel Boots': Armor("Steel Boots", "Legs", 3, "Light"),
}

others_dict = {
    'Torch': Others("Torch", "Lighting surroundings"),
    'Dragon Scale': Others("Dragon Scale", "Rare Material"),
    'Magic Scroll': Others("Magic Scroll", "Contains Spell"),
    'Cursed Amulet': Others("Cursed Amulet", "Cursed Item"),
    'Phoenix Feather': Others("Phoenix Feather", "Revives a Character"),
    'Shadow Cloak': Others("Shadow Cloak", "Grants Stealth"),
    'Ancient Tome': Others("Ancient Tome", "Contains Ancient Knowledge"),
    'Divine Shield': Others("Divine Shield", "Protective Shield"),
    'Golden Ring': Others("Golden Ring", "Valuable Jewelry"),
    'Fireball Scroll': Others("Fireball Scroll", "Casts Fireball Spell"),
    'Magic Ring': Others("Magic Ring", "Grants Magical Abilities"),
    'Elven Cloak': Others("Elven Cloak", "Grants Agility"),
}

gold_dict = {
    'Gold': Currency("Gold", "g", 0),
}



dictionaries = {
    'weapon': weapons_dict,
    'potion': potions_dict,
    'other': others_dict,
    'armor': armor_dict,
    'gold': gold_dict,
}

def get_item_name(dict_type: str) -> str:
    item_dict = dictionaries.get(dict_type)
    if item_dict is not None:
        return random.choice(list(item_dict.keys()))
    else:
        raise ValueError(f"Dictionary for '{dict_type}' not found.")

def get_item(dict_type: str):
    key = get_item_name(dict_type)
    dict_to_use = dictionaries.get(dict_type)
    
    if dict_to_use is not None:
        item_of_select = dict_to_use.get(key)
        # print(item_of_select)
        return item_of_select
    else:
        print(f"Dictionary for '{dict_type}' not found.")
        return None
    
def get_treasures(probability: Optional[int] = None) -> list[str, int, str]:
    if not probability == None:
        probability = probability
    else:
        probability = stats.stats_dict['luck'].amount_of_points_in * 4 + random.randint(0, 100)

    if 75 < probability <= 100:
        print("Great success")
        return [
            get_item("weapon"),
            get_item("potion"),
            get_item("gold"),
        ]
    elif 50 < probability <= 75:
         print("Not so great, but OK success")
         return [
            get_item("potion"),
            get_item("gold"),
        ]
    elif 25 < probability <= 50:
         print("Not so great, but OK success")
         return [
            get_item("gold"),
        ]
    else:
        print(f"Critical failure and now you are dead")
        # sys.exit()


def can_you_find_an_item() -> bool:
    items_to_find = get_treasures()
    inventory.add_items_to_inventory(items_to_find)
