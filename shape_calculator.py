

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area
    
    def get_perimeter(self):
        perimeter = (self.width * 2) + (self.height * 2)
        return perimeter

    def get_diagonal(self):
        diagonal = ((self.width ** 2) + (self.height ** 2)) ** 0.5
        return diagonal

    def get_picture(self):
        # check that the rectangle is not too big
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            # make lines equal to the height
            output = ""
            for line in range(self.height):
                lin = ""
                # make "*" equal to the width
                for star in range(self.width):
                    lin = lin + "*"
                output = output + lin + "\n"
            return output
   
    # to represent it as a string
    def __str__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"

    # how often does the shape fit inside the object (self)?
    def get_amount_inside(self, shape):
        # calculate for the width and height individually
        # strip the float of the decimal by converting to int
        widthcalc = self.width / shape.width
        timeswidth = int(widthcalc)
        heightcalc = self.height / shape.height
        timesheight = int(heightcalc)

        # multiply result for width and height to get the total
        times = timeswidth * timesheight
        return times


class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        # super(). does the function (this case the init) for the parent with the given arguments
        super().__init__(side, side)
    
    def __str__(self):
        return "Square(side=" + str(self.side) +")"

    # make a set_side function, making sure that we update both width and height
    def set_side(self, side):
        self.side = side
        super().set_width(side)
        super().set_height(side)

    # update both set_width and set_height function to update both (since its a Square)
    def set_width(self, side):
        self.side = side
        super().set_width(side)
        super().set_height(side)
        # or just:
        #self.width = side
        #self.height = side

    def set_height(self, side):
        self.side = side
        super().set_width(side)
        super().set_height(side)


reccy = Rectangle(4, 8)
square = Square(2)
print(square)
square.set_side(6)
print(square.width)
print(square.height)
square.set_width(8)
square.set_height(10)
print(square.height)
print(square)


