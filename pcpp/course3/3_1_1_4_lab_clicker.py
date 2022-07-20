"""
This is a game.

It has a board of 25 buttons in a 5x5 grid.

Each button has a unique number from 1 to 999 inclusive.

Below the grid is a stopwatch. It counts up from zero at a rate
of one per seconds. It starts the moment the player clicks any
of the buttons. It stops when the game end event is triggered.
"""
import itertools
import random
import tkinter as tk
from tkinter import messagebox


class ClickerGameLogic:
    def __init__(self):
        self.numbers = sorted(random.sample(range(1, 1000), k=25))
        self.current_number_index = 0

    @property
    def current_number(self):
        return self.numbers[self.current_number_index]

    def set_next_number(self):
        self.current_number_index += 1

        if self.current_number_index >= len(self.numbers):
            raise StopIteration


class ClickerGame(tk.Tk):
    def __init__(self):
        super().__init__()

        self.stopwatch_var = tk.IntVar(self, 0)
        self.current_stopwatch_interval_event_id = None
        self.stopwatch_label = tk.Label(self, textvariable=self.stopwatch_var)
        self.stopwatch_label.grid(row=1)

        button_frame = tk.Frame(self)
        button_frame.grid(row=0)
        self.buttons = []
        for _ in range(25):
            button = tk.Button(button_frame, width=5)
            button.bind('<ButtonRelease>', self.on_button_pressed)
            self.buttons.append(button)

        self.game_logic = ClickerGameLogic()
        self.initialize_button_grid_from_game_logic()

        self.start_stopwatch()

    def restart_game(self):
        self.game_logic = ClickerGameLogic()
        self.initialize_button_grid_from_game_logic()
        self.stopwatch_var.set(0)
        self.start_stopwatch()

    def initialize_button_grid_from_game_logic(self):
        for i, datum in enumerate(zip(self.game_logic.numbers, random.sample(range(25), k=25))):
            number, position = datum
            button = self.buttons[i]
            button.config(state='normal', text=number)
            button.grid(row=position // 5, column=position % 5)

    def on_button_pressed(self, event: tk.Event):
        button: tk.Button = event.widget
        number = int(button.cget("text"))

        if number != self.game_logic.current_number:
            return

        button.config(state='disabled')

        try:
            self.game_logic.set_next_number()
        except StopIteration:
            self.stop_stopwatch()
            player_wants_another_game = messagebox.askyesno(
                "You win!", f"You beat the game in {self.stopwatch_var.get()} seconds. Play again?"
            )

            if player_wants_another_game:
                self.restart_game()
            else:
                self.destroy()

    def start_stopwatch(self):
        self.current_stopwatch_interval_event_id = self.stopwatch_label.after(1000, self.increment_stopwatch)

    def increment_stopwatch(self):
        self.stopwatch_var.set(self.stopwatch_var.get() + 1)
        self.current_stopwatch_interval_event_id = self.stopwatch_label.after(1000, self.increment_stopwatch)

    def stop_stopwatch(self):
        self.stopwatch_label.after_cancel(self.current_stopwatch_interval_event_id)


if __name__ == '__main__':
    def main():
        ClickerGame().mainloop()


    main()
