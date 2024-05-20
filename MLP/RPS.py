# RPS.py

import random

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)
    
    if not opponent_history:
        return random.choice(["R", "P", "S"])
    
    def most_common_counter(history):
        if not history:
            return random.choice(["R", "P", "S"])
        counts = {"R": 0, "P": 0, "S": 0}
        for move in history:
            counts[move] += 1
        most_common_move = max(counts, key=counts.get)
        if most_common_move == "R":
            return "P"
        elif most_common_move == "P":
            return "S"
        elif most_common_move == "S":
            return "R"
    
    def frequency_analysis(history):
        if len(history) < 3:
            return random.choice(["R", "P", "S"])
        last_three = history[-3:]
        if last_three == ["R", "R", "R"]:
            return "P"
        elif last_three == ["P", "P", "P"]:
            return "S"
        elif last_three == ["S", "S", "S"]:
            return "R"
        else:
            return most_common_counter(history)
    
    def pattern_detection(history):
        if len(history) < 5:
            return random.choice(["R", "P", "S"])
        for length in range(4, 1, -1):
            pattern = history[-length:]
            for i in range(len(history) - length * 2):
                if history[i:i+length] == pattern:
                    next_move_index = i + length
                    if next_move_index < len(history):
                        predicted_move = history[next_move_index]
                        if predicted_move == "R":
                            return "P"
                        elif predicted_move == "P":
                            return "S"
                        elif predicted_move == "S":
                            return "R"
        return most_common_counter(history)
    
    if len(opponent_history) < 5:
        return most_common_counter(opponent_history)
    elif len(opponent_history) < 10:
        return frequency_analysis(opponent_history)
    else:
        return pattern_detection(opponent_history)
