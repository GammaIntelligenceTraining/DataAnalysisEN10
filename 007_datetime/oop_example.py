class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Employee {self.name}. Salary {self.salary}"


emp1 = Employee('Jack', 2000)
emp2 = Employee('Mary', 3000)

print(emp1)

print(str(emp1))