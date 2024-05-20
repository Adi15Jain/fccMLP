# RPS_game.py

import random

def play(player1, player2, num_games, verbose=False):
    results = {"player": 0, "opponent": 0, "tie": 0}
    player1_history = []
    player2_history = []

    for _ in range(num_games):
        player1_move = player1(player2_history[-1] if player2_history else '')
        player2_move = player2(player1_history[-1] if player1_history else '')

        player1_history.append(player1_move)
        player2_history.append(player2_move)

        if player1_move == player2_move:
            results["tie"] += 1
            winner = "Tie"
        elif (player1_move == "R" and player2_move == "S") or (player1_move == "P" and player2_move == "R") or (player1_move == "S" and player2_move == "P"):
            results["player"] += 1
            winner = "Player 1"
        else:
            results["opponent"] += 1
            winner = "Player 2"

        if verbose:
            print(f"Player 1: {player1_move}, Player 2: {player2_move} -- {winner}")

    return results

def quincy(prev_play, opponent_history=[]):
    quincy_seq = ["R", "P", "S", "R", "P", "S"]
    return quincy_seq[len(opponent_history) % len(quincy_seq)]

def abbey(prev_play, opponent_history=[]):
    if not prev_play:
        opponent_history.clear()
    opponent_history.append(prev_play)
    counter_moves = {'R': 'P', 'P': 'S', 'S': 'R'}
    if len(opponent_history) >= 2:
        last_move = opponent_history[-1]
        second_last_move = opponent_history[-2]
        if last_move == second_last_move:
            return counter_moves[last_move]
    return counter_moves[random.choice(["R", "P", "S"])]

def kris(prev_play, opponent_history=[]):
    if not prev_play:
        opponent_history.clear()
    opponent_history.append(prev_play)
    if len(opponent_history) < 3:
        return random.choice(["R", "P", "S"])
    if opponent_history[-1] == opponent_history[-2] == opponent_history[-3]:
        return {'R': 'P', 'P': 'S', 'S': 'R'}[opponent_history[-1]]
    return random.choice(["R", "P", "S"])

def mrugesh(prev_play, opponent_history=[]):
    if not prev_play:
        opponent_history.clear()
    opponent_history.append(prev_play)
    if len(opponent_history) < 3:
        return random.choice(["R", "P", "S"])
    patterns = {}
    for i in range(len(opponent_history) - 1):
        pat = tuple(opponent_history[i:i+2])
        if pat in patterns:
            patterns[pat] += 1
        else:
            patterns[pat] = 1
    last_two = tuple(opponent_history[-2:])
    predict = max(patterns, key=patterns.get)[-1] if last_two in patterns else random.choice(["R", "P", "S"])
    return {'R': 'P', 'P': 'S', 'S': 'R'}[predict]
