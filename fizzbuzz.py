def check_fizz(n: int) -> str:
    return "fizz" if n % 3 == 0 else ""


def check_buzz(n: int) -> str:
    return "buzz" if n % 5 == 0 else ""


def check_fizzbuzz(n: int) -> str:
    x = check_fizz(n) + check_buzz(n)
    return str(n) if x == "" else x


def test_check_fizz():
    n = 3
    result = check_fizz(n)
    assert result == "fizz"


def test_check_buzz():
    n = 5
    result = check_buzz(n)
    assert result == "buzz"


def test_check_fizzbuzz():
    n = 15
    result = check_fizzbuzz(n)
    assert result == "fizzbuzz"


def test_check_fizzbuzz_001():
    """Given when n is NOT a multiple of 3 and 5"""
    n = 1
    result = check_fizzbuzz(n)
    assert result == "1"
