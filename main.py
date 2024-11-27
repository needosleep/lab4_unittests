import math

class Circle:
    def area(r: int | float) -> int | float:
        '''Takes radius of circle, returns its area'''
        if (not isinstance(r, (int, float))):
            raise TypeError('incorrect data type of input')
        if (r <= 0):
            raise ValueError('radius cannot be equal or less than 0')
        return math.pi * r * r
    
    def perimeter(r: int | float) -> int | float:
        '''Takes radius of circle, returns its perimeter'''
        if (not isinstance(r, (int, float))):
            raise TypeError('incorrect data type of input')
        if (r <= 0):
            raise ValueError('radius cannot be equal or less than 0')
        return 2 * math.pi * r

class Rectangle:
    def area(a: int | float, b: int | float) -> int | float:
        '''Takes a and b - sides of a rectangle, returns area of a rectangle'''
        if (not isinstance(a, (int, float))) or (not isinstance(b, (int, float))):
            raise TypeError('incorrect data type of input')
        if (a <= 0 or b <= 0):
            raise ValueError('sides cannot be equal or less than 0')
        return a * b

    def perimeter(a: int | float, b: int | float) -> int | float:
        '''Takes a and b - sides of a rectangle, returns perimeter of a rectangle'''
        if (not isinstance(a, (int, float))) or (not isinstance(b, (int, float))):
            raise TypeError('incorrect data type of input')
        if (a <= 0 or b <= 0):
            raise ValueError('sides cannot be equal or less than 0')
        return 2 * (a + b)

class Square:
    def area(a: int | float) -> int | float:
        '''Takes side of square, returns its area'''
        if (not isinstance(a, (int, float))):
            raise TypeError('incorrect data type of input')
        if (a <= 0):
            raise ValueError('side cannot be equal or less than 0')
        return a * a


    def perimeter(a: int | float) -> int | float:
        '''Takes side of square, returns its perimeter'''
        if (not isinstance(a, (int, float))):
            raise TypeError('incorrect data type of input')
        if (a <= 0):
            raise ValueError('side cannot be equal or less than 0')
        return 4 * a

class Triangle:
    def area(a: int | float, h: int | float) -> int | float:
        '''
        Returns area of triangle.
            
            Parameters:
                a (int | float): base of triangle
                h (int | float): height of triangle which is drawn to the base

            Result:
                area (float): the area of this triangle
        '''
        if (not isinstance(a, (int, float))) or (not isinstance(h, (int, float))):
            raise TypeError('incorrect data type of input')
        if (a <= 0 or h <= 0):
            raise ValueError('side or height cannot be equal or less than 0')
        return a * h / 2

    def perimeter(a: int | float, b: int | float, c: int | float) -> int | float:
        '''
        Returns perimeter of triangle.

            Parameters:
                a, b, c (int | float): sides of a triangle

            Result:
                perimeter (int | float): the perimeter of this triangle
        '''
        if (not isinstance(a, (int, float))) or (not isinstance(b, (int, float))) or (not isinstance(c, (int, float))):
            raise TypeError('incorrect data type of input')
        if (a <= 0 or b <= 0 or c <= 0):
            raise ValueError('sides cannot be equal or less than 0')
        
        if (max(a, b, c) >= (a + b + c - max(a, b, c))):
            raise ValueError('incorrect triangle')
        return a + b + c
    
    