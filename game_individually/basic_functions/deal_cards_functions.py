"""
The program of Joker Game. This file includes the following functions:
            1. deal_cards()
            2. choose_trump()
            3. print_cards()

"""

from game_individually.basic_functions.get_players_and_cards import create_and_shuffle_cards, TRUMP_SUITS


def deal_cards(players_order):
    deck = create_and_shuffle_cards()
    print(f"Player order: {players_order}: ")

    players_and_cards = {f"{player}": [] for player in players_order}
    first_player = players_order[0]
    three_cards_to_show = players_and_cards[first_player]
    chosen_trump = None

    for i in range(9):
        for player in players_and_cards:
            players_and_cards[player].append(deck.pop(0))
        if i == 2:
            print(f"{first_player}'s Cards: {three_cards_to_show}")
            chosen_trump = choose_trump(first_player)

    return players_and_cards, chosen_trump, players_order


def choose_trump(first_player):
    chosen_trump = input(f"{first_player} choose trump: HEART, DIAMOND, SPADE, CLUB or NONE ").upper()
    while chosen_trump not in TRUMP_SUITS:
        chosen_trump = input("Enter valid trump suit: HEART, DIAMOND, SPADE, CLUB or NONE").upper()
    return chosen_trump


def print_cards(players_and_cards, chosen_trump):
    print(f"The trump of the round is {chosen_trump}")
    for player, cards in players_and_cards.items():
        print(f"{player}'s cards: {cards}")


def main():
    pass


if __name__ == '__main__':
    main()
