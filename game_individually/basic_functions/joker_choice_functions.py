"""
The program of Joker Game. This file includes the following functions:
            1. joker_is_first()
            2. joker_is_not_first()

"""

from game_individually.basic_functions.get_players_and_cards import SUITS


def joker_is_first(player_choice_card, joker_case, want_suit, take_suit):
    player_action = input("Choose: Want Highest ('WANT') or Don't Want ('TAKE')? ").upper()
    while player_action != "WANT" and player_action != "TAKE":
        player_action = input("Wrong action. Choose: Want Highest ('WANT') or Don't Want ('TAKE')? ").upper()
    joker_choice = player_action

    if joker_choice == "WANT":
        want_suit = input("Which suit of cards do you want with highest ranks? ").upper()
        while want_suit not in SUITS:
            want_suit = input("Enter valid suit. Which suit of cards do you want with highest ranks? ").upper()
        joker_case.append(player_choice_card)

    if joker_choice == "TAKE":
        take_suit = input("Which suit of card do you want to take? ").upper()
        while take_suit not in SUITS:
            take_suit = input("Enter valid suit. Which suit of card do you want to take? ").upper()

    return joker_choice, want_suit, take_suit


def joker_is_not_first(player_choice_card, joker_case):
    player_joker_choice = input("Do you want to take cards by Joker or not? (YES/NO) ").upper()
    while player_joker_choice != "YES" and player_joker_choice != "NO":
        player_joker_choice = input("Enter YES or NO. "
                                    "Do you want to take cards by Joker or not? (YES/NO) ").upper()
    if player_joker_choice == "YES":
        joker_case.append(player_choice_card)


def main():
    pass


if __name__ == '__main__':
    main()
