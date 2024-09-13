MAX_SKILL_VALUE = 10

class Stats:

    def __init__(self, name: str, amount_of_points_in: int, description: str) -> None:
        self.name = name
        self.amount_of_points_in = amount_of_points_in
        self.description = description

    def __repr__(self):
        return f"{self.name}: {self.amount_of_points_in} ({self.description})"

luck = Stats("Luck", 1, "How lucky are you")
strength = Stats("Strength", 1, "How strong are you")
intelligence = Stats("Intelligence", 1, "How smart are you")
agility = Stats("Agility", 1, "How agile are you")

stats_list = [luck, strength, intelligence, agility]

def set_stats() -> int:
    for index, stat in enumerate(stats_list):
        while True:
            try:
                skill_value = int(input(f"""
Input digit 0 - 10 to set it for 
{stat.name} ({stat.description})
"""))
                if 0 < skill_value < MAX_SKILL_VALUE:
                    stats_list[index].amount_of_points_in = skill_value
                    break
            except ValueError:
                print("Wrong value, retry")
                continue
    
def show_stas(): 
    for stat in stats_list:
        print(f"""
So, your final stats are: {stat.name} {stat.amount_of_points_in}              
""")