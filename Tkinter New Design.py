#Tkinter New Design
from tkinter import *
import time

window= Tk()
window.title("Tkinter Design Test")
window.geometry("1040x540")
window.config(background= "#0D0D0D")

screen= Canvas(window, width= 3000, height= 3000, bg= "white")

screen.place(x= 0, y= 0)

def click(event):
    print(event.x, event.y)

window.bind("<Button--1>", click)

X1= 100
Y1= 100

X2= 102
Y2= 450


for x in range(8):
    
    screen.create_rectangle(100, Y1, 450, X2, fill= 'black')

    screen.create_rectangle(X1, 100, X2, 450, fill= 'black')
    
    X1= X1 + 50
    Y1= Y1 + 50

    X2= X2 + 50
    Y2= Y2 + 50 
    
    

    
        
mainloop()

