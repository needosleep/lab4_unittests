import math

class Circle:
    def area(r):
        '''Takes radius of circle, returns its area'''
        return math.pi * r * r
    
    def perimeter(r):
        '''Takes radius of circle, returns its perimeter'''
        return 2 * math.pi * r

class Rectangle:
    def area(a, b):
        '''Takes a and b - sides of a rectangle, returns area of a rectangle'''
        return a * b

    def perimeter(a, b):
        '''Takes a and b - sides of a rectangle, returns perimeter of a rectangle'''
        return 2 * (a + b)

class Square:
    def area(a):
        '''Takes side of square, returns its area'''
        return a * a


    def perimeter(a):
        '''Takes side of square, returns its perimeter'''
        return 4 * a

class Triangle:
    def area(a, h):
        '''
        Returns area of triangle.
            
            Parameters:
                a (int | float): base of triangle
                h (int | float): height of triangle which is drawn to the base

            Result:
                area (float): the area of this triangle
        '''
        return a * h / 2

    def perimeter(a, b, c):
        '''
        Returns perimeter of triangle.

            Parameters:
                a, b, c (int | float): sides of a triangle

            Result:
                perimeter (int | float): the perimeter of this triangle
        '''
        return a + b + c
