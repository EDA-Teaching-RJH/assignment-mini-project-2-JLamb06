import pytest
from Part2 import divider

def test_divider():
    assert divider ("1/2") == 0.5
    assert divider ("3/4") == 0.75
    #Attempts to put in the value in the brackets into the divider definition and then if it doesnt work properly then it will return an error
    try:
        assert divider ("5/0")
    #This checks that the input above produces the correct error which in this case is a zero division error
    except ZeroDivisionError as exc:
        pytest.fail(exc, pytrace=True)
    #Attempts to put in the value in the brackets into the divider definition and then if it doesnt work properly then it will return an error
    try:
        assert divider ("6/5")
    #This checks that the input above produces the correct error which in this case is a value error
    except ValueError as exc:
        pytest.fail(exc, pytrace=True)
    #Puts in erroneous inputs from now on to check that all the errors have a desired outcome.
    try:
        assert divider ("king/2")
    except ValueError as exc:
        pytest.fail(exc, pytrace=True)
    try:
        assert divider ("6/Jack")
    except ValueError as exc:
        pytest.fail(exc, pytrace=True)
    try:
        assert divider ("")
    except ValueError as exc:
        pytest.fail(exc, pytrace=True)