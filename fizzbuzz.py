#!/usr/bin/env python3
from typing import List
import argparse


def check_fizz(number: int) -> str:
    return "fizz" if number % 3 == 0 else ""


def check_buzz(number: int) -> str:
    return "buzz" if number % 5 == 0 else ""


def check_fizzbuzz(number: int) -> str:
    rtn_fizzbuzz = check_fizz(number) + check_buzz(number)
    return str(number) if rtn_fizzbuzz == "" else rtn_fizzbuzz


def fizzbuzz(number: int) -> List[str]:
    return [check_fizzbuzz(i) for i in range(1, number + 1)]


def fizzbuzz_cli():
    fizzbuzz_parser = argparse.ArgumentParser(description="Fizzbuzz!!!")
    fizzbuzz_parser.add_argument("number", type=str, help="Input number to print up to")
    fizzbuzz_args = fizzbuzz_parser.parse_args()
    number = fizzbuzz_args.number
    print(fizzbuzz(int(number)))


def main():
    number = input("Please enter a number: ")
    print(fizzbuzz(int(number)))


if __name__ == "__main__":
    main()
