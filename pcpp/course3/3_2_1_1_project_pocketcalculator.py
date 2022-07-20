from enum import IntEnum
from typing import Callable


class Operator(IntEnum):
    ADD = 0
    SUBTRACT = 1
    MULTIPLY = 2
    DIVIDE = 3


class DisplayFieldMode(IntEnum):
    LEFT_OPERAND = 0
    RIGHT_OPERAND = 1
    OPERATION_RESULT = 2


class CalculatorLogic:
    def __init__(self):
        self._display_field = ''
        self.display_field_mode = DisplayFieldMode.LEFT_OPERAND
        self.selected_operator = None
        self.operand_left = None
        self.operand_right = None
        self.operation_result = None

    @property
    def display_field(self):
        return self._display_field

    @display_field.setter
    def display_field(self, value):
        value = self._clean_display_field_value(value)
        self._display_field = value
        self.compute_display_field_reactive_properties()
        self.dispatch_event('display_field.change')

    def _clean_display_field_value(self, value):
        pass

    def append_digit_to_current_operand(self, digit: int):
        pass

    def append_decimal_to_current_operand(self):
        pass

    def evaluate_operation(self):
        pass

    def clear_all(self):
        self.display_field = ''
        self.display_field_mode = DisplayFieldMode.LEFT_OPERAND
        self.selected_operator = None
        self.operand_left = None
        self.operand_right = None
        self.operation_result = None

    def negate_current_operand(self):
        pass

    def select_operator(self, operator: Operator):
        pass

    def on_display_field_change(self):
        pass

    def compute_display_field_reactive_properties(self):
        pass

    def dispatch_event(self, event_name: str, payload: dict | None = None):
        pass
