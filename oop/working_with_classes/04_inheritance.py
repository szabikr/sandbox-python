# Inspired by the Following YouTube Tutorial
# ------------------------------------------
# Object Oriented Programming in Python
# https://youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc

class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@email.com'

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

dev_1 = Developer('Szabi', 'Keresztes', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'JavaScript')
mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(f'dev_1 email address: {dev_1.email}')
print(f'dev_1 programming language: {dev_1.prog_lang}')

print()
print(f'dev_1 salary: {dev_1.pay}')
dev_1.apply_raise()
print(f'dev_1 salary after raise: {dev_1.pay}')

print()
print(f'mgr_1 email address: {mgr_1.email}')

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)

print('Employees that mgr_1 manages:')
mgr_1.print_emps()

print(f'is {mgr_1.first} a Manager? {isinstance(mgr_1, Manager)}')
print(f'is {mgr_1.first} an Employee? {isinstance(mgr_1, Employee)}')
print(f'is {mgr_1.first} a Developer? {isinstance(mgr_1, Developer)}')

print()
print(f'is {Manager.__name__} a subclass of {Employee.__name__}? {issubclass(Manager, Employee)}')
print(f'is {Manager.__name__} a subclass of {Employee.__name__}? {issubclass(Manager, Employee)}')
print(f'is {Manager.__name__} a subclass of {Developer.__name__}? {issubclass(Manager, Developer)}')




