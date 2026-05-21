# object oriented programming

class Employee:         # this is a class named Employee

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = str.lower(first) + str.lower(last) + '.bits@gmail.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return self.first + ' ' + self.last

    def pay_raise(self):
        self.pay = int(self.pay) * self.raise_amount


print(Employee.num_of_emps)

# an insance of the class Employee
emp1 = Employee('Chirag', 'Arora', 10000)
emp2 = Employee('Test', 'User', 20000)

print(Employee.num_of_emps)

# print(emp1.first)
# print(emp1.email)
# print(emp1.fullname())

# emp1.pay_raise()
# print(emp1.pay)

# print(Employee.raise_amount)

# emp1.raise_amount = 1.05
# print(emp1.raise_amount)

# print(Employee.raise_amount)
