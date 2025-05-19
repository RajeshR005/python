class circle:
    def __init__(self,r):
        self.radius=r
        self.pi=3.14
    def area_and_perimeter(self):
        area=self.pi*(self.radius*self.radius)
        perimeter=2*self.pi*self.radius
        print(f"The area of the circle is: {area}\n The perimeter of the circle is: {perimeter}")
c1=circle(5)
c1.area_and_perimeter()