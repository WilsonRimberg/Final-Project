from ggame import App, RectangleAsset, ImageAsset, SoundAsset
from ggame import LineStyle, Color, Sprite, Sound, Frame

SCREEN_WIDTH = 1420
SCREEN_HEIGHT = 810
background_asset1=ImageAsset("images/Green.png",)
background_asset2=ImageAsset("images/starfield.jpg",)
background1=Sprite(background_asset1, (0,0))
background2=Sprite(background_asset2, (0,0))
castle_asset = ImageAsset("images/castleyeah.png",)
potato_asset = ImageAsset("images/potato.png",)
potato= Sprite(potato_asset, (300,600))
potato.scale=.3
potato.fxcenter = potato.fycenter = 0.5
castle= Sprite(castle_asset, (850,200))
castle.scale=.1
castle.fxcenter = castle.fycenter = 0.5
spaceship_asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')
spaceship = Sprite(spaceship_asset, (100, 100))
spaceship.fxcenter = spaceship.fycenter = 0.5
class Wall1(Sprite):
    asset= wall_asset=ImageAsset("images/wall.png",)
    def __init__(self, position):
        super().__init__(Wall1.asset, position)
        self.scale=.3
        self.fxcenter = self.fycenter = 0.5
        
class Wall2(Sprite):
    asset= wall_asset=ImageAsset("images/wall.png",)
    def __init__(self, position):
        super().__init__(Wall1.asset, position)
        self.scale=.3
        self.fxcenter = self.fycenter = 0.5
        self.rotation=(3.14159265358979/2)
uno=[]
for x in range(0,14):
    uno.append(Wall1((112+x*88,672)))
print(uno)
for x in range(0,14):
    uno.append(Wall1((112+x*88, 30)))
for x in range(0,7):
    uno.append(Wall2((81,87+x*88)))
for x in range(0,7):
    uno.append(Wall2((1287,87+x*88)))
print(uno)
# Movement
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
def left(b):
    spaceship.dir=-4
def right(b):
    spaceship.dir=4
def up(b):
    spaceship.bob=-4
def down(b):
    spaceship.bob=4
def step():
    if spaceship.collidingWith(castle) and castle.visible==True:
            background2.visible=False
            background1.visible=True
            castle.visible=False
            potato.visible=True
            for x in uno:
                x.visible=True
            
    if spaceship.collidingWith(potato) and potato.visible==True:
            background2.visible=True
            background1.visible=False
            castle.visible =True
            potato.visible=False
            Wall1.visible=False
            Wall1.visible=False
            for x in uno:
                x.visible=False
    if spaceship.go:
        spaceship.x += spaceship.dir
        if spaceship.x + spaceship.width > SCREEN_WIDTH:
            spaceship.x -= spaceship.dir
            spaceship.rotation=(3.141592653589793238462643383/2)
        if spaceship.x < 60:
            spaceship.x -= spaceship.dir
            spaceship.rotation=((3*3.141592653589793238462643383)/2)
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
        if spaceship.y < 60:
            spaceship.y -= spaceship.bob
            spaceship.rotation=3.141592653589793238462643383
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

