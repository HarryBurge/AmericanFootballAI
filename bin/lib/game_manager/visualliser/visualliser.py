'''
This module visualises a game passed to it.
'''

__Author__ = 'Harry Burge'
__Date__ = '5/1/2020'


# Imports
import pygame
from Box2D import *
import os

# Colours
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


# visualliser
class Visualliser:
    '''
    This class controls visuals for one game for each instance of Visualliser.
    '''


    def __init__(self, win_size, win_name):
        '''
        params:-
            win_size : (int, int) : size of viewable area
            win_name : str : name of tge window that appers
        '''


        pygame.init()

        self.size = win_size
        self.screen = pygame.display.set_mode(win_size)

        pygame.display.set_caption(win_name)


    def draw(self, objects, camera_poi):
        # TODO: adjust the doc string for the object thats going to be passed
        '''
        Takes a bunch of objects in an array and then draws them depending on
        what they are. Key points: 10 pixel border around field,
        30 pixels = 1 yard.

        params:-
            objects : [] :
            camera_poi : [int, int] :

        outputs:-
            pygame window
        '''


        # Stops camera going out of view of field
        if camera_poi[1] > 3600 - self.size[1]:
            camera_poi[1] = 3600 - self.size[1] + 20
        elif camera_poi[1] < 0:
            camera_poi[1] = 0

        if camera_poi[0] > 1600 - self.size[0]:
            camera_poi[0] = 1600 - self.size[0] + 20
        elif camera_poi[0] < 0:
            camera_poi[0] = 0

        # Wipes screen and applies green background
        self.screen.fill(WHITE)
        pygame.draw.rect(self.screen,GREEN,
                            (10-camera_poi[0], 10-camera_poi[1], 1600, 3600))

        # Makes 5 yard lines
        for i in range(0,21):
            pygame.draw.rect(self.screen,WHITE,
                                (10-camera_poi[0], 307-camera_poi[1]+(i*150), 1600, 6))

        # End zone colours
        pygame.draw.rect(self.screen,BLUE,
                            (10-camera_poi[0], 10-camera_poi[1], 1600, 297))
        pygame.draw.rect(self.screen,RED,
                            (10-camera_poi[0], 3313-camera_poi[1], 1600, 297))

        # TODO: Draw objects

        pygame.display.flip()







if __name__ == '__main__':
    raise RuntimeError('This module can\'t be ran by itself. Please run AmericanFootballAI.py')
