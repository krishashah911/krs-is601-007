""" Demonstrates test cases applied to a program in another file 
Remember for pytest the test file must be name test_*.py or *_test.py and
the test cases must be name def test_*():
"""

"""
UCID: krs
Date: 10/12/23
"""
import pytest
from MyCalc import Calc
c = Calc()

def test_add():
    c.add(2,5)
    assert c.ans == 7

def test_neg_add():
    c.add(3,3)
    assert c.ans != 5

def test_sub():
    c.sub(2,2)
    assert c.ans == 0

def test_neg_sub():
    c.sub(2,2)
    assert c.ans != 1

def test_mult():
    c.mult(2,2)
    assert c.ans == 4

def test_neg_mult():
    c.mult(4,0)
    assert c.ans != 4

def test_div():
    c.div(1,1)
    assert c.ans == 1

def test_neg_div():
    c.div(1,0)
    assert c.ans != 1

def test_div_by_zero():
    try:
        c.div(1,0)
        assert False
    except:
        assert True

def test_ans_add(prev=5):
    c.ans = prev
    c.add(c.ans, 3)  
    assert c.ans == 8

def test_ans_sub(prev=5):
    c.ans = prev
    c.sub(c.ans, 3) 
    assert c.ans == 2

def test_ans_mult(prev=10):
    c.ans = prev
    c.mult(c.ans, 3) 
    assert c.ans == 30


@pytest.fixture
def calculator_with_answer():
    calculator = Calc()
    calculator.ans = 15  # Set an initial answer (prev) for testing
    return calculator

def test_ans_div(calculator_with_answer):
    # The fixture provides a calculator instance with ans set to 15
    calculator_with_answer.div(calculator_with_answer.ans, 3)
    assert calculator_with_answer.ans == 5