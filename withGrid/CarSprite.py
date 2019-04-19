from pyglet.gl import *
from pyglet.window import key
from pyglet.window import FPSDisplay
import math
from Line import *
WINDOWWIDTH=1280
WINDOWHEIGHT=720 
class CarSprite():
    def __init__(self):
        self.carSprite_image = pyglet.image.load('car_sprite5050.png')
        self.carSprite_image.anchor_x = 25
        self.carSprite_image.anchor_y = 25
        self.carSprite= pyglet.sprite.Sprite(self.carSprite_image, 40 +25, 60+25)
        self.x = self.carSprite.x
        self.y = self.carSprite.y
        self.theta = self.carSprite.rotation
        self.speed = 50.0
        self.rotation_speed = 90.0
        self.deltaX = 0.0
        self.deltaY = 0.0
        self.width = self.carSprite.width
        self.height = self.carSprite.height
        self.touchAlreadyP1=[False,False,False,False,False]
        self.touchAlreadyP2=[False,False,False,False,False]
        self.touchAlreadyP3=[False,False,False]
        self.touchAlreadyP4=[False,False,False]
    def draw(self):
        self.carSprite.draw()
        Line(self.getX()-25,self.getY()-25,self.getX()+25,self.getY()-25,[0,0,0],1).draw()
        Line(self.getX()-25,self.getY()+25,self.getX()+25,self.getY()+25,[0,0,0],1).draw()

        Line(self.getX()-25,self.getY()-25,self.getX()-25,self.getY()+25,[0,0,0],1).draw()
        Line(self.getX()+25,self.getY()-25,self.getX()+25,self.getY()+25,[0,0,0],1).draw()
        
        #checkpointP11
        Line(240,60,240,260,[0,0,0],1).draw()
        #checkpointP12
        Line(290,60,290,260,[0,0,0],1).draw()
        #checkpointP13
        Line(490,60,490,260,[0,0,0],1).draw()
        #checkpointP14
        Line(690,60,690,260,[0,0,0],1).draw()
        #checkpointP15
        Line(890,60,890,260,[0,0,0],1).draw()

        #checkpointP21
        Line(240,460,240,660,[0,0,0],1).draw()
        #checkpointP22
        Line(290,460,290,660,[0,0,0],1).draw()
        #checkpointP23
        Line(490,460,490,660,[0,0,0],1).draw()
        #checkpointP24
        Line(690,460,690,660,[0,0,0],1).draw()
        #checkpointP25
        Line(890,460,890,660,[0,0,0],1).draw()

        #checkpointP31
        Line(1040,260,1240,260,[0,0,0],1).draw()
        #checkpointP32
        Line(1040,360,1240,360,[0,0,0],1).draw()
        #checkpointP33
        Line(1040,460,1240,460,[0,0,0],1).draw()

        #checkpointP41
        Line(40,260,240,260,[0,0,0],1).draw()
        #checkpointP42
        Line(40,360,240,360,[0,0,0],1).draw()
        #checkpointP43
        Line(40,460,240,460,[0,0,0],1).draw()


    
    def getX(self):
        self.x = self.carSprite.x
        return self.x
    def getY(self):
        self.y = self.carSprite.y
        return self.y
    def getTheta(self):
        self.theta = self.carSprite.rotation
        return self.theta

    def getDeltaX(self):
        return self.deltaX
    def getDeltaY(self):
        return self.deltaY


    def updateX(self,value):
        value += self.getX()
        self.carSprite.update(x=value)
    def updateY(self,value):
        value += self.getY()
        self.carSprite.update(y=value)
    def updateTheta(self,degree):  
        degree += self.getTheta()
        self.carSprite.update(rotation=degree)
    def updateDeltaX(self, value):
        self.deltaX = value
    def updateDeltaY(self, value):
        self.deltaY = value

    def turnLeft(self):
        self.updateTheta(-self.rotation_speed)
        return self.goStraight()

    def turnRight(self):
        self.updateTheta(self.rotation_speed)
        return self.goStraight()
    def goStraight(self):
        value = self.getX() + self.speed
        thetaRadian = -math.radians(self.getTheta())
        deltaX = int(math.cos(thetaRadian) * self.speed) 
        deltaY = int(math.sin(thetaRadian) * self.speed) 
        if (((self.getX() + deltaX) <= 1240) and ((self.getX() + deltaX) >= 40)) and (((self.getY() + deltaY) <= 660) and ((self.getY() + deltaY) >= 60)):
            if ((self.getX() >=40 and self.getX() <= 240) and (self.getY() >=260) and self.getY()<=460) and (self.getX() + deltaX >240):
                return 240
            elif ((self.getX() >=1040 and self.getX() <= 1240) and (self.getY() >=260) and self.getY()<=460) and (self.getX() + deltaX <1040):
                return 1040
            elif ((self.getX() >=240 and self.getX() < 1040) and (self.getY() >=60) and self.getY()<=260) and (self.getY() + deltaY >260):
                return 260
            elif ((self.getX() >=240 and self.getX() < 1040) and (self.getY() >=460) and self.getY()<=660) and (self.getY() + deltaY <460):
                return 460
            else:
                self.updateX(deltaX)
                self.updateY(deltaY)
                return None
        else: 
            if (self.getX() + deltaX) > 1240:
                return 1240
            elif (self.getX() + deltaX) < 40:
                return 40
            elif (self.getY() + deltaY) > 660 :
                return 660
            elif (self.getY() + deltaY) <60:
                return 60
    
    
    def goReverse(self):
        value = self.getX() - self.speed
        thetaRadian = -math.radians(self.getTheta())
        deltaX = int(math.cos(thetaRadian) * self.speed )
        deltaY = int(math.sin(thetaRadian) * self.speed)
        if (((self.getX() - deltaX) <= 1240) and ((self.getX() - deltaX) >= 40)) and (((self.getY() - deltaY) <= 660) and ((self.getY() - deltaY) >= 60)):
            if ((self.getX() >=40 and self.getX() <= 240) and (self.getY() >=260) and self.getY()<=460) and (self.getX() - deltaX >240):
                return 240
            elif ((self.getX() >=1040 and self.getX() <= 1240) and (self.getY() >=260) and self.getY()<=460) and (self.getX() - deltaX <1040):
                return 1040
            elif ((self.getX() >=240 and self.getX() < 1040) and (self.getY() >=60) and self.getY()<=260) and (self.getY() - deltaY >260):
                return 260
            elif ((self.getX() >=240 and self.getX() < 1040) and (self.getY() >=460) and self.getY()<=660) and (self.getY() - deltaY <460):
                return 460
            else:
                self.updateX(-deltaX)
                self.updateY(-deltaY)
                return None
        else: 
            if (self.getX() - deltaX) > 1240:
                return 1240
            elif (self.getX() - deltaX) < 40:
                return 40
            elif (self.getY() - deltaY) > 660 :
                return 660
            elif (self.getY() - deltaY) <60:
                return 60
    
    def checkPoint(self):
        value = self.getX() - self.speed
        thetaRadian = -math.radians(self.getTheta())
        deltaX = int(math.cos(thetaRadian) * self.speed) 
        deltaY = int(math.sin(thetaRadian) * self.speed)
        
        #checkP1
        if (self.getX()>=40 and self.getX()<=1240) and (self.getY() >=60 and self.getY()<=260) and (self.getX() + deltaX >290) and not self.touchAlreadyP1[0]:
            print("hit" + str(self.getX() + deltaX-25))
            self.touchAlreadyP1[0] = True
        for i in range(4):
            if (self.getX()>=40 and self.getX()<=1240) and (self.getY() >=60 and self.getY()<=260) and (self.getX() + deltaX >340 + 200*i) and not self.touchAlreadyP1[i+1]:
                print("hit" + str(self.getX() + deltaX-25))
                self.touchAlreadyP1[i+1] = True

        #checkP2
        for i in range(4):
            if (self.getX()>=40 and self.getX()<=1240) and (self.getY() >=460 and self.getY()<=660) and (self.getX() + deltaX <850 - 200*i) and not self.touchAlreadyP2[4-i]:
                print("hit" + str(self.getX() + deltaX-25+100))
                self.touchAlreadyP2[4-i] = True
        if (self.getX()>=40 and self.getX()<=1240) and (self.getY() >=460 and self.getY()<=660) and (self.getX() + deltaX <190) and not self.touchAlreadyP2[0]:
            print("hit" + str(self.getX() + deltaX-25+100))
            self.touchAlreadyP1[0] = True

        #checkP3
        for i in range(4):
            if (self.getX()>=1040 and self.getX()<=1240) and (self.getY() >=260 and self.getY()<=460) and (self.getY() + deltaY >310+i*100) and not self.touchAlreadyP3[i]:
                print("hit" + str(self.getY() + deltaY-25))
                self.touchAlreadyP3[i] = True
        
        #checkP3
        for i in range(4):
            if (self.getX()>=40 and self.getX()<=240) and (self.getY() >=260 and self.getY()<=460) and (self.getY() + deltaY <310+i*100) and not self.touchAlreadyP4[2-i]:
                print("hit" + str(self.getY() + deltaY-25))
                self.touchAlreadyP4[1-i] = True
        

    
