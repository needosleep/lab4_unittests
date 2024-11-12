import unittest
from main import *

class Tester(unittest.TestCase):
    def test_circle(self):
        res = Circle.area(5)
        self.assertEqual(res, math.pi * 5 ** 2)
    
    def test_rectangle(self):
        pass

    def test_square(self):
        pass
    
    def test_triangle(self):
        pass
