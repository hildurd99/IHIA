from calculator import Calc

def test_add_empty_returns_zero() -> None:
    assert Calc.ADD("") == 0

def main():
    test_add_empty_returns_zero()


main()