#Tkinter New Design
from tkinter import *
import time
from Goban_V1 import *


window= Tk()
window.title("Go Game")
window.geometry("1040x540")
window.config(background= "#0D0D0D")

screen= Canvas(window, width= 3000, height= 3000, bg= "black")
screen.place(x= 0, y= 0)

my_goban= goban(9, screen)


Turn= 0

nbTime= 0

def game_loop():
    global nbTime, labelTime

    nbTime= nbTime + 1
    
    labelTime.config(text= int(nbTime))



    screen.after(1000, game_loop)



def click(event):
    global Turn
    
    Turn= Turn + 1
    
    if Turn % 2 == 1:   
        my_goban.ajoute_pierre(event.x, event.y, "blue")
    else:
        my_goban.ajoute_pierre(event.x, event.y, "white")
            




labelTitle= Label(window, text = "Go Game", font=  ("Harukaze", 78, 'bold'), bg= 'black', fg= "blue")
labelTitle.place(x= 70, y= 2)

labelTime= Label(window, text = nbTime, font=  ("PixelSplitter", 25, 'bold'), bg= 'black', fg= "blue")
labelTime.place(x= 700, y= 100)


game_loop()
my_goban.create()
window.bind("<Button--1>", click)

mainloop()