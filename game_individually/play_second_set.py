"""
The program of Joker Game. This file includes the following functions:
            1. play_second_set() => playing 4 hands (4 * 9 tricks)

"""
from game_individually.basic_functions.get_players_scores_functions import (initial_set_scores_table,
                                                                            find_perfect_match_player,
                                                                            final_set_scores_table)
from game_individually.basic_functions.play_one_set import play_one_set


def play_second_set(original_players_order, perfect_match_scores):
    second_set_scores, perfect_match_player_scores = play_one_set(original_players_order, perfect_match_scores)
    players_and_second_set_scores = initial_set_scores_table(second_set_scores)
    perfect_match = find_perfect_match_player(perfect_match_player_scores)

    if perfect_match is None:
        return players_and_second_set_scores
    else:
        second_set_scores = final_set_scores_table(players_and_second_set_scores, perfect_match)
        return second_set_scores


def main():
    pass


if __name__ == '__main__':
    main()
