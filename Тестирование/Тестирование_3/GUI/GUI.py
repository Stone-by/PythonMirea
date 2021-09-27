from tkinter import *
import tkinter.ttk as ttk
from GUI.Game_GUI import Game


class GUI:
    def __init__(self):
        window = Tk()
        window.title('Собеседник')
        notebook = ttk.Notebook(window)
        notebook.pack(fill='both', expand='yes')

        frame1 = ttk.Frame(notebook)
        frame1.pack(fill='both', expand=True)

        Game(frame1)

        window.mainloop()
