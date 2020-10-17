#!/usr/bin/env python3
""" Fizzbuzz extreme program (are you ready to see how much of a try hard I am)"""
from typing import List
import argparse
import logging

logging.basicConfig(
    filename="fizzbuzz.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
LOGGER = logging.getLogger(__file__)


def check_fizz(number: int) -> str:
    """If a integer is divisible by three function outputs fizz

    Args:
        number (int): integer to check if divisible by three

    Returns:
        str: returns fizz if divisible by three, else continues

    Examples:
        >>> check_fizz(3)
        'fizz'
        >>> check_fizz(5)
        ''
    """
    return "fizz" if number % 3 == 0 else ""


def check_buzz(number: int) -> str:
    """If a integer is divisible by five function outputs buzz

    Args:
        number (int): integer to check if divisible by five

    Returns:
        str: returns buzz if divisible by five, else continues

    Examples:
        >>> check_buzz(3)
        ''
        >>> check_buzz(5)
        'buzz'
    """
    return "buzz" if number % 5 == 0 else ""


def check_fizzbuzz(number: int) -> str:
    """If a integer is divisible by five and three function outputs fizzbuzz

    Args:
        number (int): integer to check if divisible by five and three

    Returns:
        str: returns fizzbuzz if divisible by five and three, else continues

    Examples:
        >>> check_fizzbuzz(3)
        'fizz'
        >>> check_fizzbuzz(5)
        'buzz'
        >>> check_fizzbuzz(15)
        'fizzbuzz'
        >>> check_fizzbuzz(1)
        '1'
    """
    rtn_fizzbuzz = check_fizz(number) + check_buzz(number)
    return str(number) if rtn_fizzbuzz == "" else rtn_fizzbuzz


def fizzbuzz(number: int) -> List[str]:
    """Program that takes a range of numbers from 1 to n. Checks if a number divisible by
    three are “Fizz”. Checks if number divisible by five are "Buzz". Check if numbers are
    divisible by both three and five are "Fizzbuzz". Else, the string of the integer is returned.

    Args:
        number (int): integer to generate numbers up to

    Returns:
        List[str]: Fizzbuzz results

    Examples:
        >>> fizzbuzz(15)  # doctest: +NORMALIZE_WHITESPACE
        ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz',
        'buzz', '11', 'fizz', '13', '14', 'fizzbuzz']
    """
    return [check_fizzbuzz(i) for i in range(1, number + 1)]


def fizzbuzz_cli():
    """ CLI for fizzbuzz"""
    fizzbuzz_parser = argparse.ArgumentParser(description="Fizzbuzz!!!")
    fizzbuzz_parser.add_argument("number", type=str, help="Input number to print up to")
    fizzbuzz_args = fizzbuzz_parser.parse_args()
    try:
        number = int(fizzbuzz_args.number)
    except ValueError:
        LOGGER.error("Input is not an integer!")
    else:
        print(fizzbuzz(number))


def main():
    """ Driver when running as script"""
    number = input("Please enter a number: ")
    print(fizzbuzz(int(number)))


if __name__ == "__main__":
    try:
        exit(main())
    except Exception as e:
        LOGGER.error("Oh No! Something went wrong with your script!")
        exit(1)

# errors to expect
# someone inputted a letter as an input/character that is not a number