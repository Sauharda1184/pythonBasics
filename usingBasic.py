# Using the Basic init method in classes

class Employee:
    # This is like a constructor in C++
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

#This is how we create objects and assign values to them 
emp1 = Employee('Corey', 'Schafer', 50000)
emp2 = Employee('Test','User',60000)

        #print(emp1)
        #print(emp2)

print(emp1.first)
print(emp2.first)
        #print('{} {}'.format(emp1.first, emp1.last))
print(emp1.fullname())
print(emp2.fullname())

#This is how we call the method without creating an object
print(Employee.fullname(emp1))
print(Employee.fullname(emp2))


