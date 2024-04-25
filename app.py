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
        self.default_view = "cpu"

        # Init Frames
        self.frame1 = customtkinter.CTkFrame(self, width=150, height=350)
        self.frame2 = customtkinter.CTkFrame(self, width=380, height=350)

        # Pack Frames
        self.frame1.pack(side="left", padx=5, pady=5)
        self.frame2.pack(side="right", padx=5, pady=5)

        # Init Buttons
        self.button_b3 = customtkinter.CTkButton(self.frame1, text="Battery Info", command=self.ba3_view, height=30)
        self.button_Cpu = customtkinter.CTkButton(self.frame1, text="CPU Usage", command=self.cpu_view, height=30)
        self.button_Mem = customtkinter.CTkButton(self.frame1, text="Memory Usage", command=self.mem_view, height=30)
        
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
        self.label_main.configure(require_redraw=True, text=data["main"])
        self.label_sub.configure(require_redraw=True, text=data["sub"])
        self.label_super.configure(require_redraw=True, text=data["super"])

    def ba3_view(self):
        self.default_view = "battery"
        self.update()

    def cpu_view(self):
        self.default_view = "cpu"
        self.update()

    def mem_view(self):
        self.default_view = "mem"
        self.update()

    def update(self):
        if self.default_view == "battery":
            data = {
                'main': f'{sp.battery_info()[0]}%',
                'sub': f'Time left: {sp.battery_info()[1]}',
                'super': f'Source: {sp.battery_info()[2]}'
            }
        elif self.default_view == "cpu":
            data = {
                'main': f'{sp.cpu_per()}%',
                'sub': f'Total CPUs: {sp.cpu_count()}',
                'super': f'Time Awake: {sp.cpu_times()}'
            }
        elif self.default_view == "mem":
            data = {
                'main': f'{sp.mem_per()}%',
                'sub': f'Total CPUs: {sp.cpu_count()}',
                'super': f'Time Awake: {sp.cpu_times()}'
            }
        self.view(data)  # Update the GUI

        # Schedule the update method to be called every 1/2second
        self.after(1000, self.update)


app = App()
app.update()
app.mainloop()

