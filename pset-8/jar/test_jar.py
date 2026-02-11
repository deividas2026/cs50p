import pytest
from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    jar_2 = Jar(2)
    assert jar_2.capacity == 2
    assert jar_2.size == 0
    

def test_init_with_invalid_capacity():
    with pytest.raises(ValueError):
        jar = Jar(-1)
    with pytest.raises(ValueError):
        jar = Jar(0)


def test_capacity_lower_than_size():
    jar = Jar(10)
    jar.deposit(10)

    with pytest.raises(ValueError):
        jar.capacity = 5
    

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(10)
    jar.deposit(2)
    assert jar.size == 2
    jar.deposit(2)
    assert jar.size == 4
    jar.deposit(6)
    assert jar.size == 10

    with pytest.raises(ValueError):
        jar.deposit(2)


def test_withdraw():
    jar = Jar(10)
    jar.deposit(10)
    jar.withdraw(5)
    assert jar.size == 5
    jar.withdraw(5)
    assert jar.size == 0

    with pytest.raises(ValueError):
        jar.withdraw(2)








    
