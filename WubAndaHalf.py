from ggame import App, RectangleAsset, ImageAsset, SoundAsset, TextAsset
from ggame import LineStyle, Color, Sprite, Sound, Frame

SCREEN_WIDTH = 1420
SCREEN_HEIGHT = 810
black=Color(0x000000, 1.0)
edge=LineStyle(1,black)
background_asset4=TextAsset("Game Over.", align='center', style='200px Arial', width=2000 )
background_asset5=TextAsset("Press 'Return' to restart.", align='center', style='40px Arial', width=1000)
background4=Sprite(background_asset4, (200,0))
background5=Sprite(background_asset5, (600,600))
background_asset1=ImageAsset("images/Green.png",)
background_asset2=ImageAsset("images/starfield.jpg",)
background_asset3=RectangleAsset(1420,810,edge, black)
background1=Sprite(background_asset1, (0,0))
background2=Sprite(background_asset2, (0,0))
background3=Sprite(background_asset3, (0,0))
castle_asset = ImageAsset("images/castleyeah.png",)
factory_asset = ImageAsset("images/Factory.png",)
factory=Sprite(factory_asset,(100,100))
factory.scale=.25
potato_asset = ImageAsset("images/door.jpg",)
potato= Sprite(potato_asset, (300,675))
potato.scale=.05
potato.fxcenter = potato.fycenter = 0.5
castle= Sprite(castle_asset, (850,200))
castle.scale=.1
castle.fxcenter = castle.fycenter = 0.5
class FactoryFloor(Sprite):
    factoryflr= floor_asset=ImageAsset("images/stonefloor.jpg",)
    def __init__(self, position):
        super().__init__(FactoryFloor.factoryflr, position)
        self.scale=.15
        self.fxcenter = self.fycenter = 0.5
does=[]
for x in range (0,14):
    does.append(FactoryFloor((1200-x*76,600)))
for x in range (0,14):
    does.append(FactoryFloor((1200-x*76,524)))
for x in range (0,6):
    does.append(FactoryFloor((212,448-76*x)))
for x in range (0,6):
    does.append(FactoryFloor((288,448-76*x)))
for x in range (0,12):
    does.append(FactoryFloor((364+76*x,68)))
for x in range (0,12):
    does.append(FactoryFloor((364+76*x,144)))
spaceship_asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')
spaceship = Sprite(spaceship_asset, (200, 200))
spaceship.fxcenter = spaceship.fycenter = 0.5
spaceship.scale=.6

class Wall1(Sprite):
    asset= wall_asset=ImageAsset("images/wall.png",)
    def __init__(self, position):
        super().__init__(Wall1.asset, position)
        self.scale=.3
        self.fxcenter = self.fycenter = 0.5
        
class Wall2(Sprite):
    asset= wall_asset=ImageAsset("images/wall.png",)
    def __init__(self, position):
        super().__init__(Wall2.asset, position)
        self.scale=.3
        self.fxcenter = self.fycenter = 0.5
        self.rotation=(3.14159265358979/2)

uno=[]
for x in range(0,14):
    uno.append(Wall1((112+x*88,672)))
for x in range(0,14):
    uno.append(Wall1((112+x*88, 30)))
for x in range(0,7):
    uno.append(Wall2((81,87+x*88)))
for x in range(0,7):
    uno.append(Wall2((1287,87+x*88)))
print(uno)
chips_asset=ImageAsset("images/dipsiedoodles.png",)
chips=Sprite(chips_asset, (1150,100))
chips.scale=.2
# Movement
sun_asset = ImageAsset("images/sun.png",)
sun=Sprite(sun_asset, (1150, 500))
sun.center=.5
spaceship.dir = 3
spaceship.bob=3
spaceship.go = False
spaceship.ygo= False
spaceship.thrust = 0
spaceship.thrustframe = 1
background1.visible=True
background2.visible=False
castle.visible=False
potato.visible= True
factory.visible=False
sun.visible=False
background3.visible=False
chips.visible=False
winning=False

