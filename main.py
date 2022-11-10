#Tkinter New Design
from tkinter import *
import time

window= Tk()
window.title("Tkinter Design Test")
window.geometry("1040x540")
window.config(background= "#0D0D0D")

screen= Canvas(window, width= 3000, height= 3000, bg= "black")
screen.place(x= 0, y= 0)
X= 0

def game_loop():
    global X
    X= X + 1
    print(X)


    screen.after(100, game_loop)




def click(event):
    print(event.x, event.y)
        

game_loop()
mainloop()