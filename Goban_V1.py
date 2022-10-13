#Goban GO_Game
from tkinter import *
import time

window= Tk()
window.title("The Red Pacman")
window.geometry("1000x600")
window.config(background= "#0D0D0D")

class goban:
    def __init__(self, taille, canvas):
        self.format= int(taille)
        
    def create(self):
        if self.format == 9:
            X1, Y1= 20
            X2= 380
            Y2= 24



        for x in range(self.format):
            screen.create_rectangle(X1, Y1, X2, Y2, fill= 'red')
            
            screen.create_rectangle(68.75, 68.75, 72, 551, fill= '#F0F0F2')

    




screen= Canvas(window, width= 400, height= 400, bg= "#262526")
screen.place(x= 50, y= 25)

screen.create_rectangle(20, 20, 380, 25, fill= 'red')


mainloop()