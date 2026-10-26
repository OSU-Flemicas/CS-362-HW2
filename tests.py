import unittest
from contrived_func import contrived_func

"""This file runs unit test for the contrived_func function
Assignment: HW2: Improving Coverage
Author: Flemicas
Date: 10/26/2026"""


class TestCase(unittest.TestCase):

    def test_Empty_String(self):
        """Verifies that empty strings return false
        Picked using error guessing"""
        cc: str = ""
        self.assertFalse(contrived_func(cc),
                         msg="Expected False, Actual True: Check for empty strings. Input({})".format(cc))


if __name__ == '__main__':
    unittest.main()
