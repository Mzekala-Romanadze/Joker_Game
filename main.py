"""
The program of Joker Game. Run the following code to play Joker.

This file includes the following functions:
            1. choose_game_type() => Individually or In pairs
            2. play_game() => playing 4 sets, 16 hands in total (16 * 9 tricks)

Firstly, the user should choose game type: Individually or In pairs

"""

from game_in_pairs.play_in_pairs import play_game_in_pairs
from game_individually.play_individually import play_game_individually


def choose_game_type():
    user_choice = input("Choose: Play Individually (I) or In Pairs (P)? ").upper()
    while user_choice != "I" and user_choice != "P":
        user_choice = input("Enter valid Symbol: Individually (I) or In Pairs (P) ").upper()
    if user_choice == "I":
        return "Individually"
    if user_choice == "P":
        return "In Pairs"


def play_game():
    game_type = choose_game_type()

    if game_type == "Individually":
        print("Hello Players, you play Individually ")
        print("Be mindful of every decision. Success is in the details.")

        winner_player, winner_score, game_scores_table = play_game_individually()

        if len(winner_player) > 1:
            print(f"Game is over! There are {len(winner_player)} winners: {winner_player} Congratulations! "
                  f"You won the game by {sum(winner_score)} points. ")
        else:
            print(f"Game is over! {winner_player} Congratulations! You won the game by {sum(winner_score)} points. ")

        print(f"The players and scores: {game_scores_table}")

    if game_type == "In Pairs":
        print("Hello Players, you play In Pairs ")
        print("Be mindful of every decision. Success is in the details and teamwork.")
        # winner_team, winner_score, game_scores_table = play_game_in_pairs()
        # if len(winner_team) == 1:
        #     print(f"Game is over! The winner team is {winner_team}! Congratulations! "
        #           f"You won the game by {winner_score} points. ")
        # else:
        #     print(f"Game is over! It is draw. The final score of both teams is {winner_score} points. ")
        #
        # print(f"The players and scores: {game_scores_table}")


def main():
    play_game()


if __name__ == '__main__':
    main()
