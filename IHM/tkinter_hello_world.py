from tkinter import *
from tkinter.messagebox import showinfo

starter_color = ['yellow2', 'white', 'green', 'red', 'black']
correspond = {color[0].upper(): color for color in starter_color}

number_of_case = 5
#peg noir | blanc
history = [(['Y','W','G','R','B'],(1,2))]

def alert():
    showinfo("alerte", "Test!")

def switch_color(event):
    switch_dic_color = {starter_color[i]: starter_color[i + 1] for i in range(len(starter_color) - 1)}
    switch_dic_color[starter_color[len(starter_color) - 1]] = starter_color[0]
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

def frame_of_failure(fenetre):
    failure_frame = LabelFrame(fenetre, text='Combinaisons ratée', borderwidth=2, width=300, height=200, relief=GROOVE)

    for tryout in history:
        a_failure_frame = Frame(failure_frame, padx=20, pady=5)
        for char in tryout[0]:
            square = Canvas(a_failure_frame, width=20, height=20)
            square.pack(side=LEFT)
            square.create_rectangle(0, 50, 50, 0, fill=correspond[char])
        a_failure_frame.pack()

        his_peg_frame = Frame(a_failure_frame, padx=10, pady=10)
        his_peg_frame.pack()
        for black_peg in range(tryout[1][0]):
            circle = Canvas(his_peg_frame, width=5, height=5)
            circle.pack()
            circle.create_oval(0, 10, 10, 0, fill='black')
        for white_peg in range(tryout[1][1]):
            circle = Canvas(his_peg_frame, width=5, height=5)
            circle.pack()
            circle.create_oval(0, 10, 10, 0, fill='white')

    failure_frame.pack()


def frame_of_validation(fenetre):
    full_frame = Frame(fenetre, borderwidth=2, relief=GROOVE, width=200, height=200)
    button_frame = LabelFrame(full_frame,text='Combinaisons', borderwidth=2, relief=GROOVE)
    color_btn = []

    for i in range(number_of_case):
        counter = i
        if(i > len(starter_color)):
            counter = i // len(starter_color)

        thisButton = Button(button_frame, padx=10, pady=2, bg=starter_color[i])
        thisButton.bind('<Button>', switch_color)
        thisButton.pack(fill=Y,side=LEFT)
        color_btn.append(thisButton)

    validate = Button(full_frame, text="Valide", command=lambda: validate_pattern(color_btn))

    validate.pack(side=BOTTOM, padx=30, pady=10)
    button_frame.pack(side=TOP, padx=30, pady=5)
    full_frame.pack()


def validate_pattern(pattern):
    stringPattern = ([widget['bg'][0].upper() for widget in pattern])
    showinfo("alerte", stringPattern)

def init_IHM():
    fenetre = Tk()
    fenetre.title = "MasterMind"
    fenetre["bg"] = "white"
    fenetre.maxsize(1000, 400)
    fenetre.minsize(400, 300)
    init_menu(fenetre)

    frame_of_failure(fenetre)
    frame_of_validation(fenetre)

    fenetre.mainloop()