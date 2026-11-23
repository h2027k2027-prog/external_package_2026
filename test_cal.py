import pytest
from cal import add, sub, mul, div

def add(a, b):
    assert add(10, 20) == 30

def sub(a, b):
    assert sub(20, 10) == 10

def mul(a, b):
    assert mul(10, 20) == 200

def div(a, b):
    assert div(20, 2) == 10