from numb3rs import validate

def test_validate_numbers():
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("1.260.300.278") == False
    assert validate("256.255.255.255") == False

def test_validate_words():
    assert validate("cat") == False
