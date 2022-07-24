class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
    
    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.height * self.width
    
    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):

        if self.width > 50 or self.height > 50:
            return "Too big picture."
        else:
            return '\n'.join('*' * self.width for _ in range(self.height)) + '\n'

    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)


class Square(Rectangle):
    def __init__(self, side) -> None:
        self.width = side
        self.height = side

    def set_side(self, side):
        self.width = side
        self.height = side

    def __str__(self) -> str:
        return f"Square(side={self.width})"

    def set_height(self, height):
        self.height = height

    def set_width(self, width):
        self.width = width
 

    

    
