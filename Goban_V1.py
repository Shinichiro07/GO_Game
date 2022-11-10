#Goban GO_Game
from tkinter import *
import time
import math

window= Tk()
window.title("GO_Game")
window.geometry("1200x600")
window.config(background= "#0D0D0D")


screen= Canvas(window, width= 3000, height= 3000, bg= "black")
screen.place(x= 0, y= 0)

X= 0
Y= 0
V= 0



class goban:
    def __init__(self, taille):
        self.format= int(taille)
        self.goban= [X for X in range(7)]
        
    def create(self):
        if self.format == 9:
            X1= 100
            Y1= 100

            X2= 102
            Y2= 450


            for x in range(9):
    
                screen.create_rectangle(100, Y1, 500, X2, fill= 'white')

                screen.create_rectangle(X1, 100, X2, 500, fill= 'white')
    
                X1= X1 + 50
                Y1= Y1 + 50

                X2= X2 + 50
                Y2= Y2 + 50 

        elif self.format == 13:
            X1= 100
            Y1= 100

            X2= 102
            Y2= 450


            for x in range(13):
    
                screen.create_rectangle(100, Y1, 700, X2, fill= 'white')

                screen.create_rectangle(X1, 100, X2, 700, fill= 'white')
    
                X1= X1 + 50
                Y1= Y1 + 50

                X2= X2 + 50
                Y2= Y2 + 50 

def click(event):
    global X, Y, V

    V= V + 1


    X= arrondie(event.x // 10 / 5 - 2)
    Y= arrondie(event.y // 10 / 5 - 2)

    if X >= 0 and X <= 8 and Y >= 0 and Y <= 8:
        if V % 2 == 1:

            screen.create_oval(X*50 + 80, Y*50 + 80, X*50 + 120, Y*50 + 120, fill= "white")
        else:
            screen.create_oval(X*50 + 80, Y*50 + 80, X*50 + 120, Y*50 + 120, fill= "blue")

   
    print(X, Y)

window.bind("<Button--1>", click)

def arrondie(X):
    X_int= int(X)

    X= X + 0.5

    if X_int < int(X):
        return int(X)
    else:
        return X_int




my_goban= goban(9)
my_goban.create()

mainloop()
