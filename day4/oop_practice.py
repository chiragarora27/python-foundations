# object oriented programming

import datetime


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

    @classmethod
    def set_rasie_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split('-')
        return cls(first, last, pay)

    @staticmethod
    def check_working_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True


# an insance of the class Employee
emp1 = Employee('Chirag', 'Arora', 10000)
emp2 = Employee('Test', 'User', 20000)

emp_string_1 = "Sahil-Arora-50000"

new_emp_1 = Employee.from_string(emp_string_1)

print(Employee.num_of_emps)
print(Employee.fullname(new_emp_1))

Employee.set_rasie_amt(1.07)
print(Employee.raise_amount)

my_date = datetime.date(2026, 5, 23)

print(Employee.check_working_day(my_date))

# print(Employee.num_of_emps)

# print(emp1.first)
# print(emp1.email)
# print(emp1.fullname())

# emp1.pay_raise()
# print(emp1.pay)

# print(Employee.raise_amount)

# emp1.raise_amount = 1.05
# print(emp1.raise_amount)

# print(Employee.raise_amount)
