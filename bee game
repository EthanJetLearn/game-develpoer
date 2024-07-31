import pgzrun, random
WIDTH=500
HEIGHT=500
score=0
gameover=False
bee=Actor("bee")
flower=Actor("flower")
bee.pos=250,250
flower.pos=50,50
def draw():
    screen.blit("grass backround",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("score:"+str(score),color="black",topleft=(300,300))
    if gameover:
        screen.fill("yellow")
        screen.draw.text("Gameover your score is:"+str(score), color="black",topleft=(20,300))
def update():
    global score
    if keyboard.left:
        bee.x-=4
    if keyboard.right:
        bee.x+=4
    if keyboard.up:
        bee.y-=4
    if keyboard.down:
        bee.y+=4
    if bee.colliderect(flower):
        flower.pos=random.randint(50,450),random.randint(50,450)
        score+=10
def timer():
    global gameover
    gameover=True        
clock.schedule(timer,10)
pgzrun.go()    
