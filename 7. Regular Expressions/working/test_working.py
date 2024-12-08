from working import convert
import pytest

def test_convert_complex():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_convert_simple():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_convert_mix():
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"


def test_convert_VE():
    with pytest.raises(ValueError):
        convert("9:00 AM 5 PM")
    with pytest.raises(ValueError):
        convert("13 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:74 AM to 5:00 PM")
