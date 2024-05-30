from lib.age_checker import *


def test_valid_dob():
    assert age_checker('2000-11-30')=='Access granted!'


def test_invalid_dob():
    assert age_checker('2020-11-30')=='Access denied, you are 3 and you need to be 16'


def test_invalid_entry():
    assert age_checker('2023-311-230')=='The date of birth is not in the right format'


