import pytest
from inverse_factorial import inverse_factorial

def test_inverse_factorial():
    assert inverse_factorial.inverse_factorial(120) == '5!'

def test_inverse_factorial_2():
    assert inverse_factorial.inverse_factorial(150) == 'NONE'

def test_inverse_factorial_3():
    assert inverse_factorial.inverse_factorial(6) == '3!'

def test_inverse_factorial_4():
    assert inverse_factorial.inverse_factorial(10) == 'NONE'

def test_inverse_factorial_5():
    assert inverse_factorial.inverse_factorial(0) == 'NONE'

def test_inverse_factorial_6():
    assert inverse_factorial.inverse_factorial(-2) == 'NONE'

def test_inverse_factorial_7():
    assert inverse_factorial.inverse_factorial(1) == '0! OR 1!'

def test_inverse_factorial_8():
    assert inverse_factorial.inverse_factorial(1000000) == 'NONE'

def test_inverse_factorial_9():
    assert inverse_factorial.inverse_factorial(-3) == 'NONE'

def test_inverse_factorial_10():
    assert inverse_factorial.inverse_factorial(2) == '2!'

def test_inverse_factorial_11():
    assert inverse_factorial.inverse_factorial(3) == 'NONE'