def left(b):
    spaceship.dir=-4
def right(b):
    spaceship.dir=4
def up(b):
    spaceship.bob=-4
def down(b):
    spaceship.bob=4
def step():
    if background1.visible==True:
        for x in does:
                x.visible=False
    if spaceship.visible==False:
            background2.visible=False
            background1.visible=False
            background3.visible=False
            castle.visible=False
            potato.visible=False
            factory.visible=False
            sun.visible=False
            spaceship.x=1050
            spaceship.y=550
            chips.visible=False
            for x in uno:
                x.visible=False
            for x in does:
                x.visible=False
    if spaceship.collidingWith(chips) and chips.visible==True:
            sun.visible=True
            winning=True
            chips.visible=False
    if spaceship.collidingWith(sun) and sun.visible==True:
            background2.visible=True
            background3.visible=False
            castle.visible=True
            factory.visible=True
            sun.visible=False
            spaceship.x=100
            spaceship.y=300
            for x in does:
                x.visible=False
    if spaceship.collidingWith(factory) and castle.visible==True:
            background2.visible=False
            background1.visible=False
            background3.visible=True
            castle.visible=False
            potato.visible=False
            factory.visible=False
            sun.visible=False
            spaceship.x=1000
            spaceship.y=550
            chips.visible=True
            for x in uno:
                x.visible=False
            for x in does:
                x.visible=True
    if spaceship.collidingWith(castle) and castle.visible==True:
            background2.visible=False
            background1.visible=True
            castle.visible=False
            potato.visible=True
            spaceship.x=300
            spaceship.y=480
            factory.visible=False
            for x in uno:
                x.visible=True
    if spaceship.collidingWith(potato) and potato.visible==True:
            background2.visible=True
            background1.visible=False
            castle.visible =True
            potato.visible=False
            factory.visible=True
            spaceship.x=850
            spaceship.y=330
            for x in uno:
                x.visible=False
    if spaceship.go:
        spaceship.x += spaceship.dir
        if spaceship.x + spaceship.width > SCREEN_WIDTH:
            spaceship.x -= spaceship.dir
        if background3.visible==True: 
            if spaceship.x<1300 and spaceship.x>400:
                if spaceship.y<800 and spaceship.y>400:
                    spaceship.x+=spaceship.dir
                if spaceship.y<150 and spaceship.y:
                    spaceship.x+=spaceship.dir
                if spaceship.y>150 and spaceship.y<520:
                     spaceship.x-=spaceship.dir
                     spaceship.visible=False
                     print("1")
            if spaceship.x<320 and spaceship.x>250:
                if spaceship.y<800 and spaceship.y>30:
                    spaceship.x+=spaceship.dir
                else:
                   spaceship.visible=False
                   print("2")
            if spaceship.y<400 and spaceship.y>30:
                if spaceship.x<320 and spaceship.x>200:
                    spaceship.x+=spaceship.dir
                else:
                    spaceship.visible=False
                    print("3")
            if spaceship.x>1200:
                spaceship.visible=False
                print("4")
            if spaceship.x<210:
                spaceship.visible=False
                print("5")
            if spaceship.y>605:
                spaceship.visible=False
                print("6")
        if spaceship.x +spaceship.width > 1280 and potato.visible==True:
             spaceship.x -= spaceship.dir
        if spaceship.x < 153 and potato.visible==True:
             spaceship.x -= spaceship.dir
        if spaceship.x < 60:
            spaceship.x -= spaceship.dir
        if spaceship.thrust == 1:
            spaceship.setImage(spaceship.thrustframe)
            spaceship.thrustframe += 1
            if spaceship.thrustframe == 4:
                spaceship.thrustframe = 1
        if spaceship.thrust == 0:
            spaceship.setImage(0)
    ystep()
    
