import tkinter as tk


class CalculatorLogic:
    def __init__(self):
        self.first_operand = None
        self.second_operand = None
        self.operator = None

    @property
    def operator_fn(self):
        op_fns = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b
        }
        op_fn = op_fns.get(self.operator)

        if op_fn is None:
            raise ValueError(f"self.operator is invalid. Its value is {self.operator}. "
                             f"It must instead be one of these: {tuple(op_fns.keys())}")


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.logic = CalculatorLogic()
        self.display_field_value = tk.StringVar(self)
        self.display_field = tk.Entry(self, textvariable=self.display_field_value)

    def clear_all(self):
        pass

    def negate_current_operand(self):
        pass

    def commit_first_operand_and_select_operator(self, operator: str):
        pass

    def commit_second_operand_and_evaluate_operation(self):
        pass
