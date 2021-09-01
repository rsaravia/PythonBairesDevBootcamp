# Create a unit testing to extensively test all possibilities of the function
# created in the regex exercise above.
import unittest
from ejercicio1 import match_pattern

import re

class TestMatch_Pattern(unittest.TestCase):
    def test_match_pattern(self):
        # Test matching
        self.assertAlmostEqual(match_pattern("[a-z]+_[a-z]+",
                                             'a-b-c123456789a-b-c1236123465aad_eeee1232134565aaa_bbfff125444i_iii123456'),
                              ['aad_eeee', 'aaa_bbfff', 'i_iii'])
"""
    def test_values(self):
        # Make sure value errors are raised when necessary
        self.assertRaises(ValueError, match_pattern, "[a-z]+_[a-z]+",
                                             'a-b-c123456789a-b-c1236123465aad_eeee1232134565aaa_bbfff125444i_iii123456')
"""

# go to "terminal" an excecute
#>> python -m unittest ejercicio2


# For more information about a Assert Function
# go to "Python Console" and type:
# >>> import unittest
# >>> help(unittest.TestCase.assertAlmostEqual)
