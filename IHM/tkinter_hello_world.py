from tkinter import *
from tkinter.messagebox import showinfo


def alert():
    showinfo("alerte", "Test!")

def init_menu(fenetre):
    menubar = Menu(fenetre)

    menu1 = Menu(menubar, tearoff=0)
    menu1.add_command(label="Créer", command=alert)
    menu1.add_command(label="Editer", command=alert)
    menu1.add_separator()
    menu1.add_command(label="Quitter", command=fenetre.quit)
    menubar.add_cascade(label="Fichier", menu=menu1)

    menu2 = Menu(menubar, tearoff=0)
    menu2.add_command(label="Couper", command=alert)
    menu2.add_command(label="Copier", command=alert)
    menu2.add_command(label="Coller", command=alert)
    menubar.add_cascade(label="Editer", menu=menu2)

    menu3 = Menu(menubar, tearoff=0)
    menu3.add_command(label="A propos", command=alert)
    menubar.add_cascade(label="Aide", menu=menu3)

    fenetre.config(menu=menubar)

def frame_of_tryout(fenetre):
    tryout_frame = Frame(fenetre, borderwidth=2, relief=GROOVE)
    tryout_frame.pack(side="top", padx=30, pady=30)
    #ajouter un stackpanel pouvoir empiler les essai


def init_dico_color():
    dic_color = {"R" : "red", "G" : "green", "B" : "black", "W" : "white", "Y" : "yellow"}
    base_colors = "RGBWY"

def init_IHM():
    fenetre = Tk()
    fenetre["bg"] = "white"

    init_menu(fenetre)
    frame_of_tryout(fenetre)
    label = Label(fenetre, text="Hello World")
    label.pack()

    fenetre.mainloop()