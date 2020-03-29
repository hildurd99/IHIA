from calculator import Calc

def test_add_empty_returns_zero() -> None:
    assert Calc.ADD("") == 0

def test_add_1_returns_1() -> None:
    assert Calc.ADD("1") == 1

def main():
    test_add_empty_returns_zero()
    test_add_1_returns_1()

main()