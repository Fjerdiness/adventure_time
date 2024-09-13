MAX_SKILL_VALUE = 10
MIN_SKILL_VALUE = 0
SKILL_POINTS = 15

class Stats:

    def __init__(self, name: str, amount_of_points_in: int, description: str) -> None:
        self.name = name
        self.amount_of_points_in = amount_of_points_in
        self.description = description

    def __repr__(self):
        return f"{self.name}: {self.amount_of_points_in} ({self.description})"
    
luck = Stats("Luck", {MIN_SKILL_VALUE}, "How lucky are you")
strength = Stats("Strength", {MIN_SKILL_VALUE}, "How strong are you")
intelligence = Stats("Intelligence", {MIN_SKILL_VALUE}, "How smart are you")
agility = Stats("Agility", {MIN_SKILL_VALUE}, "How agile are you")

stats_list = [luck, strength, intelligence, agility]

def set_stats() -> int:
    skill_points = SKILL_POINTS
    max_skill_value = MAX_SKILL_VALUE
    for index, stat in enumerate(stats_list):
        while True:
            try:
                skill_value = int(input(f"""
Input digit {MIN_SKILL_VALUE} - {max_skill_value} to set it for 
{stat.name} ({stat.description})
{skill_points} skill points left
"""))
                if MIN_SKILL_VALUE <= skill_value <= max_skill_value:
                    skill_points -= skill_value
                    stats_list[index].amount_of_points_in = skill_value
                    if skill_points <= max_skill_value: 
                        max_skill_value = skill_points
                    break
                else:
                    print("")
                    print(f"Please input value from {MIN_SKILL_VALUE} to {max_skill_value}")
            except ValueError:
                print("Wrong value, retry")
                continue
    
def show_stats(): 
    for stat in stats_list:
        print(f"""
So, your final stats are: {stat.name} {stat.amount_of_points_in}              
""")