try:
    from tkinter import *
except:
    from Tkinter import *
from PIL import Image, ImageTk
import random

score = 0
bullet = 0
player_1_x = []
player_1_y = []
for i in range(560,(560+79)):
    player_1_x.append(i)
for i in range((590-87),590):
    player_1_y.append(i)

history=[]
moves = [10,0]
star=[]
z = 0
left_right_shoot = "middle"
name = "shoot "
root = Tk()
var = StringVar()
speed = 600 / 10.0
wind = 600 / 1400.0
life = 3
stop_snow = "go"
def if_hit():
    global star, c, player_1, life, player_1_x, player_1_y,stop_snow,score
    for i in range(len(star)):
        a = c.coords(star[i])
        if a[1] in player_1_y:
            if a[0] in player_1_x:
                c.coords(star[i],random.randint(-500,1700),-600)
                root.after(1000)
                des = "life "+str(life)
                if life == 3:
                    c.delete(lifeico3)
                elif life == 2:
                    c.delete(lifeico2)
                elif life == 1:
                    c.delete(lifeico1)
                elif life == 0:
                    moves[0] = 0
                    stop_snow = "stop"
                    c.move("all", 700,700)
                    c.move("all", 700,700)
                    c.create_text(600, 300,text = "game over",fill='Yellow',anchor=S,font=('ArcadeClassic', 35),tag="game over")
                    score_text = "Score: " + str(score)
                    score_counter=c.create_text(600, 310,text = score_text,fill='Yellow',anchor=N,font=('ArcadeClassic', 20),tag="score counter")
                life = life -1
    root.after(1, if_hit)
def score_update():
    global score,score_counter,stop_snow
    if stop_snow != "stop":
        score += 100
        c.delete(score_counter)
        score_text = "Score: " + str(score)
        score_counter=c.create_text(5, 5,text = score_text,fill='yellow',anchor=NW,font=('ArcadeClassic', 15),tag="score counter")
    root.after(100,score_update)
def keyup(e):
    if  e.keysym in history :
        history.pop(history.index(e.keysym))
        Show_key()
        var.set(str(history))
    Show_key()
def keydown(e):
    if not e.keysym in history and e.keysym!="space":
        history.append(e.keysym)
        var.set(str(history))
    elif not e.keysym in history and e.keysym=="space":
        history.append(e.keysym)
        var.set(str(history))
    Show_key()
def Show_key():
    global name
    global iship, ship, player_1, c,left_right_shoot , current, moves, stop_snow
    if stop_snow != "stop":
        if "Left" in history or "a" in history:
            left_right_shoot = "left"
            iship = Image.open("ship.png")
            ship = ImageTk.PhotoImage(iship.rotate(15))
            c.delete(player_1)
            player_1=c.create_image(560, 590,image=ship, anchor=SW,tag="player")
            moves[1] = 5
            c.update() 
        if "Right" in history or "d" in history:
            left_right_shoot = "right"
            ship = ImageTk.PhotoImage(iship.rotate(-15))
            c.delete(player_1)
            player_1=c.create_image(560, 590,image=ship, anchor=SW,tag="player")
            moves[1] = -5
        if len(history)==0:
            moves[0]=10
            left_right_shoot = "middle"
            ship = ImageTk.PhotoImage(iship.rotate(0))
            c.delete(player_1)
            player_1=c.create_image(560, 590,image=ship, anchor=SW,tag="player")
            moves[1]=0
        if "space" in history:
            history.remove("space")
            moves[0] = 15
        else:
            moves[0] = 10
    elif stop_snow == "stop":
            if "space" in history:
                history.remove("space")
                root.destroy()
        

root.bind("<Escape>", lambda e: root.destroy())
Frame(root, height=20).pack()
root.wm_state('zoomed')
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
c=Canvas(root,height=600,width=1200,bg="black")
root.bind_all('<KeyPress>', keydown)
root.bind_all('<KeyRelease>', keyup)
c.pack(side=TOP)
iship = Image.open("ship_life.png")
iship = iship.resize((60, 60), Image.ANTIALIAS)
ship = ImageTk.PhotoImage(iship)
player_1=c.create_image(560, 590,image=ship, anchor=SW,tag="player")
iship_life = Image.open("ship_life.png")
iship_life = iship_life.resize((40, 40), Image.ANTIALIAS)
ship_life = ImageTk.PhotoImage(iship_life)
score_text = "Score: " + str(score)
score_counter=c.create_text(5, 5,text = score_text,fill='yellow',anchor=NW,font=('ArcadeClassic', 15),tag="score counter")
stara = Image.open("star1.png")
stars1 = ImageTk.PhotoImage(stara)
stara = Image.open("star2.png")
stars2 = ImageTk.PhotoImage(stara)
stara = Image.open("star3.png")
stars3 = ImageTk.PhotoImage(stara)
stara = Image.open("star4.png")
stars4 = ImageTk.PhotoImage(stara)
stara = Image.open("star5.png")
stars5 = ImageTk.PhotoImage(stara)
stara = Image.open("star6.png")
stars6 = ImageTk.PhotoImage(stara)
for i in range(15):
    star.append(c.create_image(random.randint(-500,1700),random.randrange(-600,600),image= stars1))
    star.append(c.create_image(random.randint(-500,1700),random.randrange(-600,600),image= stars2))
    star.append(c.create_image(random.randint(-500,1700),random.randrange(-600,600),image= stars3))
    star.append(c.create_image(random.randint(-500,1700),random.randrange(-600,600),image= stars4))
    star.append(c.create_image(random.randint(-500,1700),random.randrange(-600,600),image= stars5))
    star.append(c.create_image(random.randint(-500,1700),random.randrange(-600,600),image= stars6))


def update_trees():
    global star, c, moves
    for i in range(len(star)):
        p = c.coords(star[i])
        p[1] = p[1] + moves[0]
        p[0] = p[0] + moves[1]
        c.coords(star[i],p[0],p[1])
        if stop_snow != "stop":
            if(p[1]>610):
                c.coords(star[i],random.randint(-500,1100),-600)

    root.after(50, update_trees)
lifeico1 = c.create_image(10, 595,image=ship_life, anchor=SW,tag="life 1")
lifeico2 = c.create_image(42, 595,image=ship_life, anchor=SW,tag="life 2")
lifeico3 = c.create_image(74, 595,image=ship_life, anchor=SW,tag="life 3")
if_hit()
update_trees()
score_update()
root.mainloop()

