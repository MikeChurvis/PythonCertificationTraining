from tkinter import Tk, messagebox, Button


def click():
    reply = messagebox.askquestion("Quit?", "Are you sure?")

    if reply == 'yes':
        skylight.destroy()


skylight = Tk()
skylight.title("Skylight")
button = Button(skylight, text="Bye!", command=click)
button.place(x=10, y=10)
skylight.mainloop()
