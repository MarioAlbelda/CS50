import plates

def test_is_valid():
    assert plates.is_valid("CS50") == True
    assert plates.is_valid("C50") == False
    assert plates.is_valid("C") == False
    assert plates.is_valid("CS50505") == False
    assert plates.is_valid("CS50C5") == False
    assert plates.is_valid("CS05") == False
    assert plates.is_valid("CS !5,") == False
