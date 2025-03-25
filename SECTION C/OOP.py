
class Employee:
    def __init__(self, name, salary): 
        self.name = name
        self.salary = salary
    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}")



manager1 = Manager("John", 50000, "phy")
manager1.display_info()      