class Square:
 
    def __init__(self, length):
        self.length = length
    
    def __truediv__(self, divider):
        try:
            self.length /= divider
        except ZeroDivisionError:
            pass
 
    def __eq__(self, other):
        return self.length ** 2 == other.length ** 2
 
 
if __name__ == "__main__":
    r1 = Square(2)
    r2 = Square(4)
    if r1 == r2:
        print('They have the same area')
    else:
        print('They have different areas')
    r2 / 2
    if r1 == r2:
        print('They have the same area')
    else:
        print('They have different areas')

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __mul__(self, factor):
        # Define the multiplication behavior to scale the rectangle
        return Rectangle(self.width * factor, self.height * factor)

    def __lt__(self, other):
        # Compare rectangles by their areas
        return (self.width * self.height) < (other.width * other.height)

    def __str__(self):
        # String representation in the format "width x height Rectangle"
        return f"{self.width} x {self.height} Rectangle"

# Main code block to execute
if __name__ == "__main__":
    r1 = Rectangle(1, 4)
    r2 = Rectangle(2, 16)
    while r1 < r2:
        print(r1)
        r1 = r1 * 2  # Scale r1 by a factor of 2
    print(f"Final size of r1 is: {r1}.")
    print(r2)
