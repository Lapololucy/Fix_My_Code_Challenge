#!/usr/bin/python3

class Square:
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area(self):
        """Area of the square"""
        return self.width * self.width

    def perimeter(self):
        """Perimeter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area())
    print(s.perimeter())
