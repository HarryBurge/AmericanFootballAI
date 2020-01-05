'''
This is the control structure for a solo player game.
'''

__Author__ = 'Harry Burge'
__Date__ = '5/1/2020'


# Imports
from lib.objs.human import human
from lib.game_manager import game_manager
from lib.game_manager.visualliser import visualliser


# TODO: Need to add control structure for game and visuals also input for the user
# Main
def main():
    game = game_manager.Game()
    visuals = visualliser.Visualliser(win_size=(1620,1000), # Width, height
                                        win_name='AmericanFootballSolo')

    # TODO: Remove the testign code
    for i in range(0, 10000):
        visuals.draw(game.step(), [i//2,i])


if __name__ == '__main__':
    raise RuntimeError('This module can\'t be ran by itself. Please run AmericanFootballAI.py')
