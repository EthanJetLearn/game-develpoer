import pgzrun
from random import randint
from time import time
HEIGHT=700
WIDTH=700
satilites=[]
lines=[]
starttime=0
totaltime=0
cursat=0
totalsat=10
def create_sat():
    global starttime,satilite
    for i in range(totalsat):
        satilite=Actor("satilite")
        satilite.pos=randint(50,650),randint(50,650)
        satilites.append(satilite)
    starttime=time()
def draw():
    global totaltime,satilites,lines
    screen.blit("space",(0,0))
    num=1
    for i in (satilites):
        i.draw()
        screen.draw.text(str(num),(i.pos[0],i.pos[1]+20))
        num+=1
    if cursat<totalsat:
        totaltime=time()-starttime
        screen.draw.text(str(round(totaltime,2)),(10,10),fontsize=25)  
    for i in lines:
        screen.draw.line(i[0],i[1],color="white")      
def update():
    pass
def on_mouse_down(pos):
    global satilites,cursat,lines 
    if cursat<totalsat:
        if satilites[cursat].collidepoint(pos):
            if cursat:
                lines.append((satilites[cursat-1].pos,satilites[cursat].pos))
            cursat+=1
        else:
            lines=[]
            cursat=0        
create_sat()
pgzrun.go()        
