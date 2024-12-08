from um import count
import pytest

def test_counting():
    assert count("um") == 1
    assert count("um, thenaks, um...") == 2
    assert count("um?") == 1
    assert count("album?") == 0


def test_spaces():
    assert count(" um") == 1
    assert count("um ") == 1
    assert count(" um ") == 1


def test_case():
    assert count("UM") == 1
    assert count("Um") == 1
    assert count("uM") == 1
