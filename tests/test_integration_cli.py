from quick_calc.cli import run_session


def test_full_user_interaction_addition():
    # enter 5, press +, enter 3, press = -> 8
    outputs = run_session(["5", "+", "3", "="])
    assert outputs == ["8"]


def test_clear_after_calculation_resets_display():
    outputs = run_session(["5", "+", "3", "=", "C"])
    # '=' outputs 8, then 'C' outputs 0
    assert outputs == ["8", "0"]