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
        self.label_ghost = customtkinter.CTkLabel(self.frame2, text="")
        self.label_main = customtkinter.CTkLabel(self.frame2, text="", font=("Arial", 30))
        self.label_super = customtkinter.CTkLabel(self.frame2, text="", font=("Arial", 11))
        self.label_sub = customtkinter.CTkLabel(self.frame2, text="", font=("Arial", 11))

        # Pack Labels
        self.label_ghost.pack(padx=190)
        self.label_super.pack(anchor='nw')
        self.label_main.pack(pady=85.5)
        self.label_sub.pack(anchor='se')

    def view(self, data):
        self.label_main.configure(require_redraw=True, text=f'{data["main"]}%')
        self.label_sub.configure(require_redraw=True, text=f'Time left: {data["sub"]}')
        self.label_super.configure(require_redraw=True, text=f'Source: {data["super"]}')

    def update(self):
        data = {
            'main': sp.battery_info()[0],
            'sub': sp.battery_info()[1],
            'super': sp.battery_info()[2]
        }
        self.view(data)  # Update the GUI

        # Schedule the update method to be called every second
        self.after(500, self.update)


app = App()
app.update()
app.mainloop()

