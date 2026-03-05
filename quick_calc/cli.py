from __future__ import annotations

from typing import Iterable, List, Optional

from quick_calc.calculator import CalculatorState, DivisionByZeroError

HELP_TEXT = """Quick-Calc (CLI)
Enter tokens separated by spaces.
Supported tokens:
  numbers (e.g., 5, -3, 2.5)
  +  -  *  /
  =        (calculate)
  C        (clear)
  q        (quit)

Examples:
  5 + 3 =
  10 / 2 =
  10 / 0 =
"""


def _format_number(x: float) -> str:
    if float(x).is_integer():
        return str(int(x))
    return str(x)


def _handle_token(state: CalculatorState, token: str) -> Optional[str]:
    token = token.strip()

    if token.lower() == "q":
        return "QUIT"

    if token.upper() == "C":
        state.clear()
        return "0"

    if token in {"+", "-", "*", "/"}:
        state.set_op(token)
        return None

    if token == "=":
        try:
            res = state.equals()
            return _format_number(res)
        except DivisionByZeroError:
            state.clear()
            return "Error: Division by zero"

    # number token
    try:
        float(token)
    except ValueError:
        return f"Error: Invalid token '{token}'"

    state.set_number(token)
    return None


def run_session(tokens: Iterable[str]) -> List[str]:
    """
    Integration-testable runner.
    Returns outputs produced by '=', 'C', and error messages.
    """
    state = CalculatorState()
    outputs: List[str] = []
    for t in tokens:
        out = _handle_token(state, t)
        if out == "QUIT":
            break
        if out is not None:
            outputs.append(out)
    return outputs


def main() -> None:
    print(HELP_TEXT)
    state = CalculatorState()

    while True:
        line = input("> ").strip()
        if not line:
            continue

        for token in line.split():
            out = _handle_token(state, token)
            if out == "QUIT":
                print("Bye.")
                return
            if out is not None:
                print(out)


if __name__ == "__main__":
    main()