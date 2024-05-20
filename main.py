# main.py

from RPS_game import play, quincy, abbey, kris, mrugesh
from RPS import player

if __name__ == "__main__":
    bots = [quincy, abbey, kris, mrugesh]
    bot_names = ["quincy", "abbey", "kris", "mrugesh"]
    
    for bot, name in zip(bots, bot_names):
        print(f"Testing against {name}")
        result = play(player, bot, 1000)
        print(f"Win rate against {name}: {result['player'] / 1000:.2%}")
