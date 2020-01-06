'''
This module is a game without control structure. This doesn't include visuals.
'''

__Author__ = 'Harry Burge'
__Date__ = '5/1/2020'


# TODO: Remove useless comments once not needed no more

# Imports
from Box2D import *
from lib.objs.human import human
from utils import generalUtil


# Game
class Game:
    '''
    This class has every that is needed to have a game except for visuals
    and the control structure.
    '''

    def __init__(self):
        self.world = b2World(gravity=b2Vec2(0, 1),doSleep=True)
        self.timeStep = 1.0 / 60
        self.vel_iters, self.pos_iters = 6, 2

        self.dynamicObjects = []
        self.staticObjects = []


    def step(self):
        '''
        Runs one tick of pyhsics
        '''
        self.world.Step(timeStep=self.timeStep,
                        velocityIterations=self.vel_iters,
                        positionIterations=self.pos_iters)
        self.world.ClearForces()


    def create_dynamic_object(self, object, poi, angle): # Need to be able to add new hit boxes
        '''
        Creates a moveable object and ties together a object (e.g. human) to it

        params:-
            object : Object : As long as has .get_image()
            poi : (float, float) : In yards
            angle : float : Angle in degrees
        '''
        angle = generalUtil.degrees_to_rad(angle)
        temp = self.world.CreateDynamicBody(position=poi)
        temp.CreatePolygonFixture(box=(0.3,0.3), density=1, friction=0.3) # TODO: will need to change density and stuffs to human things
        temp.angle = angle

        self.dynamicObjects.append({"object":object, "b2object":temp})

    def create_static_object(self, poi, object=None, angle=0, rect=None): # Need to be able to add new hit boxes
        '''
        Creates a static object and ties together a object

        params:-
            object : Object : As long as has .get_image()
            poi : (float, float) : In yards
            angle : float : Angle in degrees
        '''
        angle = generalUtil.degrees_to_rad(angle)
        temp = self.world.CreateStaticBody(position=poi)

        if rect != None:
            temp.CreatePolygonFixture(box=rect, density=1, friction=2.0)

        temp.angle = angle

        self.staticObjects.append({"object":object, "b2object":temp})


    def get_visual_objects(self):
        '''
        Gets all objects with images that need to be drawn.

        outputs:-
            [{path=str, poi=[float, float], angle=float}, ...] :
                                        Used in conjunction with Visualliser.draw
                                        Angle in degrees
        '''
        temp = []
        for i in self.dynamicObjects:
            temp.append({"path":i["object"].get_image(),
                        "poi":[i["b2object"].position.x*30, i["b2object"].position.y*30],
                        "angle":generalUtil.rad_to_degrees(i["b2object"].angle)})

        for i in self.staticObjects:
            if i["object"] != None:
                if i["object"].get_image():
                    temp.append({"path":i["object"].get_image(),
                                "poi":[i["b2object"].position.x*30, i["b2object"].position.y*30],
                                "angle":generalUtil.rad_to_degrees(i["b2object"].angle)})
        return temp





if __name__ == '__main__':
    raise RuntimeError('This module can\'t be ran by itself. Please run AmericanFootballAI.py')
