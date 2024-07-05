"""
The program of Joker Game. This file includes the following functions:
            1. play_one_set() => playing 4 hands (4 * 9 tricks)

"""

from game_individually.basic_functions.play_one_hand import play_one_hand


def play_one_set(original_players_order, perfect_match_scores):
    hand_number = 0
    temp_players_order = None
    one_set_scores = []
    for _ in range(4):
        temp_players_order, one_set_scores, perfect_match_scores = play_one_hand(one_set_scores, hand_number,
                                                                                 temp_players_order,
                                                                                 perfect_match_scores,
                                                                                 original_players_order)
        hand_number += 1

    return one_set_scores, perfect_match_scores


def main():
    pass


if __name__ == '__main__':
    main()
