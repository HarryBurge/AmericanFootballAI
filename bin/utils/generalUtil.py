'''
This is a list of general funcs that might be helpful and used throughout the program
'''

__Author__ = 'Harry Burge'
__Date__ = '4/1/2020'


# Imports
import math

# Util Contents

# Searchs multiple items in a list
def search_items_to_list(items, target_list):
    for i in items:
        return True if i in target_list else None
    return False


# Converts radians to degress
def rad_to_degrees(rad):
    return rad*(math.pi/180)

# Converts degress to radians
def degrees_to_rad(deg):
    return deg*(180/math.pi)

# Class for denug lines
class Line:

    def __init__(self):
        self.img = 'lib/game_manager/visualliser/imgs/BlackLine.png'

    def get_image(self):
        return self.img


if __name__ == '__main__':
    raise RuntimeError('This module can\'t be ran by itself. Please run AmericanFootballAI.py')
