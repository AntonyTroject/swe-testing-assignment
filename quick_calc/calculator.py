from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


class DivisionByZeroError(ValueError):
    """Raised when attempting to divide by zero."""


def add(a: float, b: float) -> float:
    return a + b


def sub(a: float, b: float) -> float:
    return a - b


def mul(a: float, b: float) -> float:
    return a * b


def div(a: float, b: float) -> float:
    if b == 0:
        raise DivisionByZeroError("Cannot divide by zero.")
    return a / b


@dataclass
class CalculatorState:
    current_input: str = ""
    stored_value: float = 0.0
    pending_op: Optional[str] = None  # "+", "-", "*", "/" or None
    result: float = 0.0

    def clear(self) -> None:
        self.current_input = ""
        self.stored_value = 0.0
        self.pending_op = None
        self.result = 0.0

    def set_number(self, token: str) -> None:
        # token is validated outside
        self.current_input = token

    def set_op(self, op: str) -> None:
        # If there is a pending op and we have a new number, compute first (chained ops)
        if self.pending_op is not None and self.current_input != "":
            self.equals()
            self.pending_op = op
            return

        # Move current input into stored_value (if present)
        if self.current_input != "":
            self.stored_value = float(self.current_input)
            self.current_input = ""

        self.pending_op = op

    def equals(self) -> float:
        if self.pending_op is None:
            if self.current_input != "":
                self.result = float(self.current_input)
            return self.result

        a = self.stored_value
        b = float(self.current_input) if self.current_input != "" else 0.0

        if self.pending_op == "+":
            self.result = add(a, b)
        elif self.pending_op == "-":
            self.result = sub(a, b)
        elif self.pending_op == "*":
            self.result = mul(a, b)
        elif self.pending_op == "/":
            self.result = div(a, b)
        else:
            raise ValueError(f"Unknown operation: {self.pending_op}")

        # After equals: store result, reset operation, clear input
        self.stored_value = self.result
        self.pending_op = None
        self.current_input = ""
        return self.result