# https://cs50.harvard.edu/python/2022/psets/8/jar/

from pytest import raises
from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(50)
    assert jar.capacity == 50


def test_deposit():
    jar = Jar()

    jar.deposit(2)
    assert jar.size == 2
    jar.deposit(10)
    assert jar.size == 12

    with raises(ValueError):
        jar.deposit(5)


def test_withdraw():
    jar = Jar()
    jar.deposit(12)

    jar.withdraw(6)
    assert jar.size == 6
    jar.withdraw(3)
    assert jar.size == 3

    with raises(ValueError):
        jar.withdraw(12)


def test_str():
    jar = Jar()

    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
