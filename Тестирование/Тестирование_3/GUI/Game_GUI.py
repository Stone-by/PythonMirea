from tkinter import *

from Res import Game_back


class Game:
    def __init__(self, canvas):
        self._gui_game(canvas)
        self.index = 0

    def _gui_game(self, canvas):
        frame = Frame(canvas)
        frame.grid(pady=10, sticky='nsew')
        self._game(frame)

    def _game(self, frame):
        def _click1():
            self.index = 1

        def _click2():
            self.index = 2

        def _click3():
            self.index = 3

        def _click4():
            self.index = 4

        def _click5():
            self.index = 5

        def _click6():
            label['text'] = Game_back.game(entry.get(), self.index)

        buttons = ('Поздороваться', 'Познакомится', 'Спросить о предметах', 'Спросить о днях недели', 'Спросить о играх')

        button1 = Button(frame, text=buttons[0], bd=5, command=_click1)
        button1.grid(row=1, column=1, sticky="nsew", padx=2, pady=2)
        button2 = Button(frame, text=buttons[1], bd=5, command=_click2)
        button2.grid(row=2, column=1, sticky="nsew", padx=2, pady=2)
        button3 = Button(frame, text=buttons[2], bd=5, command=_click3)
        button3.grid(row=3, column=1, sticky="nsew", padx=2, pady=2)
        button4 = Button(frame, text=buttons[3], bd=5, command=_click4)
        button4.grid(row=4, column=1, sticky="nsew", padx=2, pady=2)
        button5 = Button(frame, text=buttons[4], bd=5, command=_click5)
        button5.grid(row=5, column=1, sticky="nsew", padx=2, pady=2)

        label = Label(frame, text='')
        label.grid(row=1, column=2, sticky="nsew", padx=2, pady=2)

        entry = Entry(frame, width=25)
        entry.grid(row=2, column=2, sticky="nsew", padx=2, pady=2)

        button6 = Button(frame, text='', bd=5, command=_click6)
        button6.grid(row=6, column=1, sticky="nsew", padx=2, pady=2)
