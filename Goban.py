#Goban GO_Game
import time
import math


X= 0
Y= 0
V= 0



class goban:
    def __init__(self, taille, screen):
        self.format= int(taille)
        self.goban_map= []
        self.screen= screen
        self.turn= 0
        
    def create(self):
        if self.format == 9:
            
            self.goban_map= [['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                     ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                    ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                    ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                    ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                    ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                    ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                    ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                    ['0', '0', '0', '0', '0', '0', '0', '0', '0']]
        
        
            X1= 100
            Y1= 100

            X2= 102
            Y2= 450


            for x in range(9):
    
                self.screen.create_rectangle(100, Y1, 500, X2, fill= 'white')

                self.screen.create_rectangle(X1, 100, X2, 500, fill= 'white')
    
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
    
                self.screen.create_rectangle(100, Y1, 700, X2, fill= 'white')

                self.screen.create_rectangle(X1, 100, X2, 700, fill= 'white')
    
                X1= X1 + 50
                Y1= Y1 + 50

                X2= X2 + 50
                Y2= Y2 + 50
                
    
    def ajoute_pierre(self, coordX, coordY, couleur):
        coordX= arrondie(coordX // 10 / 5 - 2)
        coordY= arrondie(coordY // 10 / 5 - 2)
        
        if coordX >= 0 and coordX <= 8 and coordY >= 0 and coordY <= 8:
            if int(self.goban_map[coordX][coordY]) == 0:
                
                if couleur == "black":
                    self.goban_map[coordX][coordY]= 1
                    self.screen.create_oval(coordX*50 + 80, coordY*50 + 80, coordX*50 + 120, coordY*50 + 120, fill= "black")
            
                else:
                    self.goban_map[coordX][coordY]= 2
                    self.screen.create_oval(coordX*50 + 80, coordY*50 + 80, coordX*50 + 120, coordY*50 + 120, fill= "white")
   


def arrondie(X):
    X_int= int(X)

    X= X + 0.5

    if X_int < int(X):
        return int(X)
    else:
        return X_int
