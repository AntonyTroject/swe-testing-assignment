# Testing Strategy

I tested the main functionality of the calculator: basic arithmetic operations like addition, subtraction, multiplication, division.
Also  division by zero, working with negative numbers, decimals and very large values.
Reset State (Clear / C): Checked that the `clear()` method completely resets the current state of the calculator (input, stored value, selected operation and result).

Separately, I made integration tests for “as if the user enters commands” scenarios via the CLI:
- Full script: `5 + 3 =` should return `8`.
- After calculation, pressing `C` should reset the displayed result to `0`.
  
I didn’t test the interface since it wasn’t included in the assignment, and I didn’t test the security because it wasn’t needed for such a small, especially local project

# Lecture Concepts

## The Testing Pyramid
The project has more unit tests than integration tests. Unit tests are fast and cover most of the logic.
There are fewer integration tests because they check “end-to-end” scenarios that the components work together correctly.

## Black-box vs White-box
Unit tests are closer to white-box because I directly test internal functions (`add`, `div`) and internal state (`CalculatorState.clear()`).
Integration tests are closer to black-box, because I simulate user input through `run_session(...)` and only check the output,
without getting into the internal implementation.erformance, UX, stress tests) were deliberately not done due to the small scale of the task.

## Functional vs Non-Functional
The tests in the project are mainly functional: they check the correctness of calculations and the correctness of Clear/divide by zero behavior.
Non-functional tests (performance, UX, stress tests) were deliberately not done due to the small scale of the task.

# Test Results Summary

| Test name                                   | Type         | Status |
|---------------------------------------------|--------------|--------|
| test_addition_basic                         | Unit         | Pass   |
| test_subtraction_basic                      | Unit         | Pass   |
| test_multiplication_basic                   | Unit         | Pass   |
| test_division_basic                         | Unit         | Pass   |
| test_division_by_zero_raises                | Unit         | Pass   |
| test_negative_numbers                       | Unit         | Pass   |
| test_decimal_numbers                        | Unit         | Pass   |
| test_very_large_numbers                     | Unit         | Pass   |
| test_clear_resets_state                     | Unit         | Pass   |
| test_full_user_interaction_addition         | Integration  | Pass   |
| test_clear_after_calculation_resets_display | Integration  | Pass   |

