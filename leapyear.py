import pytest

def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False

print(f'1700 - {is_leap_year(1700)}')
print(f'1800 - {is_leap_year(1800)}')
print(f'1900 - {is_leap_year(1900)}')
print(f'2000 - {is_leap_year(2000)}')
print(f'2100 - {is_leap_year(2100)}')
print(f'2200 - {is_leap_year(2200)}')
print(f'2300 - {is_leap_year(2300)}')

