import pgzrun
TITLE="quiz"
WIDTH=680
HEIGHT=680
scroll_box=Rect(0,0,680,100)
Qb=Rect(10,120,500,150)
box_1=Rect(10,290,220,150)
box_2=Rect(270,290,220,150)
box_3=Rect(10,460,220,150)
box_4=Rect(270,460,220,150)
Tb=Rect(520,120,140,150)
Sb=Rect(520,290,140,300)
answer_box=[box_1,box_2,box_3,box_4]
score=0
total_time=10
qfile="C:/Users/ethan/OneDrive/Desktop/gam dev 1/questions.txt"
questions=[]
finish=False
count=0
curq=0

def draw():
    screen.clear()
    screen.fill("blue")
    screen.draw.filled_rect(scroll_box,"orange")
    screen.draw.filled_rect(Qb,"orange")
    for i in answer_box:
        screen.draw.filled_rect(i,"orange")
    screen.draw.filled_rect(Tb,"sky blue")
    screen.draw.filled_rect(Sb,"green")
    message=f"Welcome to quiz master. You are at Q:{curq} of {count}"
    screen.draw.textbox(message,scroll_box,color="white")     
    screen.draw.textbox(str(total_time),Tb,color="black")
    screen.draw.textbox("skip",Sb,color="black",angle=-90)
    screen.draw.textbox(question[0],Qb,color="White")
    index=1
    for i in answer_box:
        screen.draw.textbox(question[index].strip(),i,color="white")
        index+=1

def update():
    scroll_box.x-=2
    if scroll_box.right<0:
        scroll_box.left=WIDTH

def readq():
    global count,questions,qfile
    with open(qfile,"r") as file:
        for i in file:
            questions.append(i)
            count+=1


def eq():
    global curq
    curq+=1
    return questions.pop(0).split("|")
    
def on_mouse_down(pos):
    global question,score,total_time
    index=1
    for i in answer_box:
        if i.collidepoint(pos):
            if index is int(question[5]):
                score+=1
                if questions:
                    question=eq()
                    total_time=10                    
                else:
                    gameover() 
            else:
                gameover()
        index+=1
    if Sb.collidepoint(pos):
        skip()    

def gameover():
    global question,finish,total_time
    message=f"gameover you got {score} out of 10"
    question=[message,"-","-","-","-",6]
    total_time=0
    finish=True
def skip():
    global question,total_time
    if questions and not finish:
        question=eq()
        total_time=10 
    else:
        gameover()  
def timer():
    global total_time
    if total_time:
        total_time-=1
    else:
        gameover()                                
readq()
question=eq()
clock.schedule_interval(timer,1)            
pgzrun.go()    
