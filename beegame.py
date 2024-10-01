import pgzrun
import random

WIDTH=500
HEIGHT=500
TITLE="BeeGame"

bee=Actor("bee")
bee.pos=(250,250)

flower=Actor("flower")
flower.pos=(50,50)

Score=0

def draw():  
    screen.blit("background",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("Score:"+str(Score), color="black", topleft=(10,10))

def place_flower():
    flower.x=random.randint(50, WIDTH-50)
    flower.y=random.randint(50, HEIGHT-50)

def update():
    global Score
    if keyboard.left:
       bee.x-=2
    if keyboard.up:
        bee.y-=2
    if keyboard.right:
        bee.x+=2
    if keyboard.down:
       bee.y+=2

    if bee.colliderect(flower):
        Score=Score+10
        place_flower()

pgzrun.go()