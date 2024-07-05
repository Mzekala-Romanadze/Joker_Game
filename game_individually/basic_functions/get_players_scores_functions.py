"""
The program of Joker Game. This file includes the following functions:
            1. calculate_hand_scores()
            2. initial_set_scores_table()
            3. find_perfect_match_player()
            4. final_set_scores_table()
            5. create_game_scores_table()

"""

from game_individually.basic_functions.get_players_and_cards import BID_MATCH_POINTS


def calculate_hand_scores(players_calls, player_take_scores, perfect_match_scores):
    player_hand_scores = {}

    for player, call in players_calls.items():
        take = player_take_scores.get(player, 0)

        if call == take:
            score = BID_MATCH_POINTS[str(call)]
            if player not in perfect_match_scores:
                perfect_match_scores[player] = []
            perfect_match_scores[player].append(1)
        elif take == 0 and call > 0:
            score = BID_MATCH_POINTS["Fine"]
            if player not in perfect_match_scores:
                perfect_match_scores[player] = []
            perfect_match_scores[player].append(0)
        else:
            score = take * BID_MATCH_POINTS["No match"]
            if player not in perfect_match_scores:
                perfect_match_scores[player] = []
            perfect_match_scores[player].append(0)

        player_hand_scores[player] = score

    return player_hand_scores, perfect_match_scores


def initial_set_scores_table(set_scores):
    players_and_set_scores = {}

    for game_set in set_scores:
        for player, score in game_set.items():
            if player not in players_and_set_scores:
                players_and_set_scores[player] = []
            players_and_set_scores[player].append(score)

    return players_and_set_scores


def find_perfect_match_player(perfect_match):
    player_succeed_in_set = []

    for player, trick_win in perfect_match.items():
        if sum(trick_win) == 4:
            player_succeed_in_set.append(player)

    if not player_succeed_in_set:
        return None
    else:
        return player_succeed_in_set


def final_set_scores_table(players_and_set_scores, perfect_match):
    players_and_final_set_scores = {}
    other_player_scores = []

    for player, score in players_and_set_scores.items():
        if player not in perfect_match:
            scores_to_sum = []
            for i in score:
                if i > 0:
                    scores_to_sum.append(i)
            other_player_scores.append(sum(scores_to_sum))

    bonus_point = max(other_player_scores)
    final_set_scores = {}
    for player, scores in players_and_set_scores.items():
        if player not in perfect_match:
            final_set_scores[player] = sum(scores)
        if player in perfect_match:
            final_set_scores[player] = sum(scores) + bonus_point

    return final_set_scores


def create_game_scores_table(first_set_scores, second_set_scores, third_set_scores, fourth_set_scores):
    all_set_scores = [first_set_scores, second_set_scores, third_set_scores, fourth_set_scores]

    game_scores_table = {}

    for game_set in all_set_scores:
        for player, score in game_set.items():
            if player not in game_scores_table:
                game_scores_table[player] = score
            else:
                game_scores_table[player] += score

    players_scores = []
    for player, score in game_scores_table.items():
        players_scores.append(score)

    winner_score = max(players_scores)
    winner_player = []
    for player, score in game_scores_table.items():
        if winner_score == score:
            winner_player.append(player)

    return winner_player, winner_score, game_scores_table


def main():
    pass


if __name__ == '__main__':
    main()
