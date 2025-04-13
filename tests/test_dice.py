
from src.dice import *


def test_d6_rolling():
    """
    Test 100 dice rolls and confirm
    they are between 1 and 6 
    """
    for _ in range(100):
        roll = roll_d6()
        assert (roll >= 1 and roll <= 6), "Dice roll did not match a D6"

def test_d3_rolling():
    """
    """
    for _ in range(100):
        roll = roll_d3()
        assert (roll >= 1 and roll <= 3), "Dice roll did not match a D3"
