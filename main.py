#Tkinter New Design
from tkinter import *
import time
from Goban_V1 import *
from Menu import *


window= Tk()
window.title("Go Game")
window.geometry("1200x600")
window.config(background= "#0D0D0D")

screen= Canvas(window, width= 3000, height= 3000, bg= "black")
screen.place(x= 0, y= 0)

my_goban= goban(9, screen)


Turn= 0

nbTime= 0

def game_loop():
    global nbTime, labelTime

    #nbTime= nbTime + 1
    
    #labelTime.config(text= int(nbTime))
    
   


    screen.after(1000, game_loop)



def click(event):
    global Turn
    
    Turn= Turn + 1
    
    if Turn % 2 == 1:   
        my_goban.ajoute_pierre(event.x, event.y, "black")
    else:
        my_goban.ajoute_pierre(event.x, event.y, "white")
            

bg = PhotoImage(file = r"C:\Users\adrien\Desktop\GO_Game\Jeu de go 2.png")

screen.create_image(0,0,image=bg,anchor="nw")



#labelTitle= Label(window, text = "Go Game", font=  ("Harukaze", 78, 'bold'), fg= "red")
#labelTitle.place(x= 70, y= 2)

#labelTime= Label(window, text = nbTime, font=  ("PixelSplitter", 25, 'bold'), fg= "red")
#labelTime.place(x= 700, y= 100)


game_loop()
menu= menu(screen)
menu.afficher()



window.bind("<Button--1>", click)

mainloop()