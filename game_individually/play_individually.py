"""
The program of Joker Game (Individually). This file includes the following function:
                1. play_game_individually() => playing 4 sets, 16 hands in total (16 * 9 tricks)

"""


from game_individually.basic_functions.get_players_and_cards import get_players_order
from game_individually.basic_functions.get_players_scores_functions import create_game_scores_table
from game_individually.play_first_set import play_first_set
from game_individually.play_second_set import play_second_set
from game_individually.play_third_set import play_third_set
from game_individually.play_fourth_set import play_fourth_set


def play_game_individually():
    original_players_order = get_players_order(hand_number=0)

    first_set_scores = play_first_set(original_players_order, perfect_match_scores={f"{player}": [] for player in
                                                                                    original_players_order})
    second_set_scores = play_second_set(original_players_order, perfect_match_scores={f"{player}": [] for player in
                                                                                      original_players_order})
    third_set_scores = play_third_set(original_players_order, perfect_match_scores={f"{player}": [] for player in
                                                                                    original_players_order})
    fourth_set_scores = play_fourth_set(original_players_order, perfect_match_scores={f"{player}": [] for player in
                                                                                      original_players_order})

    winner_player, winner_score, game_scores_table = create_game_scores_table(first_set_scores, second_set_scores,
                                                                              third_set_scores, fourth_set_scores)

    return winner_player, winner_score, game_scores_table


def main():
    pass


if __name__ == '__main__':
    main()
