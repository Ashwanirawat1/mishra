class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius
    

    def set_radius(self, value):
        if not isinstance(value, (int, float)):
            raise Exception("Radius must be an int or float")
        self.radius = value

    def circumference(self):
        return 2*3.14*self.radius

c = Circle(2)
print(c.__dict__)
print(c.radius)
c.radius = 3
print(c.__dict__)
print(c.radius)