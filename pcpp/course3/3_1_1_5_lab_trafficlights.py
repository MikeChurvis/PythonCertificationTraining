"""
This is a simulator of british-style traffic lights.

It has a canvas upon which is rendered a visualization of a traffic
light.

It has a 'next' button which when clicked will cycle the traffic
light to its next state.

It has a 'quit' button which when clicked will immediately exit
the application.
"""
import itertools
import tkinter as tk

TRAFFIC_LIGHT_PHASES = (
    (True, False, False),
    (True, True, False),
    (False, False, True),
    (False, True, False)
)


class TrafficLightSimulator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.traffic_light_phase_cycler = itertools.cycle(TRAFFIC_LIGHT_PHASES)

        self.red_light_state = tk.BooleanVar()
        self.red_light_state.trace('w', self.on_red_light_state_change)
        self.yellow_light_state = tk.BooleanVar()
        self.yellow_light_state.trace('w', self.on_yellow_light_state_change)
        self.green_light_state = tk.BooleanVar()
        self.green_light_state.trace('w', self.on_green_light_state_change)

        self.canvas = tk.Canvas(self, width=100, height=280, bg='#555555')
        self.canvas.grid(row=0)
        self.red_light_visual_id = None
        self.yellow_light_visual_id = None
        self.green_light_visual_id = None

        next_button = tk.Button(self, text="Next", command=self.switch_to_next_traffic_light_phase)
        next_button.grid(row=1)

        quit_button = tk.Button(self, text="Quit", command=self.destroy)
        quit_button.grid(row=2)

        self.switch_to_next_traffic_light_phase()

    def draw_red_light_visual(self):
        is_on = self.red_light_state.get()
        self.canvas.delete(self.red_light_visual_id)
        self.red_light_visual_id = self.canvas.create_oval(
            10, 10, 90, 90,
            fill='red' if is_on else ''
        )

    def draw_yellow_light_visual(self):
        is_on = self.yellow_light_state.get()
        self.canvas.delete(self.yellow_light_visual_id)
        self.yellow_light_visual_id = self.canvas.create_oval(
            10, 100, 90, 180,
            fill='yellow' if is_on else ''
        )

    def draw_green_light_visual(self):
        is_on = self.green_light_state.get()
        self.canvas.delete(self.green_light_visual_id)
        self.green_light_visual_id = self.canvas.create_oval(
            10, 190, 90, 270,
            fill='green' if is_on else ''
        )

    def switch_to_next_traffic_light_phase(self):
        self.set_traffic_light_state(*next(self.traffic_light_phase_cycler))

    def set_traffic_light_state(self, red_state: bool, yellow_state: bool, green_state: bool):
        self.red_light_state.set(red_state)
        self.yellow_light_state.set(yellow_state)
        self.green_light_state.set(green_state)

    def on_red_light_state_change(self, *args):
        self.draw_red_light_visual()

    def on_yellow_light_state_change(self, *args):
        self.draw_yellow_light_visual()

    def on_green_light_state_change(self, *args):
        self.draw_green_light_visual()


if __name__ == '__main__':
    def main():
        TrafficLightSimulator().mainloop()


    main()
