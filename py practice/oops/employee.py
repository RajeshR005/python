class Employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary
        
    # def showdetails(self):
        # return self.role , self.department, self.salary
        # print("The role is",self.role)
        # print("The department is",self.department)
        # print("The Salary of the person is:",self.salary)
class Engineer(Employee):
    
    def __init__(self,role,department,salary,name,age):
        super().__init__(role,department,salary)
        self.name=name
        self.age=age
        
    def updated_details(self):
        
        print("Name:",self.name)
        print("Age:",self.age)
        print("role:",self.role)
        print("department",self.department)
        print("salary",self.salary)

emp2=Engineer("Developer","Team Python",25000,"Prince",22)
emp2.updated_details()
        
















# emp.showdetails()
