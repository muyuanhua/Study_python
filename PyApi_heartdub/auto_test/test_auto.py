import pytest

def func(x):
    return x+1

def test_om():
    assert func(3) == 5
