class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        returned_string = ""
        for i in range(self.height):
            returned_string += "*".center(self.width, "*") + "\n"
        return returned_string

    def get_amount_inside(self, shape):
        print(self.width, self.height, shape.width, shape.height)
        if self.width >= shape.width and self.height >= shape.height:
            return (self.width // shape.width) * (self.height // shape.height)
        else:
            return 0

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):

    def __init__(self, side):
        self.height = side
        self.width = side

    def set_side(self, side):
        self.set_height(side)
        self.set_width(side)

    def __repr__(self):
        return f"Square(side={self.width})"