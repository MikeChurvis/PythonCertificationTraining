"""
This is a game.

It has a 500 x 500 window that cannot be resized.

The window contains a single button labelled "Catch Me!".

Mousing over the button causes the button to jump to a different
location on the screen, such that the button's post-jump bounding
rectangle...

- is completely within the bounds of the window (the button is 100%
  visible).
- does not intersect the pre-jump bounding rectangle (the button
  is in a completely different place).

Clicking the button causes the player to win the game. In theory,
this should be impossible. Practically, this event branch must be
accounted for.
"""
import tkinter as tk
from random import choices, choice
from tkinter import messagebox


class ClickMeGame(tk.Tk):
    def __init__(self, width=500, height=500, jump_zone_visualizer_enabled=False):
        super().__init__()

        # Disable window resizing.
        self._width = width
        self._height = height
        self.geometry(f"{self._width}x{self._height}")
        self.resizable(False, False)

        self.jump_zone_visualizer_enabled = jump_zone_visualizer_enabled
        self.canvas = tk.Canvas(self, width=self._width, height=self._height)

        if self.jump_zone_visualizer_enabled:
            self.canvas.place(x=0, y=0)

        self.button = tk.Button(self, text="Catch Me!", command=self.trigger_player_win)
        self.button.place(x=0, y=0)

        self.button.bind("<Enter>", self.trigger_button_jump)

    def trigger_button_jump(self, event=None):
        btn_x, btn_y = self.button.winfo_x(), self.button.winfo_y()
        btn_w, btn_h = self.button.winfo_width(), self.button.winfo_height()
        max_x, max_y = self._width - btn_w, self._height - btn_h

        # The exclusion zone is the space where, if you moved the button there, it would touch its old footprint.
        exclusion_zone_top = btn_y - btn_h
        exclusion_zone_bottom = btn_y + btn_h
        exclusion_zone_left = btn_x - btn_w
        exclusion_zone_right = btn_x + btn_w

        # Valid space is anywhere you can move the button such that it:
        # - won't touch its old footprint,
        # - won't clip out of of the bounds of the window.
        # They are rectangles, defined here as tuple[x_range, y_range].
        valid_space_above = range(0, max_x), range(0, exclusion_zone_top)
        valid_space_below = range(0, max_x), range(exclusion_zone_bottom, max_y)
        valid_space_left = range(0, exclusion_zone_left), range(exclusion_zone_top, exclusion_zone_bottom)
        valid_space_right = range(exclusion_zone_right, max_x), range(exclusion_zone_top, exclusion_zone_bottom)

        valid_spaces = valid_space_above, valid_space_below, valid_space_left, valid_space_right
        valid_space_volumes = tuple(map(lambda box: len(box[0]) * len(box[1]), valid_spaces))

        # To pick a valid value, we must first pick a rectangle where that value can be.
        # The picker is random, but is weighted in favor of bigger rectangles,
        # as if it's throwing a dart at a piece of paper with different-sized squares on it.
        possible_xs, possible_ys = choices(valid_spaces, weights=valid_space_volumes)[0]

        new_x, new_y = choice(possible_xs), choice(possible_ys)

        self.button.place(x=new_x, y=new_y)

        # The section below drives the visualizer for the calculation performed above.
        if not self.jump_zone_visualizer_enabled:
            return

        # Clear the canvas.
        self.canvas.delete(*self.canvas.find_all())

        # Draw the old footprint.
        self.canvas.create_rectangle(btn_x, btn_y, btn_x + btn_w, btn_y + btn_h, outline='', fill='pink')

        # Outline the spaces where the new button can jump to. Ignore zero-volume areas.
        for range_x, range_y in valid_spaces:
            try:
                vis_min_x, vis_min_y, vis_max_x, vis_max_y = min(range_x), min(range_y), max(range_x), max(range_y)
            except ValueError:
                continue
            self.canvas.create_rectangle(vis_min_x, vis_min_y, vis_max_x, vis_max_y, width=1, outline='red')

        # Pinpoint the new location chosen by the calculation.
        self.canvas.create_line(new_x - 5, new_y, new_x + 5, new_y, fill='blue')
        self.canvas.create_line(new_x, new_y - 5, new_x, new_y + 5, fill='blue')


    def trigger_player_win(self):
        messagebox.showinfo('You... Won??', 'boris_the_animal_thats_not_possible.gif')
        self.destroy()


if __name__ == '__main__':
    def main():
        ClickMeGame(jump_zone_visualizer_enabled=True).mainloop()


    main()
