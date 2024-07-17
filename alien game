import pgzrun
TITLE="Alien game"
WIDTH=500
HEIGHT=500
message=""
alien=Actor("alien")
alien.pos=(250,250)
def draw():
    screen.clear()
    screen.fill("blue")
    screen.draw.text(message,center=(450,10),fontsize=30)
    alien.draw()
def update():
    alien.left+=5
    if alien.left>WIDTH:
        alien.right=0
def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message="good shot"
        sounds.eep.play()
    else:
        message="you missed"
pgzrun.go()        
