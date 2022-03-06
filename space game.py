try:
	from tkinter import *
except:
	from Tkinter import *
from PIL import Image, ImageTk
import random, pyglet, sys, os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



pyglet.font.add_file(resource_path('images/arcadeclassic.ttf'))
ArcadeClassic = pyglet.font.load('ArcadeClassic')

score = 0
bullet = 0
player_1_x = []
player_1_y = []
for i in range(560,(560+79)):
	player_1_x.append(i)
for i in range((590-87),590):
	player_1_y.append(i)
spawn_x = []
spawn_y = []
for i in range(500-150,(500+199+150)):
	spawn_x.append(i)
for i in range((650-150-147),650+150):
	spawn_y.append(i)

history=[]
moves = [10,0]
star=[]
z = 0
left_right_shoot = "middle"
name = "shoot "
root = Tk()
var = StringVar()
life = 3
stop_asteroids = "go"


def spawn_kill():
	global star, c, spawn_x, spawn_y, i_star, q, root
	for i_star in range(len(star)):
		q = c.coords(star[i_star])
		if q[1] in spawn_y:
			if q[0] in spawn_x:
				c.delete(star[i_star])
	root.after(1, if_hit)
def if_hit():
	global star, c, player_1, life, player_1_x, player_1_y,stop_asteroids,score
	for i in range(len(star)):
		a = c.coords(star[i])
		if a[1] in player_1_y:
			if a[0] in player_1_x:
				c.coords(star[i],random.randint(-500,1700),-600)
				root.after(1000)
				des = "life "+str(life)
				if life == 3:
					c.delete(lifeico4)
				elif life == 2:
					c.delete(lifeico3)
				elif life == 1:
					c.delete(lifeico2)
				elif life == 0:
					c.delete(lifeico1)
					moves[0] = 0
					stop_asteroids = "stop"
					c.move("all", 700,700)
					c.move("all", 700,700)
					c.create_text(600, 300,text = "game over",fill='Yellow',anchor=S,font=('ArcadeClassic', 35),tag="game over")
					score_text = "Score: " + str(score)
					score_counter=c.create_text(600, 310,text = score_text,fill='Yellow',anchor=N,font=('ArcadeClassic', 20),tag="score counter")
				life = life -1
	root.after(ms=1,func=if_hit)
def score_update():
	global score,score_counter,stop_asteroids,star, c, spawn_x, spawn_y, i_star, q
	if stop_asteroids != "stop":
		score += 100
		c.delete(score_counter)
		score_text = "Score: " + str(score)
		score_counter=c.create_text(5, 5,text = score_text,fill='yellow',anchor=NW,font=('ArcadeClassic', 15),tag="score counter")
	root.after(100,score_update)
	#if stop_asteroids == 'stop': 
	#	for i_star in range(len(star)):
	#		q = c.coords(star[i_star])
	#		if q[1] in spawn_y:
	#			if q[0] in spawn_x:
	#				c.delete(star[i_star])
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
	global iship, ship, player_1, c,left_right_shoot , current, moves, stop_asteroids, name, spawn_kill
	if stop_asteroids != "stop":
		if "Left" in history or "a" in history:
			left_right_shoot = "left"
			iship = Image.open(resource_path("images/ship.png"))
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
	elif stop_asteroids == "stop":
			if "space" in history:
				history.remove("space")
				root.destroy()
		

root.bind("<Escape>", lambda e: root.destroy())
Frame(root, height=20).pack()
root.wm_state('zoomed')
root.wm_title("Robert Kimber - Space Game")
root.iconbitmap(resource_path("images/ship.ico"))
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
c=Canvas(root,height=600,width=1200,bg="black")
root.bind_all('<KeyPress>', keydown)
root.bind_all('<KeyRelease>', keyup)
c.pack(side=TOP)
iship = Image.open(resource_path("images/ship_life.png"))
iship = iship.resize((60, 60), Image.ANTIALIAS)
ship = ImageTk.PhotoImage(iship)
player_1=c.create_image(560, 590,image=ship, anchor=SW,tag="player")
iship_life = Image.open(resource_path("images/ship_life.png"))
iship_life = iship_life.resize((40, 40), Image.ANTIALIAS)
ship_life = ImageTk.PhotoImage(iship_life)
score_text = "Score: " + str(score)
score_counter=c.create_text(5, 5,text = score_text,fill='yellow',anchor=NW,font=('ArcadeClassic', 15),tag="score counter")

def create_stars():
	global stars1, stars2, stars3, stars4, stars5, stars6, star, stars, stara
	stara = Image.open(resource_path("images/star1.png"))
	stars1 = ImageTk.PhotoImage(stara)
	stara = Image.open(resource_path("images/star2.png"))
	stars2 = ImageTk.PhotoImage(stara)
	stara = Image.open(resource_path("images/star3.png"))
	stars3 = ImageTk.PhotoImage(stara)
	stara = Image.open(resource_path("images/star4.png"))
	stars4 = ImageTk.PhotoImage(stara)
	stara = Image.open(resource_path("images/star5.png"))
	stars5 = ImageTk.PhotoImage(stara)
	stara = Image.open(resource_path("images/star6.png"))
	stars6 = ImageTk.PhotoImage(stara)
	for i in range(15):
		star.append(c.create_image(random.randint(-500,1700),random.randrange(-600,400),image= stars1))
		star.append(c.create_image(random.randint(-500,1700),random.randrange(-600,400),image= stars2))
		star.append(c.create_image(random.randint(-500,1700),random.randrange(-600,400),image= stars3))
		star.append(c.create_image(random.randint(-500,1700),random.randrange(-600,400),image= stars4))
		star.append(c.create_image(random.randint(-500,1700),random.randrange(-600,400),image= stars5))
		star.append(c.create_image(random.randint(-500,1700),random.randrange(-600,400),image= stars6))
create_stars()

def update_asteroids():
	global star, c, moves
	for i in range(len(star)):
		p = c.coords(star[i])
		p[1] = p[1] + moves[0]
		p[0] = p[0] + moves[1]
		c.coords(star[i],p[0],p[1])
		if stop_asteroids != "stop":
			if(p[1]>610):
				c.coords(star[i],random.randint(-500,1100),-600)
	root.after(50, update_asteroids)

lifeico1 = c.create_image(10, 595,image=ship_life, anchor=SW,tag="life 1")
lifeico2 = c.create_image(42, 595,image=ship_life, anchor=SW,tag="life 2")
lifeico3 = c.create_image(74, 595,image=ship_life, anchor=SW,tag="life 3")
lifeico4 = c.create_image(106, 595,image=ship_life, anchor=SW,tag="life 4")
if_hit()
update_asteroids()
score_update()
root.mainloop()

