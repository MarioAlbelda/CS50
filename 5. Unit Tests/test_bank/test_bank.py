from bank import value

def test_value():
    assert value("Hello") == 0
    assert value("Hey, man") == 20
    assert value("What's up?") == 100
    assert value("hey, dude") == 20
