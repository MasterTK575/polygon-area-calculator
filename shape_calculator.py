

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
            return "Too big for picture"
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



reccy = Rectangle(4, 8)
square = Rectangle(4, 4)
print(reccy)
print(reccy.get_amount_inside(square))


