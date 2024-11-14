class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def scale(self, factor):
        # Method to scale the rectangle's width and height
        self.width *= factor
        self.height *= factor

    def area(self):
        # Calculate the area of the rectangle
        return self.width * self.height

    def __lt__(self, other):
        # Compare rectangles based on their areas
        return self.area() < other.area()

    def __str__(self):
        # String representation in the format "width x height Rectangle"
        return f"{self.width} x {self.height} Rectangle"

if __name__ == "__main__":
    r1 = Rectangle(1, 4)
    r2 = Rectangle(2, 16)
    while r1 < r2:
        print(r1)
        r1.scale(2)
    print(f"Final size of r1 is: {r1}.")
    print(r2)

