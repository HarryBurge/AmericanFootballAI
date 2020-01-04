'''
This module contains the class of human, used to represent a player on the field.
'''

__Author__ = 'Harry Burge'
__Date__ = '4/1/2020'


# Imports


# Class human
class Human():

    def __init__(self, height_arms_extended, poistion, succ_hurdle,
                succ_balance, fumble, make_fumble,
                stick_block, break_block, make_tackle,
                break_tackle, model_image, legs, arms, head):
        self.height_arms_extended = height_arms_extended
        self.poistion = poistion
        self.succ_hurdle = succ_hurdle
        self.succ_balance = succ_balance
        self.fumble = fumble
        self.make_fumble = make_fumble
        self.stick_block = stick_block
        self.break_block = break_block
        self.make_tackle = make_tackle
        self.break_tackle = break_tackle
        self.model_image = model_image
        self.legs = legs
        self.arms = arms
        self.head = head

        self.offBalance = False
