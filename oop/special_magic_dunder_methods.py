class Employee:
    raise_amt: 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = f'{first}.{last}@email.com'
        self.pay = pay

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
    
    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

    def __str__(self):
        return f'{self.fullname()} - {self.email}'

    def __add__(self, other):
        if isinstance(other, Employee):
            return self.pay + other.pay
        
        """Let the 'other' type to check if they know how to add these instances together"""
        return NotImplemented

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Szabi', 'Keresztes', 50000)
emp_2 = Employee('Test', 'Employee', 60000)


print(f'Using the __str__ dunder method: {emp_1}')

print()
print(f'The result of adding 2 Employees together (__add__): {emp_1 + emp_2}')

print()
print(f'Debugging related print, using the __repr__ method: {repr(emp_1)}')
print(f'End user related print, using the __str__ method: {str(emp_1)}')

print()
print(f'Using the dunder __len__ method: {len(emp_1)}')


# When we say >>> len('test') this is what happens in the background:
# print('test'.__len__())

# When we say >>> 1 + 2 this is what happens in the background:
# print(int.__add__(1, 2))

# When we say >>> 'a' + 'b' this is what happens in the background:
# print(str.__add__('a', 'b'))
