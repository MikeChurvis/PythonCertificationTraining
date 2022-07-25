from __future__ import annotations

import functools
import tkinter as tk
from tkinter.font import Font


class Calculator(tk.Tk):
    MAX_CHARACTERS = 10

    class Mode:
        LEFT_OPERAND = 0
        RIGHT_OPERAND = 1
        RESULT = 2

    class OperatorCode:
        NOT_SELECTED = -1
        ADDITION = 0
        SUBTRACTION = 1
        MULTIPLICATION = 2
        DIVISION = 3

    class OperandModifyError(ValueError):
        def __init__(self, reason: str):
            super().__init__(f"Cannot modify operand: {reason}")

    class EvaluationError(Exception):
        pass

    def __init__(self):
        super().__init__()

        # Instantiate observable data stores.

        self._mode = tk.IntVar(name="CalculatorVar_Mode")
        self._operator_code = tk.IntVar(name="CalculatorVar_OperatorCode")
        self._left_operand_variable = tk.StringVar(name="CalculatorVar_LeftOperand")
        self._right_operand_variable = tk.StringVar(name="CalculatorVar_RightOperand")
        self._result_variable = tk.StringVar(name="CalculatorVar_Result")

        # Instantiate widgets.

        self._display_entry = tk.Entry(self,
                                       justify="right",
                                       font=Font(family="Courier", size=16, weight="bold"),
                                       width=Calculator.MAX_CHARACTERS)

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

        self._addition_operator_button = tk.Button(
            self,
            text="+",
            width=2,
            command=self.command_factory__operator_button(Calculator.OperatorCode.ADDITION)
        )
        self._subtraction_operator_button = tk.Button(
            self,
            text="-",
            width=2,
            command=self.command_factory__operator_button(Calculator.OperatorCode.SUBTRACTION)
        )
        self._multiplication_operator_button = tk.Button(
            self,
            text="*",
            width=2,
            command=self.command_factory__operator_button(Calculator.OperatorCode.MULTIPLICATION)
        )
        self._division_operator_button = tk.Button(
            self,
            text="/",
            width=2,
            command=self.command_factory__operator_button(Calculator.OperatorCode.DIVISION)
        )

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

        # Initialize data store values by resetting the calculator.
        self.command__clear_button()

    @property
    def mode(self):
        return self._mode.get()

    @mode.setter
    def mode(self, new_mode: int):
        if new_mode == Calculator.Mode.LEFT_OPERAND:
            display_variable = self._left_operand_variable
        elif new_mode == Calculator.Mode.RIGHT_OPERAND:
            display_variable = self._right_operand_variable
        elif new_mode == Calculator.Mode.RESULT:
            display_variable = self._result_variable
        else:
            raise NotImplementedError(f"Attempted to set Calculator.mode to {new_mode}. "
                                      "There is no observable variable that corresponds to this mode.")

        self._display_entry.config(textvariable=display_variable)
        self._mode.set(new_mode)

    @property
    def operator_code(self):
        return self._operator_code.get()

    @operator_code.setter
    def operator_code(self, value):
        self._operator_code.set(value)

    @property
    def is_in_an_operand_mode(self):
        return self.mode in (Calculator.Mode.LEFT_OPERAND, Calculator.Mode.RIGHT_OPERAND)

    @property
    def current_operand_variable(self):
        if self.mode == Calculator.Mode.LEFT_OPERAND:
            current_operand = self._left_operand_variable
        elif self.mode == Calculator.Mode.RIGHT_OPERAND:
            current_operand = self._right_operand_variable
        else:
            raise ValueError(f"There is no current operand because the calculator is currently in mode {self.mode}, "
                             "which is not an operand mode.")

        return current_operand

    def clear_all(self):
        self.mode = Calculator.Mode.LEFT_OPERAND
        self.operator_code = Calculator.OperatorCode.NOT_SELECTED
        self._left_operand_variable.set("0")
        self._right_operand_variable.set("0")
        self._result_variable.set("")

    def append_character_to_current_operand(self, character: str):
        if not self.is_in_an_operand_mode:
            raise Calculator.OperandModifyError(f"Calculator is currently in mode {self.mode}, "
                                                "which is not an operand mode.")

        if len(character) > 1:
            raise Calculator.OperandModifyError("The given value is longer one character "
                                                f"(given value was '{character}')")

        if character not in "0123456789.":
            raise Calculator.OperandModifyError("The given character is not a digit or a decimal point "
                                                f"(given character was '{character}')")

        current_value = self.current_operand_variable.get()

        # Do not allow more than one decimal point character to be added.
        if "." in current_value and character == ".":
            return

        # If the only character is a 0, replace it with the new character.
        if current_value == "0":
            current_value = ""

        # Always reserve space for the sign character.
        if current_value.startswith("-"):
            max_length = Calculator.MAX_CHARACTERS
        else:
            max_length = Calculator.MAX_CHARACTERS - 1

        new_value = (current_value + character)[:max_length]
        self.current_operand_variable.set(new_value)

    def try_flip_sign_of_current_operand(self):
        if not self.is_in_an_operand_mode:
            raise Calculator.OperandModifyError(f"Calculator is currently in mode {self.mode}, "
                                                "which is not an operand mode.")

        operand_value = self.current_operand_variable.get()

        if operand_value.startswith("-"):
            operand_value = operand_value[1:]
        else:
            operand_value = "-" + operand_value

        assert len(operand_value) <= Calculator.MAX_CHARACTERS

        self.current_operand_variable.set(operand_value)

    def evaluate_operation_and_display_result(self):
        # If the calculator's already in result mode, nothing needs to be done.
        if self.mode != Calculator.Mode.RIGHT_OPERAND:
            raise ValueError(f"Cannot evaluate operation: The calculator is in mode {self.mode}. "
                             f"It must be in mode {Calculator.Mode.RIGHT_OPERAND} to evaluate its operation.")

        if self.operator_code == Calculator.OperatorCode.NOT_SELECTED:
            raise ValueError("Cannot evaluate operation: No operator selected.")

        left_operand = self._left_operand_variable.get()
        right_operand = self._right_operand_variable.get()
        operator_function = {
            Calculator.OperatorCode.ADDITION: lambda a, b: a + b,
            Calculator.OperatorCode.SUBTRACTION: lambda a, b: a - b,
            Calculator.OperatorCode.MULTIPLICATION: lambda a, b: a * b,
            Calculator.OperatorCode.DIVISION: lambda a, b: a / b
        }.get(self.operator_code)

        if operator_function is None:
            raise NotImplementedError(f"No corresponding function for operator code {self.operator_code}")

        cast_as_number = float if "." in left_operand else int
        left_operand = cast_as_number(left_operand)

        cast_as_number = float if "." in right_operand else int
        right_operand = cast_as_number(right_operand)

        try:
            raw_result = operator_function(left_operand, right_operand)

            # Cast to int whenever possible.
            if isinstance(raw_result, float) and raw_result.is_integer():
                raw_result = int(raw_result)

            result_string = str(raw_result)

            # Compute metrics on result string.
            result_is_integer = isinstance(raw_result, int)
            max_characters_allowed = Calculator.MAX_CHARACTERS - (0 if raw_result >= 0 else 1)

            if result_is_integer:
                if len(result_string) > max_characters_allowed:
                    raise Calculator.EvaluationError
            else:
                # Don't allow float representations that include non-numeric characters.
                # Example: the result is so large that Python tries to use scientific notation.
                result_string_contains_non_numeric_characters = any(
                    map(lambda c: c not in "0123456789.-", result_string))
                if result_string_contains_non_numeric_characters:
                    raise Calculator.EvaluationError

                # The specs say that any number of post-decimal digits can be truncated (dropped).
                # This means that only the part before the decimal matters.
                part_before_decimal, _ = result_string.split(".")
                if len(part_before_decimal) > max_characters_allowed:
                    raise Calculator.EvaluationError

                # Truncate as necessary.
                result_string = result_string[:max_characters_allowed]

                # Trim trailing decimal point.
                if result_string.endswith("."):
                    result_string = result_string[:-1]

        except (ArithmeticError, Calculator.EvaluationError):
            result_string = "Error!"

        self._result_variable.set(result_string)
        self.mode = Calculator.Mode.RESULT

    def command_factory__operator_button(self, operator_code: int):
        def command__operator_button():
            # Give the user a hint that they may want to clear the calculator.
            if self.mode == Calculator.Mode.RESULT:
                make_button_flash(self._clear_button)
                return

            self.operator_code = operator_code
            self.mode = Calculator.Mode.RIGHT_OPERAND

        return command__operator_button

    def command_factory__numpad_button(self, digit: int):
        def command__numpad_button():
            if not self.is_in_an_operand_mode:
                self.clear_all()
            self.append_character_to_current_operand(str(digit))

        return command__numpad_button

    def command__clear_button(self):
        self.clear_all()

    def command__decimal_point_button(self):
        if not self.is_in_an_operand_mode:
            self.clear_all()
        self.append_character_to_current_operand(".")

    def command__equals_button(self):
        # Give a visual indication that the operator has not been chosen yet.
        if self.mode == Calculator.Mode.LEFT_OPERAND:
            make_button_flash(self._addition_operator_button)
            make_button_flash(self._subtraction_operator_button)
            make_button_flash(self._multiplication_operator_button)
            make_button_flash(self._division_operator_button)
            return

        # Give the user a hint that they may want to clear the calculator.
        if self.mode == Calculator.Mode.RESULT:
            make_button_flash(self._clear_button)
            return

        self.evaluate_operation_and_display_result()

    def command__sign_flip_button(self):
        if not self.is_in_an_operand_mode:
            return

        self.try_flip_sign_of_current_operand()


def make_button_flash(button: tk.Button):
    previous_bg_color = button.cget('bg')
    new_bg_color = 'yellow'

    def reset_bg():
        button.config(bg=previous_bg_color)

    button.config(bg=new_bg_color)
    button.after(200, reset_bg)


if __name__ == '__main__':
    def main():
        Calculator().mainloop()


    main()
