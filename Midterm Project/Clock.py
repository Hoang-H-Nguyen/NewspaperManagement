# importing whole module
from tkinter import *
from tkinter.ttk import *
from time import strftime


class DigitalClock:
    def __init__(self, window, clockLabel):
        self.window = window
        self.clockLabel = clockLabel
        self.clockLabel.place(x=0, y=0)
        self.display_time()

    def display_time(self):
        self.current_time = strftime('%H:%M:%S %p')
        self.clockLabel['text'] = self.current_time
        self.window.after(200, self.display_time)
