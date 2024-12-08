from seasons import minutes
import pytest

def test_counting():
    assert minutes("2023-08-07") == "Five hundred twenty-seven thousand forty"
    assert minutes("2022-08-07") == "One million, fifty-two thousand, six hundred forty"


def test_errors():
    with pytest.raises(SystemExit) as excinfo:
        minutes("January 1, 999")
    assert str(excinfo.value) == "Invalid date"
