from tkinter import *


class menu:
    def __init__(self, canvas):
        self.screen= canvas
        self.button1= 0
        self.button2= 0
        self.button3= 0
        self.affichage_jeu_de_go_fr= 0
        self.affichage_jeu_de_go_jap= 0
        self.affichage= False

    
    def afficher(self):
        self.affichage= True
        
        self.button1= Button(self.screen,text="Play",width=25,height=1,bg="black",fg="white", font=("Hashiba",18),relief="flat")
        self.button2= Button(self.screen,text="Rules",width=25,height=1,bg="black",fg="white",font=("Hashiba",18),relief="flat",command= self.afficher_regle)
        self.button3= Button(self.screen,text="Settings",width=25,height=1,bg="black",fg="white",font=("Hashiba",18),relief="flat")
                
        self.affichage_jeu_de_go_fr=self.screen.create_text(600,100,anchor= "center", text="JEU DE GO",font=("Harukaze",200),fill="dark red", activefill= "white")
        self.affichage_jeu_de_go_jap=self.screen.create_text(600,250,anchor= "center", text="囲碁",font=("Harukaze",50),fill="black")
        
        print("ok")
        self.button1.place(x=420,y=350)
        self.button2.place(x=420,y=420)
        self.button3.place(x=420,y=490)


    def destroy(self):
        
        if self.affichage == True:
            self.screen.delete(self.affichage_jeu_de_go_fr)
            self.screen.delete(self.affichage_jeu_de_go_jap)
        
            self.button1.place_forget()
            self.button2.place_forget()
            self.button3.place_forget()
            #self.screen.delete('all')
            self.affichage= False




    def afficher_regle(self):
        self.destroy()
        affichage_regle=self.screen.create_text(600,100,anchor= "center", text="Rules",font=("Harukaze",200),fill="dark red")


#window= Tk()
#window.geometry("1200x600")
#bg = PhotoImage(file = r"C:\Users\adrien\Desktop\GO_Game\Jeu de go 2.png")
#canvas1= Canvas(window, width=3000, height=3000)
#canvas1.pack(fill= "both",expand=True)
#canvas1.create_image(0,0,image=bg,anchor="nw")'''






#window.mainloop()



