# Inspired by the Following YouTube Tutorial
# ------------------------------------------
# Object Oriented Programming in Python
# https://youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def full_name(self):
        return f'{self.first} {self.last}'

emp_1 = Employee('John', 'Doe', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.email)
print(emp_2.email)

print(emp_1.full_name())
print(Employee.full_name(emp_2))
