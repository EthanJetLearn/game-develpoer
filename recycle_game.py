import pgzrun,random
HEIGHT=650
WIDTH=650
finallevel=6
trash=["chips","plastic bag","chips","bottle"]
startspeed=10
win=False
lose=False
curlvl=1
lvllist=[]
animations=[]
def draw():
    screen.clear()
    screen.blit("recycle backround 2.png",(0,0))
    if win:
        screen.draw.text("You win",fontsize=55,center=(325,325),color="white")
    elif lose:
        screen.draw.text("you lose",fontsize=55,center=(325,325),color="red")
    else:
        for i in lvllist:
            i.draw()
def update():
    global lvllist
    if len(lvllist)==0:
        lvllist=item_creator(curlvl)            
def item_creator(num):
    item_list=item_loader(num)
    item_images=image_loader(item_list)
    layout_items(item_images)
    animation(item_images)
    return item_images
def item_loader(num):
    item_list=["paper"]
    for i in range(num):
        item=random.choice(trash)
        item_list.append(item)
    return item_list
def image_loader(item_list):
    item_images=[]
    for i in item_list:
        item=Actor(i)
        item_images.append(item)
    return item_images    
def layout_items(abc):
    numgaps=len(abc)+1
    gapsize=625/numgaps
    random.shuffle(abc)
    for i,j in enumerate(abc,1):
        xpos=i*gapsize
        j.x=xpos
def animation(xyz):
    for i in xyz:
        timetaking=startspeed-curlvl
        i.anchor=("center","bottom")
        anime=animate(i,duration=timetaking,on_finished=finished,y=HEIGHT) 
        animations.append(anime)       
def finished():
    global lose
    lose=True
def on_mouse_down(pos):
    global lvllist
    for i in lvllist:
        if i.collidepoint(pos):
            if "paper" in i.image:
                winning()
            else:
                finished()
def winning():
    global win,lvllist,animations,finallevel,curlvl
    stop_animation(animations)
    if curlvl==finallevel:
        win=True
    else:
        curlvl+=1
        lvllist=[]
        animations=[] 
def stop_animation(jkl):
    for i in jkl:
        if i.running:
            i.stop()
pgzrun.go()        
