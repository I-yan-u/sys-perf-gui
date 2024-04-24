import engine.sys_per
import customtkinter
import tkinter as tk
import turtle
from time import sleep

class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x400")
        self.title("System Performance")


app = App()
app.mainloop()

