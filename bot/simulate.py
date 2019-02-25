from api.game import start_poker, setup_config

from bot.callbot import CallBot
from bot.pokerBot import pokerBot
from bot.human_player import ConsolePlayer
from bot.fish_player import FishPlayer
from utils.players import BasePokerPlayer
from bot.honest_player import HonestPlayer

#-----------------------
import numpy as np

if __name__ == '__main__':
    #blogger_bot = DataBloggerBot()
    poker_bot = pokerBot()
    call_bot = CallBot()
    # initial stock 100 - chips
    #fish_player = FishPlayer()
   # honest_player = HonestPlayer()
    console_player = ConsolePlayer()

    stack_log = []
    for round in range(100):
        p1, p2 = poker_bot, ConsolePlayer()

        config = setup_config(max_round=1, initial_stack=100, small_blind_amount=5)
        config.register_player(name="PokerBot", algorithm=p1)
        config.register_player(name="Human", algorithm=p2)
        game_result = start_poker(config, verbose=1)

        stack_log.append([player['stack'] for player in game_result['players'] if player['uuid'] == poker_bot.uuid])
       # print('Avg. stack:', '%d' % (int(np.mean(stack_log))))

        for player_info in game_result["players"]:
            print(player_info)

