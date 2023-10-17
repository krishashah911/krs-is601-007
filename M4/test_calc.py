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

def test_add():             # Takes 2 and 5 as float values and sums up to assert the value is 7
    c.add(2,5)
    assert c.ans == 7

def test_neg_add():         # Takes 3 and 3 as float values and sums up to assert the value is not 5.
    c.add(3,3)
    assert c.ans != 5

"""
UCID: krs
Date: 10/12/23
"""
def test_sub():             # Takes 2 and 2 as float values and subtracts to assert the value is 0
    c.sub(2,2)
    assert c.ans == 0

def test_neg_sub():         # Takes 2 and 2 as float values and subtracts to assert the value is not 1
    c.sub(2,2)
    assert c.ans != 1

"""
UCID: krs
Date: 10/12/23
"""
def test_mult():            # Takes 2 and 2 as float values and multiplies to assert the value is 4
    c.mult(2,2)
    assert c.ans == 4

def test_neg_mult():        # Takes 4 and 0 as float values and multiplies to assert the value is not 4
    c.mult(4,0)
    assert c.ans != 4

"""
UCID: krs
Date: 10/12/23
"""
def test_div():             # Takes 1 and 1 as float values and divides to assert the value is 1
    c.div(1,1)
    assert c.ans == 1

def test_neg_div():         # Takes 1 and 0 as float values and divides to assert the value is not 1
    c.div(1,0)
    assert c.ans != 1

def test_div_by_zero():     # Asserts that denominator cannot be zero
    try:
        c.div(1,0)
        assert False
    except:
        assert True

"""
UCID: krs
Date: 10/12/23
"""
def test_ans_add(prev=5):       # Takes previous answer as 5 and 3 to sum up to assert the value is 8.
    c.ans = prev
    c.add(c.ans, 3)  
    assert c.ans == 8

"""
UCID: krs
Date: 10/12/23
"""
def test_ans_sub(prev=5):       # Takes previous answer as 5 and 3 to subtract to assert the value is 2
    c.ans = prev
    c.sub(c.ans, 3) 
    assert c.ans == 2

"""
UCID: krs
Date: 10/12/23
"""
def test_ans_mult(prev=10):     # Takes previous answer as 10 and 3 to multiply to assert the value is 2
    c.ans = prev
    c.mult(c.ans, 3) 
    assert c.ans == 30


"""
UCID: krs
Date: 10/12/23
"""
@pytest.fixture
def calculator_with_answer():
    calculator = Calc()
    calculator.ans = 15                         # Set an initial answer (prev) for testing
    return calculator

def test_ans_div(calculator_with_answer):       # The fixture provides a calculator instance with ans set to 15
    calculator_with_answer.div(calculator_with_answer.ans, 3)
    assert calculator_with_answer.ans == 5      # Takes previous answer 15 and divides 3 to assert the value is 5