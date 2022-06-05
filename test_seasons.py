# https://cs50.harvard.edu/python/2022/psets/8/seasons/

from seasons import Number


def test_valid_numbers():
    assert Number.to_word(1) == "one"
    assert Number.to_word(2) == "two"
    assert Number.to_word(3) == "three"
    assert Number.to_word(123) == "one hundred twenty-three"
    assert Number.to_word(456789) == "four hundred fifty-six thousand, seven hundred eighty-nine"
