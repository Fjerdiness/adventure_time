from general import npcs
# from general import actions
# from general import stats


def main():
    npc = npcs.get_npc()
    print(npcs.player_attack_npc(npc))
    # actions.input_to_play()
    # stats.set_stats()
    # stats.show_stats()
    # while True:
    #     where_to = actions.what_to_do()
    #     actions.process_user_input(where_to)


if __name__ == "__main__":
    main()