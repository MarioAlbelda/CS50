from twttr import shorten

def test_shorten():
    assert shorten("David") == "Dvd"
    assert shorten("Hello people") == "Hll ppl"
    assert shorten("Alo") == "l"
    assert shorten("You are 3, right?") == "Y r 3, rght?"
