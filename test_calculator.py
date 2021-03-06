from calculator import Calc

def test_add_empty_returns_zero() -> None:
    assert Calc.ADD("") == 0

def test_add_1_returns_1() -> None:
    assert Calc.ADD("1") == 1

def test_add_twonumbers_returns_sum() -> None:
    assert Calc.ADD("1,2") == 3

def test_add_morenumbers_returns_sum() -> None:
    assert Calc.ADD("1,2,3,4,5") == 15

def test_add_newline_returns_sum() -> None:
    assert Calc.ADD("1\n2,3") == 6

def test_add_greater1000_returns_sum() -> None:
    assert Calc.ADD("1001,2") == 2

def test_add_negative_returns_error() -> None:
    assert Calc.ADD("2,-4,3,-5") == "Negatives not allowed: -4,-5"

def main():
    test_add_empty_returns_zero()
    test_add_1_returns_1()
    test_add_twonumbers_returns_sum()
    test_add_morenumbers_returns_sum()
    test_add_newline_returns_sum()
    test_add_greater1000_returns_sum()
    test_add_negative_returns_error()

main()