from um import count
import pytest

def test_single_um():
    assert count("hello, um, world") == 1

def test_multiple_um():
    assert count("um, um, UM, uM") == 4

def test_no_um():
    assert count("yummy umbrella") == 0

def test_case_insensitive():
    assert count("Um, excuse me, UM...") == 2

def test_boundaries():
    assert count("um? yummy um!") == 2