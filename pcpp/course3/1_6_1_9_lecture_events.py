import tkinter as tk
from tkinter import messagebox


class SwitchApp:
    def __init__(self):
        self.window = tk.Tk()
        self.switch_is_on = True
        self.button_1 = tk.Button(self.window, text="On/Off", command=self.on_off)
        self.button_2 = tk.Button(self.window, text="Peekaboo!", command=self.peekaboo)
        self.button_1.pack()
        self.button_2.pack()

    def run(self):
        self.window.mainloop()

    def on_off(self):
        self.switch_is_on = not self.switch_is_on

        if self.switch_is_on:
            self.button_2.config(command=self.peekaboo)
            self.button_2.config(text="Peekaboo!")
        else:
            self.button_2.config(command=self.do_nothing)
            self.button_2.config(text="Gee!")

    @staticmethod
    def peekaboo():
        messagebox.showinfo("", "PEEKABOO!")

    @staticmethod
    def do_nothing():
        pass


app = SwitchApp()
app.run()