import tkinter as tk

window = tk.Tk()

button_positions = (10, 10), (20, 40), (30, 70)

for button_id, position in enumerate(button_positions):
    x, y = position
    button = tk.Button(window, text=f"Button #{button_id + 1}")
    button.place(x=x, y=y)

window.mainloop()
