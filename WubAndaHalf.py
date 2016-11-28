from ggame import App, RectangleAsset, ImageAsset, SoundAsset
from ggame import LineStyle, Color, Sprite, Sound, Frame

SCREEN_WIDTH = 1420
SCREEN_HEIGHT = 810
potato=800
background_asset1=ImageAsset("images/Green.png",)
background_asset2=ImageAsset("images/starfield.jpg",)
background1=Sprite(background_asset1, (0,0))
background2=Sprite(background_asset2, (0,0))
spaceship_asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')
spaceship = Sprite(spaceship_asset, (740, 405))
spaceship.fxcenter = spaceship.fycenter = 0.5
# Movement
spaceship.dir = 3
spaceship.bob=3
spaceship.go = False
spaceship.ygo= False
spaceship.thrust = 0
spaceship.thrustframe = 1
def left(b):
    spaceship.dir=-4
def right(b):
    spaceship.dir=4
def up(b):
    spaceship.bob=-4
def down(b):
    spaceship.bob=4
    
def step():
    if spaceship.go:
        spaceship.x += spaceship.dir
        if spaceship.x + spaceship.width > potato:
            background1=Sprite(background_asset2, (0,0))
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
    

def rightKey(event):
    spaceship.go = True
    spaceship.ygo=False
    spaceship.thrust = 1
    spaceship.rotation=(3.141592653589793238462643383*3)/2
    right(spaceship)

def upKey(event):
    spaceship.ygo = True
    spaceship.go=False
    spaceship.thrust = 1
    spaceship.rotation=0
    up(spaceship)
    
def downKey (event):
    spaceship.ygo = True
    spaceship.go = False
    spaceship.thrust = 1
    spaceship.rotation=3.141592653589793238462643383
    down(spaceship)
myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.listenKeyEvent('keydown', 'a', leftKey)
myapp.listenKeyEvent('keydown', 'd', rightKey)
myapp.listenKeyEvent('keydown', 'w', upKey)
myapp.listenKeyEvent('keydown', 's', downKey)
myapp.run(step)

