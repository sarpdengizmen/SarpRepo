from math import cos, sin, pi, acos, sqrt
class stupidclass():
    pass

class point2d():
    '''A 2D point class'''

    def __init__(self,x=0 ,y=0):
        print('IM ALIVE!')
        self.x = x
        self.y = y

    def __del__(self): # This is what is done when the object is deleted
        print(f'({self.x},{self.y}): IM DEAD!')
    
    def distance(self, p = None):
        if p == None:
            p = point2d()
        return sqrt(
                    (self.x - p.x)**2 + 
                    (self.y - p.y)**2
                    )
    
    def __str__(self): # This is what is returned when you change object to string object overwriting base class properties
        return f"This is a point at: {self.x},{self.y}"
    
    def __repr__(self): 
        return f"{self.x},{self.y}"
    
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, newValue): # This is what is done when you try to set the value of x
        if isinstance(newValue, int):
            self.__x = newValue
        else:
            print(f"{newValue} is not an integer")
            self.__x = -1
    
class vector2d(point2d): # Inheritance from point2d

    def __init__(self, x=0, y=0):
        point2d.__init__(self, x, y) # Call the base class constructor
        print('hello vector as well')

    def __str__(self):
        return f"This is a vector at: {self.x},{self.y}"
    
    def __repr__(self):
        return f"{self.x},{self.y}"
    
    def __magnitude(self):
        return point2d.distance(self)
    
    @property
    def magnitude(self):
        return self.__magnitude()
    
    @magnitude.setter
    def magnitude(self, newValue):
        print('You cant set the magnitude')
    
    def __add__(self, b):
        return vector2d(self.x + b.x, self.y + b.y)
    
    def __mul__(self, b):
        return self.x * b.x + self.y * b.y
    def __eq__(self,b):
        return self.x == b.x and self.y == b.y