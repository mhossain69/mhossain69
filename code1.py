class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __mul__(self, factor):
        # Multiply the width and height by a factor
        return Rectangle(self.width * factor, self.height * factor)

    def __lt__(self, other):
        # Compare areas of the rectangles
        return self.width * self.height < other.width * other.height

    def __str__(self):
        # String representation in the format "width x height Rectangle"
        return f"{self.width} x {self.height} Rectangle"

if __name__ == "__main__":
    r1 = Rectangle(1, 4)
    r2 = Rectangle(2, 16)
    while r1 < r2:
        print(r1)
        r1 = r1 * 2
    print(f"Final size of r1 is: {r1}.")
    print(r2)

