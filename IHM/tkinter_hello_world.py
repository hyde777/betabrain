from tkinter import *
from tkinter.messagebox import showinfo


def alert():
    showinfo("alerte", "Test!")

def switch_color(event):
    switch_dic_color = {"red" : "green", "green" : "black", "black" : "yellow2", "yellow2" : "white", "white" : "red"}
    widget = event.widget
    widget.configure(bg=switch_dic_color[widget['bg']])


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

def frame_of_validation(fenetre):
    tryout_frame = Frame(fenetre, borderwidth=2, relief=GROOVE)
    starterColor = ['yellow2','white','green','red','black']
    color_btn = []

    for i in range(len(starterColor)):
        thisButton = Button(tryout_frame, padx=10, pady=2, bg=starterColor[i])
        thisButton.bind('<Button>', switch_color)
        thisButton.grid(row=0, column=i)
        color_btn.append(thisButton)

    validate = Button(tryout_frame, text="Valide", command=lambda: validate_pattern(color_btn))
    validate.grid(row=0, column=7)
    tryout_frame.pack(side="top", padx=30, pady=30)

def validate_pattern( pattern):
    stringPattern = ''.join([widget['bg'][0] for widget in pattern])
    showinfo("alerte", stringPattern)

def init_IHM():
    fenetre = Tk()
    fenetre.title = "MasterMind"
    fenetre["bg"] = "white"

    init_menu(fenetre)

    frame_of_validation(fenetre)
    label = Label(fenetre, text="Hello World")
    label.pack()

    fenetre.mainloop()