from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar._capacity == 12
    assert jar._size == 0

    jar = Jar(10)
    assert jar._capacity == 10
    assert jar._size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(8)
    assert jar.size == 8
    with pytest.raises(ValueError) as excinfo:
        jar.deposit(5)
    assert str(excinfo.value) == "Cookie jar's capacity exceeded"
    with pytest.raises(ValueError) as excinfo:
        jar.deposit(-3)
    assert str(excinfo.value) == "Number of cookies to deposit must be a non-negative integer"


def test_withdraw():
    jar = Jar()
    jar.deposit(8)
    jar.withdraw(3)
    assert jar.size == 5
    with pytest.raises(ValueError) as excinfo:
        jar.withdraw(8)
    assert str(excinfo.value) == "There aren't that many cookies in the cookie jar"
    with pytest.raises(ValueError) as excinfo:
        jar.withdraw(-3)
    assert str(excinfo.value) == "Number of cookies to withdraw must be a non-negative integer"
