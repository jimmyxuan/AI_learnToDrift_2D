from pyglet.gl import *
from pyglet.window import key
from pyglet.window import FPSDisplay
import math
from CarSprite import *
from Line import *
from Track import *
from Grid import *
WINDOWWIDTH=1280
WINDOWHEIGHT=720 
class MyWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(MyWindow,self).__init__(*args, **kwargs)
        #this clear thing affect the background color
        #comment it out to get a black background
        glClearColor(1,1.0,1.0,1)
        self.fps_display = FPSDisplay(self)
        self.car = CarSprite()
        self.key_handler = key.KeyStateHandler()
        self.testTrack= Track([40,60,1200,600],[240,260,800,200])
        self.testGrid = Grid(40,60,1200,600,50)

    def update(self, dt):
        if self.key_handler[key.LEFT]:
            self.car.turnLeft(dt)
        
        if self.key_handler[key.RIGHT]:
            self.car.turnRight(dt)

        if self.key_handler[key.UP]:
            self.car.goStraight(dt)

        if self.key_handler[key.DOWN]:
            self.car.goReverse(dt)
        self.car.runningCar(dt)
        self.car.reset()
        


    def update(self, dt):
        if self.key_handler[key.LEFT]:
            self.car.turnLeft(dt)
        
        if self.key_handler[key.RIGHT]:
            self.car.turnRight(dt)

        if self.key_handler[key.UP]:
            self.car.goStraight(dt)

        if self.key_handler[key.DOWN]:
            self.car.goReverse(dt)
        self.car.runningCar(dt)

if __name__ == "__main__":
    window = MyWindow(WINDOWWIDTH,WINDOWHEIGHT, "DRIFT AI", resizable=True, vsync =True)
    window.push_handlers(window.key_handler)
    pyglet.clock.schedule_interval(window.update,1/60.0)
    pyglet.app.run()
