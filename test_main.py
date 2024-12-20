import unittest
import math
import main

class Tester(unittest.TestCase):

    def test_circle(self):
        r1, r2, r3 = 3, 0, -5
        r4, r5, r6 = '5', (3, 4), complex(5, 1)

        self.assertEqual(main.Circle.area(r1), math.pi * 9)
        self.assertEqual(main.Circle.perimeter(r1), math.pi * 6)

        with self.assertRaises(ValueError):
            main.Circle.area(r2)
            main.Circle.area(r3)

        with self.assertRaises(ValueError):
            main.Circle.perimeter(r2)
            main.Circle.perimeter(r3)
        
        with self.assertRaises(TypeError):
            main.Circle.area(r4)
            main.Circle.area(r5)
            main.Circle.area(r6)
        
        with self.assertRaises(TypeError):
            main.Circle.perimeter(r4)
            main.Circle.perimeter(r5)
            main.Circle.perimeter(r6)
        
        return
    
    def test_rectangle(self):
        a1, b1 = 3, 4
        a2, b2 = 6, -2
        a3, b3 = -9, 2
        a4, b4 = 0, -10
        a5, b5 = -2, -2
        a6, b6 = 2.5, 3.0
        a7, b7 = "3", 8
        a8, b8 = (1.2,), "9"

        self.assertEqual(main.Rectangle.area(a1, b1), 12)
        self.assertEqual(main.Rectangle.perimeter(a1, b1), 14)
        
        self.assertEqual(main.Rectangle.area(a6, b6), 7.5)
        self.assertEqual(main.Rectangle.perimeter(a6, b6), 11.0)

        with self.assertRaises(ValueError):
            main.Rectangle.area(a2, b2)
            main.Rectangle.area(a3, b3)
            main.Rectangle.area(a4, b4)
            main.Rectangle.area(a5, b5)

        with self.assertRaises(ValueError):
            main.Rectangle.perimeter(a2, b2)
            main.Rectangle.perimeter(a3, b3)
            main.Rectangle.perimeter(a4, b4)
            main.Rectangle.perimeter(a5, b5)

        with self.assertRaises(TypeError):
            main.Rectangle.area(a7, b7)
            main.Rectangle.area(a8, b8)
        
        with self.assertRaises(TypeError):
            main.Rectangle.perimeter(a7, b7)
            main.Rectangle.perimeter(a8, b8)

        return

    def test_square(self):
        a1, a2, a3 = 1.5, 0, -1
        a4, a5 = complex(5, 0), list()

        self.assertEqual(main.Square.area(a1), 2.25)
        self.assertRaises(ValueError, main.Square.area, a2)
        self.assertRaises(ValueError, main.Square.perimeter, a2)
        self.assertRaises(ValueError, main.Square.area, a3)
        self.assertRaises(ValueError, main.Square.perimeter, a3)

        with self.assertRaises(TypeError):
            main.Square.area(a4)
            main.Square.area(a5)
        
        with self.assertRaises(TypeError):
            main.Square.perimeter(a4)
            main.Square.perimeter(a5)

        return
    
    def test_triangle(self):
        a1, b1, c1, h1 = 20, 12, 16, 9.6
        a2, b2, c2, h2 = 5, -3, 0, -9
        a3, b3, c3, h3 = 1, 2, 4, 3
        a4, b4, c4, h4 = 1, 2, '3', '4'
        
        self.assertEqual(main.Triangle.area(a1, h1), 96)
        self.assertEqual(main.Triangle.perimeter(a1, b1, c1), 48)
        self.assertRaises(ValueError, main.Triangle.area, a2, h2)
        self.assertRaises(ValueError, main.Triangle.perimeter, a2, b2, c2)
        self.assertEqual(main.Triangle.area(a3, h3), 1.5)
        self.assertRaises(ValueError, main.Triangle.perimeter, a3, b3, c3)
        self.assertRaises(TypeError, main.Triangle.area, a4, h4)
        self.assertRaises(TypeError, main.Triangle.perimeter, a4, b4, c4)

        return

if __name__ == '__main__':
    unittest.main()
