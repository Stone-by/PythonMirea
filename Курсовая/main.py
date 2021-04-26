from tkinter import *
from tkinter import messagebox as mb
from tkinter.ttk import *
from PIL import ImageTk, Image
import random

Rez = 100

class GAME(object):
    def __init__(self, a, b, znak, ball):
        self.a = a
        self.b = b
        self.znak = znak
        self.ball = ball

    def sumator(self):
        if (self.znak == '+'):
            #print(str(self.a) + "+" + str(self.b))
            suma_2 = int(self.a + self.b)
            return suma_2
        if (self.znak == '-'):
            #print(str(self.a) + "-" + str(self.b))
            suma_2 = int(self.a - self.b)
            return suma_2
        if (self.znak == '*'):
            #print(str(self.a) + "*" + str(self.b))
            suma_2 = int(self.a * self.b)
            return suma_2
        if (self.znak == '/'):
            #print(str(self.a) + "/" + str(self.b))
            suma_2 = int(self.a / self.b)
            return suma_2

        # suma = int(input())
        #
        # if(suma == suma_2):
        #     return 1
        # else:
        #     return 0

    def PRINT(self):
        def chec():
            if (self.ball == 11):
                global Rez
                Rez = 1
                window.destroy()
            if (self.ball == -11):
                Rez = 0
                window.destroy()

        def Potverd():
            s = suma.get()
            if not s.isdigit():
                mb.showerror(
                    "Ошибка",
                    "Должно быть введено число")
            else:
                if (start.sumator() == int(suma.get())):
                    self.ball += 1

                    self.a = random.randint(1, 100)
                    self.b = random.randint(1, 100)
                    c = random.randint(1, 4)

                    if (c == 1):
                        self.znak = '+'
                    if (c == 2):
                        self.znak = '-'
                    if (c == 3):
                        self.znak = '*'
                    if (c == 4):
                        self.znak = '/'
                else:
                    self.ball -= 1

                    self.a = random.randint(1, 100)
                    self.b = random.randint(1, 100)
                    c = random.randint(1, 4)

                    if (c == 1):
                        self.znak = '+'
                    if (c == 2):
                        self.znak = '-'
                    if (c == 3):
                        self.znak = '*'
                    if (c == 4):
                        self.znak = '/'

                lbl1.config(text=str(self.a) + " " + str(self.znak) + " " + str(self.b) + " = ")
                # lbl2.config(text=str(self.znak))
                # lbl3.config(text=str(self.b))
                lbl4.config(text="Ваши баллы: " + str(self.ball))

                chec()

        window = Tk()

        window.title("Математическая игра")
        window.geometry('700x350')

        s = Style()
        s.configure('My.TFrame', background='red')
        mail1 = Frame(window, style='My.TFrame')
        mail1.place(height=350, width=700)
        mail1.config()

        lbl1 = Label(window, text=str(self.a) + " " + str(self.znak) + " " + str(self.b) + " = ")
        lbl1.grid(column=0, row=0)
        # lbl2 = Label(window, text=str(self.znak))
        # lbl2.grid(column=1, row=0)
        # lbl3 = Label(window, text=str(self.b) + " =")
        # lbl3.grid(column=2, row=0)

        lbl4 = Label(window, text="Ваши баллы: " + str(self.ball))
        lbl4.grid(column=0, row=1)

        suma = Entry(window, width=10)
        suma.grid(column=1, row=0)

        btn1 = Button(window, text="Потвердить", command=Potverd)
        btn1.grid(column=0, row=2)
        suma.focus()

        window.mainloop()

if __name__ == "__main__":
    a = 0
    b = 0
    znak = ''
    ball = 0

    a = random.randint(1, 100)
    b = random.randint(1, 100)
    c = random.randint(1, 4)

    if (c == 1):
        znak = '+'
    if (c == 2):
        znak = '-'
    if (c == 3):
        znak = '*'
    if (c == 4):
        znak = '/'

    start = GAME(a, b, znak, ball)
    start.PRINT()

    if(Rez == 1):
        root = Tk()
        img = ImageTk.PhotoImage(Image.open("Котик.png"))
        panel = Label(root, image=img)
        panel.pack(side="bottom", fill="both", expand="yes")
        root.mainloop()
    if(Rez == 0):
        root = Tk()
        img = ImageTk.PhotoImage(Image.open("3bVvalH00wI.jpg"))
        panel = Label(root, image=img)
        panel.pack(side="bottom", fill="both", expand="yes")
        root.mainloop()

    # if (start.sumator() == 1):
    #     ball += 1
    #     print("Ваши баллы: " + str(ball))
    # else:
    #     ball -= 1
    #     print("Ваши баллы: " + str(ball))