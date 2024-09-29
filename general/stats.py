import tkinter as tk
from tkinter import ttk
MAX_SKILL_VALUE = 10
MIN_SKILL_VALUE = 0
SKILL_POINTS = 15
DEFAULT_HP = 200
DEFAULT_MP = 50
DEFAULT_AP = 0
DEFAULT_NAME = "Player"

class Stats:

    def __init__(self, name: str, amount_of_points_in: int, description: str) -> None:
        self.name = name
        self.amount_of_points_in = amount_of_points_in
        self.description = description

    def __repr__(self):
        return f"{self.amount_of_points_in} ({self.description})"
    
class Character():
    """Character stats, like HP, MP, Level, reputation, etc"""
    def __init__(self, name: str, player_hp: int, player_mp: int, player_lvl: int, player_armor_points: int):
        self.name = name
        self.player_hp = player_hp
        self.player_mp = player_mp
        self.player_lvl = player_lvl
        self.player_armor_points = player_armor_points

    def __repr__(self):
        return f"Player name: {self.name.capitalize()}, HP: {self.player_hp}, MP: {self.player_mp}, LVL: {self.player_lvl}, Armor: {self.player_armor_points}"
    
stats_dict = {
    "luck": Stats("Luck", MIN_SKILL_VALUE, "Amount of gold, potions, critical damages etc"),
    "strength": Stats("Strength", MIN_SKILL_VALUE, "Damage from weapon and HP"),
    "intelligence": Stats("Intelligence", MIN_SKILL_VALUE, "Mana points"),
    "agility": Stats("Agility", MIN_SKILL_VALUE, "Lowering damage taken")
}

player_hp = (DEFAULT_HP + (stats_dict["strength"].amount_of_points_in * 10))
player_mp = (DEFAULT_MP + (stats_dict["intelligence"].amount_of_points_in * 20))
player_armor_points = (DEFAULT_AP + (stats_dict["agility"].amount_of_points_in * 2))

character_dict = {
    "player": Character(DEFAULT_NAME, player_hp, player_mp, 1, player_armor_points)
}  


def set_character_stats(window) -> int:
    skill_points = SKILL_POINTS
    max_skill_value = MAX_SKILL_VALUE

    frame = tk.Frame(window, bg="lightgray")
    frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    def submit_points():
        nonlocal skill_points
        for key, value in stats_dict.items():
            try:
                skill_point_input = int(skill_entries[key].get())
                
                if 0 <= skill_point_input <= skill_points and 0 <= skill_point_input <= max_skill_value:
                    stats_dict[key] = Stats(value.name, skill_point_input, value.description)
                    skill_points -= skill_point_input
                else:
                    print(f"Please input a value between 0 and {min(skill_points, max_skill_value)}.")
            except ValueError:
                print("Invalid input. Please enter an integer value.")

        show_stats()

    skill_entries = {}
    for key, value in stats_dict.items():
        label = tk.Label(frame, text=f"Enter points for {value.name} ({value.description}):")
        label.pack()
        
        skill_entry = tk.Entry(frame)
        skill_entry.pack()
        skill_entries[key] = skill_entry

    submit_button = tk.Button(frame, text="Submit Skill Points", command=submit_points)
    submit_button.pack()

def show_stats(): 
    print("So, your final stats are:")
    for key, value in stats_dict.items():
        print(f"{key.capitalize()}: {value.amount_of_points_in} ({value.description})")