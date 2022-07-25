import tkinter as tk
from tkinter.font import Font
from enum import IntEnum


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        # Instantiate observable data stores.

        self._first_operand_variable = tk.StringVar(value="-876543210")
        self._second_operand_variable = tk.StringVar(value="0")
        self._result_variable = tk.StringVar()

        # Instantiate widgets.

        self._display_entry = tk.Entry(self,
                                       justify="right",
                                       font=Font(family="Courier", size=16, weight="bold"),
                                       width=10,
                                       textvariable=self._first_operand_variable)

        self._numpad_buttons = [
            tk.Button(self,
                      text=str(i),
                      width=2,
                      command=self.command_factory__numpad_button(i))
            for i in range(10)
        ]

        self._clear_button = tk.Button(self, text="C", width=2, command=self.command__clear_button)
        self._decimal_point_button = tk.Button(self, text=".", width=2, command=self.command__decimal_point_button)
        self._equals_button = tk.Button(self, text="=", width=3, command=self.command__equals_button)
        self._sign_flip_button = tk.Button(self, text="+/-", width=3, command=self.command__sign_flip_button)

        self._addition_operator_button = tk.Button(self,
                                                   text="+",
                                                   width=2,
                                                   command=self.command__addition_operator_button)
        self._subtraction_operator_button = tk.Button(self,
                                                      text="-",
                                                      width=2,
                                                      command=self.command__subtraction_operator_button)
        self._multiplication_operator_button = tk.Button(self,
                                                         text="*",
                                                         width=2,
                                                         command=self.command__multiplication_operator_button)
        self._division_operator_button = tk.Button(self,
                                                   text="/",
                                                   width=2,
                                                   command=self.command__division_operator_button)

        # Place widgets.

        self._display_entry.grid(row=0, columnspan=5)

        self._numpad_buttons[0].grid(row=4, column=0)
        self._numpad_buttons[1].grid(row=3, column=0)
        self._numpad_buttons[2].grid(row=3, column=1)
        self._numpad_buttons[3].grid(row=3, column=2)
        self._numpad_buttons[4].grid(row=2, column=0)
        self._numpad_buttons[5].grid(row=2, column=1)
        self._numpad_buttons[6].grid(row=2, column=2)
        self._numpad_buttons[7].grid(row=1, column=0)
        self._numpad_buttons[8].grid(row=1, column=1)
        self._numpad_buttons[9].grid(row=1, column=2)

        self._clear_button.grid(row=4, column=1)
        self._decimal_point_button.grid(row=4, column=2)
        self._equals_button.grid(row=3, column=3)
        self._sign_flip_button.grid(row=4, column=3)

        self._addition_operator_button.grid(row=1, column=4)
        self._subtraction_operator_button.grid(row=2, column=4)
        self._multiplication_operator_button.grid(row=3, column=4)
        self._division_operator_button.grid(row=4, column=4)

    def command_factory__numpad_button(self, digit: int):
        def command__numpad_button():
            pass

        return command__numpad_button

    def command__clear_button(self):
        pass

    def command__decimal_point_button(self):
        pass

    def command__equals_button(self):
        pass

    def command__sign_flip_button(self):
        pass

    def command__addition_operator_button(self):
        pass

    def command__subtraction_operator_button(self):
        pass

    def command__multiplication_operator_button(self):
        pass

    def command__division_operator_button(self):
        pass




if __name__ == '__main__':
    def main():
        Calculator().mainloop()


    main()
