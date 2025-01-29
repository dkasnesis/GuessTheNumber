from tkinter import *
import random
import os, sys
screen = Tk()
screen.configure(bg="#FFCCCC")
screen.geometry('450x300')
screen.resizable(height=False, width=False)
screen.title("Guess the number")


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def close_app():
    screen.destroy()


def randomise():
    global a
    tries_e.config(state="normal")
    check = choice.get()
    if check==1:
        a=random.randint(0,50)
        print(a)
    elif check==2:
        a=random.randint(0,100)
        print(a)
    elif check==3:
        a=random.randint(0,200)
        print(a)


def checka(event):
    global tries
    guess = tries_e.get()
    if int(guess) == a:
        imglbl.configure(image=correct)
        tries = tries + 1
        tries_e.config(state="disabled")
    elif int(guess) > a:
        imglbl.configure(image=down)
        tries = tries + 1
    elif int(guess) < a:
        imglbl.configure(image=up)
        tries = tries + 1
    tries_e.delete(0, END)
    triesl.config(text="tries:" + str(tries))


choice = IntVar()
choice.set(2) # ksekinaw me kapoio radiobutton epilegmeno
tries=0

up = PhotoImage(file=resource_path("uparrow.png"))
down = PhotoImage(file=resource_path("downarrow.png"))
correct = PhotoImage(file=resource_path("correct.png"))
dice = PhotoImage(file=resource_path("dice.png"))

imglbl= Label(screen, image=dice, bg="#FFCCCC")
imglbl.grid(row=5, column=0, rowspan=2)

lblt = Label(screen, text="Guess The Number!", fg="#660000", bg="#FFCCCC", font=("Impact",30))
lblt.grid(row=0, column=0, columnspan=3)
btnE= Radiobutton (screen, text="Easy: 0-50", font=("Ink Free", 13), fg="#FF3333", width=10, borderwidth=8, relief="groove", value=1, variable=choice)
btnE.grid(row=1, column=0)
btnM= Radiobutton (screen, text="Medium: 0-100", font=("Ink Free", 13), fg="#FF3333", width=13, borderwidth=8, relief="groove", value=2, variable=choice)
btnM.grid(row=1, column=1)
btnH= Radiobutton (screen, text="Hard: 0-200", font=("Ink Free", 13), fg="#FF3333", width=13, borderwidth=8, relief="groove", value=3, variable=choice)
btnH.grid(row=1, column=2)
lbli = Label(screen, text="~  In this game you will try to find a secret number that", fg="#CC0000", bg="#FFCCCC", font=("Book Antiqua",13))
lbli.grid(row=2, column=0, columnspan=3)
lbli2 = Label(screen, text="is randomly chosen every round. Try to guess it with", fg="#CC0000", bg="#FFCCCC", font=("Book Antiqua",13))
lbli2.grid(row=3, column=0, columnspan=3)
lbli3 = Label(screen, text="the least possible tries!", fg="#CC0000", bg="#FFCCCC", font=("Book Antiqua",13))
lbli3.grid(row=4, column=0, columnspan=3)
tries_e = Entry(screen, width=10, state="disabled")
tries_e.grid(row=5, column=1)
triesl = Label(screen, text="Tries: ", font=("Ink Free", 14), fg="#990000", bg="#FFCCCC")
triesl.grid(row=6, column=1)
btnEx=Button (screen, text="EXIT", font=("Impact", 14), fg="#FF9999", width=10, borderwidth=8, relief="groove",command=close_app)
btnEx.grid(row=5, column=2)
btnEx=Button (screen, text="RANDOMIZE", font=("Impact", 14), fg="#FF9999", width=10, borderwidth=8, relief="groove", command=randomise)
btnEx.grid(row=6, column=2)

screen.bind('<Return>', checka)

screen.mainloop()