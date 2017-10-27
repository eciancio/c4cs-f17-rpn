import unittest

import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rnp.calculate('1 1 + ')
        self.assertEqual(2, result)
    
