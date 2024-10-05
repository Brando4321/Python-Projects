
# Make sure it catches the valueError
# Make a file to run the test using the assert key
from app import calc_numbers

# Test if it accepts integer
def test_calc_numbers():
    assert calc_numbers()== int()

