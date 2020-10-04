"""Test file for fizzbuzz"""
from fizzbuzz import fizzbuzz, check_fizzbuzz, check_buzz, check_fizz


def test_check_fizz():
    """ Checks if check_fizz returns fizz if the number is divisible by three"""
    number = 3
    result = check_fizz(number)
    assert result == "fizz"


def test_check_buzz():
    """ Checks if check_buzz returns buzz if the number is divisible by five"""
    number = 5
    result = check_buzz(number)
    assert result == "buzz"


def test_check_fizzbuzz():
    """ Checks if check_fizzbuzz returns fizzbuzz if the number is divisible by five and three"""
    number = 15
    result = check_fizzbuzz(number)
    assert result == "fizzbuzz"


def test_check_fizzbuzz_001():
    """ Given when number is NOT a multiple of 3 and 5"""
    number = 1
    result = check_fizzbuzz(number)
    assert result == "1"


def test_fizzbuzz():
    """ Checks if program works when given an integer and generates a list of str"""
    number = 15
    result = fizzbuzz(number)
    assert result == [
        "1",
        "2",
        "fizz",
        "4",
        "buzz",
        "fizz",
        "7",
        "8",
        "fizz",
        "buzz",
        "11",
        "fizz",
        "13",
        "14",
        "fizzbuzz",
    ]
