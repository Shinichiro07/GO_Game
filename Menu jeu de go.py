from tkinter import *

def button_destroy():
    button1.place_forget()
    button2.place_forget()
    button3.place_forget()
    canvas1.delete('all')


def afficher_regle():
    button1.place_forget()
    button2.place_forget()
    button3.place_forget()



window= Tk()
window.geometry("1200x600")
bg = PhotoImage(file = r"C:\Users\seb60\OneDrive\Bureau\Jeu de go\Jeu de go 2.png")



canvas1= Canvas(window,width =1200,height=600)
canvas1.pack(fill= "both",expand=True)
canvas1.create_image(0,0,image=bg,anchor="nw")

affichage_jeu_de_go=canvas1.create_text(600,100,text="JEU DE GO",font=("Harukaze",60),fill="Dark Red")



button1=Button(window,text="Play",width=25,height=1,bg="Black",fg="white",font=("Hashiba",20),relief="flat",command=button_destroy)
button2=Button(window,text="Rules",width=25,height=1,bg="Black",fg="white",font=("Hashiba",20),relief="flat",command=afficher_regle)
button3=Button(window,text="Settings",width=25,height=1,bg="Black",fg="white",font=("Hashiba",20),relief="flat")

button1.place(x=475,y=200)
button2.place(x=475,y=300)
button3.place(x=475,y=400)






window.mainloop()



