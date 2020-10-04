#!/usr/bin/env python3
from typing import List
import argparse


def check_fizz(n: int) -> str:
    return "fizz" if n % 3 == 0 else ""


def check_buzz(n: int) -> str:
    return "buzz" if n % 5 == 0 else ""


def check_fizzbuzz(n: int) -> str:
    x = check_fizz(n) + check_buzz(n)
    return str(n) if x == "" else x


def fizzbuzz(n: int) -> List[str]:
    return [check_fizzbuzz(i) for i in range(1, n + 1)]


def fizzbuzz_cli():
    fizzbuzz_parser = argparse.ArgumentParser(description="Fizzbuzz!!!")
    fizzbuzz_parser.add_argument('number', type=str, help="Input number to print up to")
    fizzbuzz_args = fizzbuzz_parser.parse_args()
    n = fizzbuzz_args.number
    print(fizzbuzz(int(n)))


def main():
    n = input("Please enter a number: ")
    print(fizzbuzz(int(n)))


if __name__ == "__main__":
    main()
