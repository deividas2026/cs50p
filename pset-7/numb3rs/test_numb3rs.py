from numb3rs import validate
import random


def test_first_byte():
    for i in range(256):
        assert validate(f"{i}.0.0.0") == True
        assert validate(f"{i}.255.255.255") == True
        assert validate(f"{i}.99.100.200") == True

    assert validate("-1.244.244.244") == False 
    assert validate("257.244.244.244") == False 
    assert validate("1000.244.244.244") == False 
    assert validate("01.244.244.244") == False 


def test_second_byte():
    for i in range(256):
        assert validate(f"0.{i}.0.0") == True
        assert validate(f"255.{i}.255.255") == True
        assert validate(f"99.{i}.100.200") == True

    assert validate("244.-1.244.244") == False 
    assert validate("244.257.244.244") == False 
    assert validate("244.1000.244.244") == False 
    assert validate("33.01.244.244") == False 
    

def test_last_byte():
    for i in range(256):
        assert validate(f"0.0.0.{i}") == True
        assert validate(f"43.12.255.{i}") == True
        assert validate(f"22.242.99.{i}") == True

    assert validate("244.244.244.00") == False 
    assert validate("244.244.244.09") == False 
    assert validate("244.244.244.999") == False 
    assert validate("33.244.244.-8") == False 


def test_valid_ips():
    for i in range(256):
        ip = f"{i}.{i}.{i}.{i}"
        assert validate(ip) == True
    

    for i in range(100):
        a = random.randint(0, 255)
        b = random.randint(0, 255)
        c = random.randint(0, 255)
        d = random.randint(0, 255)
        ip = f"{a}.{b}.{c}.{d}"
        assert validate(ip) == True
 

def test_random_valid_ips():
    for i in range(100):
        a = random.randint(0, 255)
        b = random.randint(0, 255)
        c = random.randint(0, 255)
        d = random.randint(0, 255)
        ip = f"{a}.{b}.{c}.{d}"
        assert validate(ip) == True


def test_invalid_ips():
    for i in range(1000):
        a = random.randint(256, 1000)
        b = random.randint(0, 255)
        c = random.randint(0, 255)
        d = random.randint(0, 255)
        ip = f"{a}.{b}.{c}.{d}"
        assert validate(ip) == False
 

    for i in range(1000):
        a = random.randint(0, 255)
        b = random.randint(0, 255)
        c = random.randint(0, 255)
        d = random.randint(500, 2000)
        ip = f"{a}.{b}.{c}.{d}"
        assert validate(ip) == False
 
    assert validate("12.12") == False
    assert validate("12...") == False
    assert validate("12..12.") == False
    assert validate("12...255") == False
    assert validate("0...255") == False
    assert validate("0..21.255") == False
    assert validate("0.33.21.256") == False
    assert validate("0.33.21.") == False
    assert validate("0.00.21.244") == False
    assert validate("") == False
    assert validate("....") == False
    assert validate("my ip is 0.0.0.0") == False
    assert validate(" 0.0.0.0") == False
    assert validate(" 1.1.1.1 ") == False
    assert validate("1.1.1.1 ") == False
    assert validate("12121212") == False














