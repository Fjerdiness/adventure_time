import random
import sys
from general import actions, locations, stats, enemies



def start():
    user_input = str(input("Hello. Do you wanna to play? y/n ")).lower().strip()
    if user_input == "y":
        print("Nice, lets go!")
    elif user_input == "n":
        print("As you wish")
        sys.exit()
    else:
        print("wrong input, retry")
        start()
    stats.set_stats()
    stats.show_stats()

def main():
    start()
    actions.what_to_do()
    while True:
        position = locations.whats_around_you()
        locations.is_should_search(position)


if __name__ == "__main__":
    main()