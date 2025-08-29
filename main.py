import math


def calculate_circle_area(radius: float) -> float:
    """Calculate the area of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2


class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        """Initialize the rectangle with width and height."""
        if width < 0 or height < 0:
            raise ValueError("Width and height cannot be negative")
        self.width: float = width
        self.height: float = height


    def area(self) -> float:
        """Return the area of the rectangle."""
        return self.width * self.height


    def perimeter(self) -> float:
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


    def is_square(self) -> bool:
        """Return True if the rectangle is a square, else False."""
        return self.width == self.height


    def resize(self, new_width: float, new_height: float) -> None:
        """Change the width and height of the rectangle."""
        if new_width < 0 or new_height < 0:
            raise ValueError("Width and height cannot be negative")
        self.width = new_width
        self.height = new_height


def test_rectangle() -> None:
    rect = Rectangle(5, 10)
    assert rect.width == 5
    assert rect.height == 10
    assert rect.area() == 50
    assert rect.perimeter() == 30
    assert rect.is_square() is False

    rect.resize(7, 7)
    assert rect.is_square() is True
    assert rect.area() == 49
    assert rect.perimeter() == 28


if __name__ == "__main__":
    # Task 1: Circle area
    radius: float = float(input("Enter the radius of the circle: "))
    area: float = calculate_circle_area(radius)
    print(f"The area of the circle with radius {radius} is {area:.2f}")

    # Task 2: Rectangle class tests (using assert)
    test_rectangle()
    print("All rectangle tests passed.")