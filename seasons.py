# https://cs50.harvard.edu/python/2022/psets/8/seasons/

from math import log10, trunc
from datetime import date
from re import fullmatch
from sys import exit


class Number:
    _ones = {
        0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
        5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
        10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
        15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
    }
    _tens = {
        2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty',
        6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'
    }
    _illions = {
        1: 'thousand', 2: 'million', 3: 'billion'
    }

    @classmethod
    def to_word(cls, number):
        places = cls._split_number(number)
        length = len(places)

        output = ""

        for idx, num in enumerate(places):
            hundreds = num // 100
            tens = num % 100

            if hundreds:
                output += f"{cls._ones[hundreds]} hundred "

            if tens:
                if 0 <= tens < 20:
                    output += f"{cls._ones[tens]} "
                else:
                    output += f"{cls._tens[cls._get_digit(tens, 1)]}"

                    if tens % 10 != 0:
                        output += f"-{cls._ones[cls._get_digit(tens, 0)]} "

            if idx + 1 != length:
                output += f"{cls._illions[length - idx - 1]}, "

        return output.rstrip()

    @classmethod
    def _split_number(cls, number):
        digits = []

        for i in range(0, trunc(log10(number) + 1), 3):
            num = 0

            for j in range(0, 3):
                n = cls._get_digit(number, i + j)
                num += n * 10 ** j

            digits.insert(0, num)

        return tuple(digits)

    @classmethod
    def _get_digit(cls, number, nth_digit):
        return (number % 10 ** (nth_digit + 1) - number % 10 ** nth_digit) // 10 ** nth_digit


def main():
    birth = input("Date of birth: ")

    if not fullmatch(r"([0-9]{4})-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])", birth):
        exit("Invalid date format")

    birthdate = date.fromisoformat(birth)
    timespan = date.today() - birthdate
    minutes = round(timespan.total_seconds() / 60)

    print(f"{Number.to_word(minutes)} minutes".capitalize())


if __name__ == "__main__":
    main()