def ystep():
    if spaceship.ygo:
        spaceship.y += spaceship.bob
        if spaceship.y +spaceship.height > SCREEN_HEIGHT+60:
            spaceship.y -= spaceship.bob
            spaceship.rotation=0
        if background3.visible==True: 
            if spaceship.x<1300 and spaceship.x>400:
                if spaceship.y<605 and spaceship.y>520:
                    spaceship.y+=spaceship.bob
                if spaceship.y>50 and spaceship.y<150:
                    spaceship.y+=spaceship.bob
                if spaceship.y>150 and spaceship.y<520:
                    spaceship.y-=spaceship.bob
                    spaceship.visible=False
                    print("7")
            if spaceship.x<320 and spaceship.x>180:
                if spaceship.y<800 and spaceship.y>30:
                    spaceship.y+=spaceship.bob
                else:
                    spaceship.visible=False
                    print("8")
            if spaceship.x>1200:
                spaceship.visible=False
                print("9")
            if spaceship.x<210:
                spaceship.visible=False
                print("10")
            if spaceship.y>605:
                spaceship.visible=False
                print("11")
        #if background3.visible==True and spaceship.collidingWithSprites(self, sclass=FactoryFloor)>0:
            #spaceship.y += spaceship.bob
        #if background3.visible==True and spaceship.collidingWithSprites(self, sclass=FactoryFloor)==0:
            #spaceship.x -= spaceship.bob
        if spaceship.y +spaceship.height > 722 and potato.visible==True:
             spaceship.y -= spaceship.bob
        if spaceship.y < 104 and potato.visible==True:
            spaceship.y-=spaceship.bob
        if spaceship.y < 60:
            spaceship.y -= spaceship.bob
        if spaceship.thrust == 1:
            spaceship.setImage(spaceship.thrustframe)
            spaceship.thrustframe += 1
            if spaceship.thrustframe == 4:
                spaceship.thrustframe = 1
        if spaceship.thrust == 0:
            spaceship.setImage(0)

def leftKey(event):
    spaceship.go = True
    spaceship.ygo= False
    spaceship.thrust = 1
    spaceship.rotation=(3.141592653589793238462643383/2)
    left(spaceship)
def leftUp(event):
    spaceship.go = False
    spaceship.ygo= False
    spaceship.thrust = 1
    left(spaceship)
    

def rightKey(event):
    spaceship.go = True
    spaceship.ygo=False
    spaceship.thrust = 1
    spaceship.rotation=(3.141592653589793238462643383*3)/2
    right(spaceship)
def rightUp(event):
    spaceship.go = False
    spaceship.ygo= False
    spaceship.thrust = 1
    right(spaceship)
    

def upKey(event):
    spaceship.ygo = True
    spaceship.go=False
    spaceship.thrust = 1
    spaceship.rotation=0
    up(spaceship)
def upUp(event):
    spaceship.go = False
    spaceship.ygo= False
    spaceship.thrust = 1
    up(spaceship)
    
    
def downKey (event):
    spaceship.ygo = True
    spaceship.go = False
    spaceship.thrust = 1
    spaceship.rotation=3.141592653589793238462643383
    down(spaceship)
def downUp(event):
    spaceship.go = False
    spaceship.ygo= False
    spaceship.thrust = 1
    down(spaceship)
    
def stopx(event):
    spaceship.dir-=0

myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.listenKeyEvent('keydown', 'a', leftKey)
myapp.listenKeyEvent('keyup', 'a', leftUp)
myapp.listenKeyEvent('keydown', 'd', rightKey)
myapp.listenKeyEvent('keyup', 'd', rightUp)
myapp.listenKeyEvent('keydown', 'w', upKey)
myapp.listenKeyEvent('keyup', 'w', upUp)
myapp.listenKeyEvent('keydown', 's', downKey)
myapp.listenKeyEvent('keyup', 's', downUp)
myapp.run(step)


