import pytest
import leapyear

def test_is_dividable_with_4_and_not_with_100():
    year = 2004
    assert leapyear.is_leap_year(year) == (year % 4 == 0) and (year % 100 != 0) == True

def test_is_dividable_with_400():
    year = 2000
    assert leapyear.is_leap_year(year) == (year % 400 == 0) == True

def test_is_not_dividable_with_4():
    year = 2023
    assert leapyear.is_leap_year(year) == (year % 4 == 0) == False

def test_is_dividable_with_100_but_not_400():
    year = 1800
    assert leapyear.is_leap_year(year) == (year % 100 != 0) and (year % 400 == 0) == False
