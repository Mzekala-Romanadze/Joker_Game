"""
The program of Joker Game. This file includes the following functions:
            1. check_card()
            2. find_highest_suit_card()
            3. find_highest_rank_value_card()
            4. find_winner_card()

"""

from game_individually.basic_functions.get_players_and_cards import RANK_VALUES


def check_card(player_choice_card, cards):
    while player_choice_card not in cards:
        player_choice_card = input("You do not have this card. Choose another which you want to be led: ")


def find_highest_suit_card(cards, card_suit):
    player_suit_cards = [card for card in cards if card_suit in card]

    highest_card = None
    highest_rank_value = -1

    for card in player_suit_cards:
        rank = card.split(' of ')[0]
        rank_value = RANK_VALUES[rank]
        if rank_value > highest_rank_value:
            highest_rank_value = rank_value
            highest_card = card

    return highest_card


def find_highest_rank_value_card(table_cards, chosen_trump):
    highest_card = None
    highest_rank_value = -1

    for card in table_cards:
        rank, suit = card.split(' of ')
        if rank == "Joker":
            continue
        if suit == chosen_trump:
            rank_value = RANK_VALUES[rank] + 100
        else:
            rank_value = RANK_VALUES[rank]
        if rank_value > highest_rank_value:
            highest_rank_value = rank_value
            highest_card = card

    return highest_card


def find_winner_card(joker_case, trump_joker_case, chosen_trump, table_cards, joker_choice, take_suit):
    table_cards_suits = [card.split()[-1] for card in table_cards]

    if len(joker_case) == 1 and len(trump_joker_case) == 1:
        winner_card = trump_joker_case[0]
    elif len(joker_case) == 1 and len(trump_joker_case) > 1:
        winner_card = find_highest_suit_card(trump_joker_case, chosen_trump)
    elif len(joker_case) == 1:
        winner_card = joker_case[0]
    elif len(joker_case) == 2:
        winner_card = joker_case[1]
    elif joker_choice == "TAKE" and take_suit not in table_cards_suits:
        if chosen_trump in table_cards_suits:
            winner_card = find_highest_suit_card(table_cards, chosen_trump)
        else:
            winner_card = table_cards[0]
    elif joker_choice == "TAKE" and take_suit in table_cards_suits:
        if chosen_trump in table_cards_suits:
            winner_card = find_highest_suit_card(table_cards, chosen_trump)
        else:
            winner_card = find_highest_suit_card(table_cards, take_suit)
    else:
        winner_card = find_highest_rank_value_card(table_cards, chosen_trump)

    return winner_card


def main():
    pass


if __name__ == '__main__':
    main()
