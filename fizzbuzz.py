def check_fizz(n: int) -> str:
    return "fizz" if n % 3 == 0 else ""


def check_buzz(n: int) -> str:
    return "buzz" if n % 5 == 0 else ""

# def test_check_number(n: int):
#     n = 1
#     result = fizzbuzz(n)
#     assert result == "1"


def test_check_fizz():
    n = 3
    result = check_fizz(n)
    assert result == "fizz"


def test_check_buzz():
    n = 5
    result = check_buzz(n)
    assert result == "buzz"
