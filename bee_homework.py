import pgzrun, random
WIDTH=500
HEIGHT=500
score=0
gameover=False
lion=Actor("lion")
zebra=Actor("zebra")
lion.pos=250,250
zebra.pos=50,50
def draw():
    screen.blit("grass backround",(0,0))
    lion.draw()
    zebra.draw()
    screen.draw.text("score:"+str(score),color="black",topleft=(300,300))
    if gameover:
        screen.fill("yellow")
        screen.draw.text("Gameover your score is:"+str(score), color="black",topleft=(20,300))
def update():
    global score
    if keyboard.left:
        lion.x-=4
    if keyboard.right:
        lion.x+=4
    if keyboard.up:
        lion.y-=4
    if keyboard.down:
        lion.y+=4
    if lion.colliderect(zebra):
        zebra.pos=random.randint(50,450),random.randint(50,450)
        score+=10
def timer():
    global gameover
    gameover=True        
clock.schedule(timer,10)
pgzrun.go()    
