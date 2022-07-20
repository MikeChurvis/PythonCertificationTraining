"""
This is a calculator.

It has two fields, one for each operand of a binary operation.

It has an operation type selector in the form of a radio button.
This selector is positioned in between the two operand fields.

It has an 'evaluate' button that, when pressed, launches the Results
Modal.

The Results Modal describes the operation performed and its result.
- On error, the Results Modal displays the nature of the invalidity.

The user may choose from one of four operand types:

- Addition
- Subtraction
- Multiplication
- Division
"""

import tkinter as tk
from tkinter import messagebox


class BadInput(Exception):
    def __init__(self, reason):
        self.reason = reason


class SimpleCalculatorApp(tk.Tk):
    operators = {
        '+': ('plus', lambda a, b: a + b),
        '-': ('minus', lambda a, b: a - b),
        '*': ('times', lambda a, b: a * b),
        '/': ('divided by', lambda a, b: a / b)
    }

    def __init__(self):
        super().__init__()

        # Initialize backing values.
        self._left_operand = tk.StringVar(self)
        self._right_operand = tk.StringVar(self)
        self.selected_operator = tk.StringVar(self, list(self.operators)[0])

        # Initialize UI widgets.
        left_operand_field = tk.Entry(self, textvariable=self._left_operand)
        right_operand_field = tk.Entry(self, textvariable=self._right_operand)
        evaluate_button = tk.Button(self, text="Evaluate", command=self.evaluate_operation)
        operator_choices_frame = tk.Frame(self)
        operator_choices = [
            tk.Radiobutton(operator_choices_frame,
                           text=operator,
                           variable=self.selected_operator,
                           value=operator)
            for operator in self.operators
        ]

        # Place UI widgets.
        left_operand_field.grid(row=0, column=0)
        operator_choices_frame.grid(row=0, column=1)
        for op_choice in operator_choices:
            op_choice.pack()
        right_operand_field.grid(row=0, column=2)
        evaluate_button.grid(row=1, columnspan=3)

    @property
    def left_operand(self):
        left_operand_field = self._left_operand.get()

        try:
            if left_operand_field.isdigit():
                left_operand = int(left_operand_field)
            else:
                left_operand = float(left_operand_field)
        except ValueError:
            raise BadInput('Left operand is not a valid number.')

        return left_operand

    @property
    def right_operand(self):
        right_operand_field = self._right_operand.get()

        try:
            if right_operand_field.isdigit():
                right_operand = int(right_operand_field)
            else:
                right_operand = float(right_operand_field)
        except ValueError:
            raise BadInput('Right operand is not a valid number.')

        return right_operand

    def evaluate_operation(self):
        try:
            op_verb, op_func = self.operators[self.selected_operator.get()]

            result_value = op_func(self.left_operand, self.right_operand)
            result_string = f"{self.left_operand} {op_verb} {self.right_operand} is {result_value}"

            messagebox.showinfo("Operation Result:", result_string)
        except BadInput as error:
            messagebox.showerror('Input Error', error.reason)
        except ZeroDivisionError:
            messagebox.showerror('Zero Division Error', 'Cannot divide by zero.')
        except ArithmeticError as error:
            messagebox.showerror('Arithmetic Error', str(error))


if __name__ == '__main__':
    def main():
        SimpleCalculatorApp().mainloop()


    main()
