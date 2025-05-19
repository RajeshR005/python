class student:
    scl_name="Prince Higher secondary"
    def __init__(self,name,maths,science,computer_science):
        self.name=name
        self.maths=maths
        self.science=science
        self.computer_science=computer_science
    def avg(self):
        avg=self.maths+self.science+self.computer_science//3
        print(avg)
s1=student("Prince",97,86,100)
print(s1.scl_name)
print(s1.name)
print("Maths: ",s1.maths,"\nScience: ",s1.science, "\nComputer Science: ",s1.computer_science)
s1.avg()


        