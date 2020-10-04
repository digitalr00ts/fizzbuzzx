from fizzbuzz import fizzbuzz, check_fizzbuzz, check_buzz, check_fizz


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


def test_fizzbuzz():
    n = 15
    result = fizzbuzz(n)
    assert result == ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7',
                      '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz']