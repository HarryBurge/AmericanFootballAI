'''
This is the control structure for a solo player game.
'''

__Author__ = 'Harry Burge'
__Date__ = '5/1/2020'


# Imports
from lib.objs.human import human
from lib.game_manager import game_manager
from lib.game_manager.visualliser import visualliser
from utils import generalUtil

# Examples
example_player = human.Human(height_arms_extended=1, poistion=1, succ_hurdle=1,
            succ_balance=1, fumble=1, make_fumble=1,
            stick_block=1, break_block=1, make_tackle=1,
            break_tackle=1, model_image='lib/game_manager/visualliser/imgs/redcircle.png', legs=1, arms=1, head=1)


# TODO: Need to add control structure for game and visuals also input for the user
# Main
def main():
    game = game_manager.Game()
    visuals = visualliser.Visualliser(win_size=(1620,1000), # Width, height
                                        win_name='AmericanFootballSolo')



    # TODO: remove this - testing
    # TODO: points are failing aswell think its due to angle
    #game.create_dynamic_object(example_player, (1.0,1.0), 0)
    game.create_dynamic_object(example_player, (1.0,0.0), -90) # TODO: found issue with angle not getting drawn correct only takes starting angle
    game.create_static_object(poi=(0,10), object=generalUtil.Line(), rect=(1, 0.6), angle=-45) #Width/x height/y # TODO: Rotates image in wrong direction to the actual image
    game.create_static_object(poi=(2,10), object=generalUtil.Line(), rect=(1, 0.6), angle=45)

    # TODO: Remove the testign code
    for i in range(0, 1000):
        game.step()
        temp = game.get_visual_objects()
        visuals.draw(temp, [0, 0]) # TODO: change camera to variable



if __name__ == '__main__':
    raise RuntimeError('This module can\'t be ran by itself. Please run AmericanFootballAI.py')
