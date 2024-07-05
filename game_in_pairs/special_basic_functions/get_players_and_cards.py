"""
The program of Joker Game. This file includes the following functions:
            1. Constant variables
            2. get_player_names()
            3. get_players_order()
            4. create_and_shuffle_cards()

"""

import random

NUMBER_OF_PLAYERS = 4
TOTAL_ROUND_CALL = 9
DECK_OF_CARDS = {
    "SPADE": ["Ace of SPADE", "King of SPADE", "Queen of SPADE", "Jack of SPADE", "10 of SPADE",
              "9 of SPADE", "8 of SPADE", "7 of SPADE", "Joker of Spades"],
    "CLUB": ["Ace of CLUB", "King of CLUB", "Queen of CLUB", "Jack of CLUB", "10 of CLUB",
             "9 of CLUB", "8 of CLUB", "7 of CLUB", "Joker of Clubs"],
    "HEART": ["Ace of HEART", "King of HEART", "Queen of HEART", "Jack of HEART", "10 of HEART",
              "9 of HEART", "8 of HEART", "7 of HEART", "6 of HEART"],
    "DIAMOND": ["Ace of DIAMOND", "King of DIAMOND", "Queen of DIAMOND", "Jack of DIAMOND", "10 of DIAMOND",
                "9 of DIAMOND", "8 of DIAMOND", "7 of DIAMOND", "6 of DIAMOND"]
}
SUITS = DECK_OF_CARDS.keys()
RANK_VALUES = {"Joker": 20, "Ace": 14, "King": 13, "Queen": 12, "Jack": 11, "10": 10, "9": 9, "8": 8, "7": 7, "6": 6}
TRUMP_SUITS = ["HEART", "DIAMOND", "SPADE", "CLUB", "NONE"]
BID_MATCH_POINTS = {"0": 50, "1": 100, "2": 150, "3": 200, "4": 250, "5": 300, "6": 350, "7": 400, "8": 450, "9": 900,
                    "No match": 10, "Fine": -500}


def get_player_names() -> list:
    players = []
    for i in range(1, NUMBER_OF_PLAYERS + 1):
        player_name = input(f"Enter name of Player {i}: ").capitalize()
        while player_name in players:
            player_name = input(f"This name is already taken. Enter another name for Player {i}: ").capitalize()
            if player_name in players:
                continue
        while not player_name:
            player_name = input(f"Please enter name for Player {i}: ").capitalize()
        players.append(player_name)
    return players


def get_players_order(hand_number):
    players = get_player_names()
    first_card_dealer = random.choice(players)
    temp_list_1 = []
    temp_list_2 = []
    for player in players:
        if player == first_card_dealer:
            index = players.index(player)
            temp_list_1.append(players[index + 1:])
            temp_list_2.append(players[:index + 1])

    combine_lists = temp_list_1 + temp_list_2
    if hand_number == 0:
        players_order = [player for sublist in combine_lists for player in sublist]
        return players_order


def create_and_shuffle_cards():
    deck_of_cards = []
    for suit in SUITS:
        deck_of_cards += DECK_OF_CARDS[suit]
    random.shuffle(deck_of_cards)

    return deck_of_cards


def main():
    pass


if __name__ == '__main__':
    main()
