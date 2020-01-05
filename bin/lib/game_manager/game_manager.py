'''
This module is a game without control structure. This doesn't include visuals.
'''

__Author__ = 'Harry Burge'
__Date__ = '5/1/2020'


# TODO: Remove useless comments once not needed no more

# Imports
from Box2D import *


# Game
class Game:
    '''
    This class has every that is needed to have a game except for visuals
    and the control structure.
    '''

    def __init__(self):
        self.world = b2World(gravity=b2Vec2(0, 0),doSleep=True)
        self.timeStep = 1.0 / 60
        self.vel_iters, self.pos_iters = 6, 2
        # self.groundBody = self.world.CreateStaticBody(
        #     position=(0,-10),
        #     shapes=b2PolygonShape(box=(50,10)),
        #     )
        # self.body = self.world.CreateDynamicBody(position=(0,300))
        # self.box = self.body.CreatePolygonFixture(box=(1,1), density=1, friction=0.3)


    def step(self):
        # Instruct the world to perform a single step of simulation. It is
        # generally best to keep the time step and iterations fixed.
        self.world.Step(timeStep=self.timeStep,
                        velocityIterations=self.vel_iters,
                        positionIterations=self.pos_iters)

        # Clear applied body forces. We didn't apply any forces, but you
        # should know about this function.
        self.world.ClearForces()

        #return [self.body.position, self.body.angle]




if __name__ == '__main__':
    raise RuntimeError('This module can\'t be ran by itself. Please run AmericanFootballAI.py')
