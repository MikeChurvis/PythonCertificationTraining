import tkinter as tk
from tkinter import messagebox


def question():
    answer = messagebox.askyesno("?", "To be or not to be?")
    print(answer)


window = tk.Tk()
button = tk.Button(window, text="Ask the question!", command=question)
button.pack()
window.mainloop()
