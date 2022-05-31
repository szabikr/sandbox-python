# Inspired by the Following YouTube Tutorial
# ------------------------------------------
# Object Oriented Programming in Python
# https://youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc

class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def full_name(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('John', 'Doe', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(Employee.num_of_emps)

emp_1.apply_raise()
print(emp_1.pay)

emp_2.raise_amount = 1.05
emp_2.apply_raise()
print(emp_2.pay)
