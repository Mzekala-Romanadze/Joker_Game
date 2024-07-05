"""
The program of Joker Game. This file includes the following functions:
            1. joker_is_want()
            2. joker_is_take()

"""

from game_individually.basic_functions.check_and_find_card_functions import check_card, find_highest_suit_card


def joker_is_want(player_choice_card, cards, player_cards_suits, joker_case, want_suit, chosen_trump, trump_joker_case):
    while want_suit in player_cards_suits:
        if player_choice_card.split()[0] == "Joker":
            player_joker_choice = input("Do you want to take cards by Joker or not? (YES/NO) ").upper()
            while player_joker_choice != "YES" and player_joker_choice != "NO":
                player_joker_choice = input("Enter YES or NO. Do you want to take "
                                            "cards by Joker or not? (YES/NO) ").upper()
            if player_joker_choice == "YES":
                joker_case.append(player_choice_card)
            break

        highest_card = find_highest_suit_card(cards, want_suit)
        if player_choice_card.split()[-1] != want_suit:
            player_choice_card = input("You have to lead card with wanted suit. "
                                       "Which card do you want to be led? ")
            check_card(player_choice_card, cards)
        if player_choice_card.split()[-1] == want_suit:
            if player_choice_card != highest_card:
                player_choice_card = input("You have to lead highest card with wanted suit. ")
            if player_choice_card == highest_card:
                break

    while want_suit not in player_cards_suits:
        if player_choice_card.split()[0] == "Joker":
            player_joker_choice = input("Do you want to take cards by Joker or not? (YES/NO) ").upper()
            while player_joker_choice != "YES" and player_joker_choice != "NO":
                player_joker_choice = input("Enter YES or NO. Do you want to take "
                                            "cards by Joker or not? (YES/NO) ").upper()
            if player_joker_choice == "YES":
                joker_case.append(player_choice_card)
            break

        if chosen_trump in player_cards_suits and player_choice_card.split()[-1] != chosen_trump:
            player_choice_card = input("You have to lead trump suit card. Which card do you want to be led? ")
            check_card(player_choice_card, cards)

        if chosen_trump in player_cards_suits and player_choice_card.split()[-1] == chosen_trump:
            trump_joker_case.append(player_choice_card)
            break

        if chosen_trump not in player_cards_suits:
            break


def joker_is_take(player_choice_card, cards, player_cards_suits, joker_case, take_suit, chosen_trump):
    while take_suit in player_cards_suits:
        if player_choice_card.split()[0] == "Joker":
            player_joker_choice = input("Do you want to take cards by Joker or not? (YES/NO) ").upper()
            while player_joker_choice != "YES" and player_joker_choice != "NO":
                player_joker_choice = input("Enter YES or NO. Do you want to take "
                                            "cards by Joker or not? (YES/NO) ").upper()
            if player_joker_choice == "YES":
                joker_case.append(player_choice_card)
            break

        highest_card = find_highest_suit_card(cards, take_suit)
        if player_choice_card.split()[-1] != take_suit:
            player_choice_card = input("You have to lead card with take suit. Which card do you want to be led? ")
            check_card(player_choice_card, cards)
        if player_choice_card.split()[-1] == take_suit:
            if player_choice_card != highest_card:
                player_choice_card = input("You have to lead highest card with take suit. ")
            if player_choice_card == highest_card:
                break

    while take_suit not in player_cards_suits:
        if player_choice_card.split()[0] == "Joker":
            player_joker_choice = input("Do you want to take cards by Joker or not? (YES/NO) ").upper()
            while player_joker_choice != "YES" and player_joker_choice != "NO":
                player_joker_choice = input("Enter YES or NO. Do you want to take "
                                            "cards by Joker or not? (YES/NO) ").upper()
            if player_joker_choice == "YES":
                joker_case.append(player_choice_card)
            break

        if chosen_trump in player_cards_suits and player_choice_card.split()[-1] != chosen_trump:
            player_choice_card = input("You have to lead trump suit card. Which card do you want to be led? ")
            check_card(player_choice_card, cards)

        if chosen_trump in player_cards_suits and player_choice_card.split()[-1] == chosen_trump:
            break

        if chosen_trump not in player_cards_suits:
            break


def main():
    pass


if __name__ == '__main__':
    main()
