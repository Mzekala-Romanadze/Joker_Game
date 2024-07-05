"""
The program of Joker Game. This file includes the following functions:
            1. player_calls()
            2. check_calls()

"""

from game_individually.basic_functions.get_players_and_cards import TOTAL_ROUND_CALL
from game_individually.basic_functions.deal_cards_functions import deal_cards
from game_individually.basic_functions.rearrange_players_order import rearrange_players_order_for_next_hand


def player_calls(hand_number, temp_players_order, original_players_order):
    if hand_number == 0:
        players_and_cards, chosen_trump, players_order = deal_cards(original_players_order)
        temp_players_order = players_order
    else:
        temp_players_order = rearrange_players_order_for_next_hand(temp_players_order)
        players_and_cards, chosen_trump, players_order = deal_cards(temp_players_order)
        temp_players_order = players_order

    players_calls = {}

    card_dealer = temp_players_order[-1]
    total_round_score = 0

    for player, cards in players_and_cards.items():
        print(f"{player}'s cards: {cards} ")
        if player == card_dealer:
            unavailable_score = TOTAL_ROUND_CALL - total_round_score
            player_call = check_calls(player)
            players_calls[player] = player_call
            while players_calls[player] == unavailable_score:
                player_call = int(input(f"{player}, {unavailable_score} is unavailable. choose another "
                                        f"call: "))
                player_call = check_calls(player, player_call)
                players_calls[player] = player_call
            total_round_score += players_calls[player]
            break
        player_call = check_calls(player)
        players_calls[player] = player_call
        total_round_score += players_calls[player]

    return temp_players_order, players_and_cards, players_calls, total_round_score, chosen_trump


def check_calls(player, player_call=None):
    if player_call is None:
        player_call = int(input(f"{player} what's your call? (if pass enter '0') "))

    while player_call < 0 or player_call > 9:
        player_call = int(input(f"{player} your call must be in range 0-9 "))
    return player_call


def main():
    pass


if __name__ == '__main__':
    main()
