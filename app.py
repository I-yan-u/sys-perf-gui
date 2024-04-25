import engine.sys_per as sp
import customtkinter
import tkinter as tk
import turtle
from time import sleep

class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x400")
        self.title("System Performance")


        self.frame1 = customtkinter.CTkFrame(self, width=150, height=350)
        self.frame2 = customtkinter.CTkFrame(self, width=380, height=350)

        self.frame1.pack(side="left", padx=5, pady=5)
        self.frame2.pack(side="right", padx=5, pady=5)

        self.

app = App()
app.mainloop()

