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

        # Init Frames
        self.frame1 = customtkinter.CTkFrame(self, width=150, height=350)
        self.frame2 = customtkinter.CTkFrame(self, width=380, height=350)

        # Pack Frames
        self.frame1.pack(side="left", padx=5, pady=5)
        self.frame2.pack(side="right", padx=5, pady=5)

        # Init Buttons
        self.button_b3 = customtkinter.CTkButton(self.frame1, text="Battery Info", command=None, height=30)
        self.button_Cpu = customtkinter.CTkButton(self.frame1, text="CPU Usage", command=None, height=30)
        self.button_Mem = customtkinter.CTkButton(self.frame1, text="Memory Usage", command=None, height=30)
        
        # Pack Buttons
        self.button_b3.pack(padx=5, pady=60.25)
        self.button_Cpu.pack(padx=5, pady=5)
        self.button_Mem.pack(padx=5, pady=60.25)

        # Init Labels
        self.label_main = customtkinter.CTkLabel(self.frame2, text="", font=("Arial", 28))
        self.label_super = customtkinter.CTkLabel(self.frame2, text="", font=("Arial", 16))
        self.label_sub = customtkinter.CTkLabel(self.frame2, text="", font=("Arial", 16))

        # Pack Labels

app = App()
app.mainloop()

