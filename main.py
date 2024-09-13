import random


DIRECTIONS = {"n", "w", "s", "e"}
LOCATIONS = {"Forest", "Castle", "Dungeon", "House", "River", "Lake"}

def start():
    user_input = str(input("Hello. Do you wanna to play? y/n ")).lower()
    if user_input == "y":
        print("Nice, lets go!")
    else:
        print("As you wish")
        quit()

def where_to() -> str:
    while True:
        user_input = str(input("Where do you wanna go? n, w, s, e "))
        if user_input in DIRECTIONS:
            return user_input
        else:
            print("Wrong input. Retry.")
            continue

def location_info() -> int:
    location_index = random.randint(0, len(LOCATIONS))
    print(f"You`re in {LOCATIONS[location_index]}. You start to search for a sword of agammemnon")
    return location_index

def is_sword_here() -> bool | int:
    probability = random.randint(0, 100)
    if probability > 50:
        print(f"You have found sword of agammemnon!")
        return True
    elif 1 < probability < 50:
        print(f"No luck, keep searching at next location")
        return False
    return probability







def main():
    start()
    where_to()
main()