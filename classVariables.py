#Class variables 

class Employee:

    #decalring a class variable
    numOfEmp = 0
    raise_amount = 1.04
    doubleRaise = 2

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last 
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.numOfEmp +=1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    def double_raise(self):
        self.pay = int(self.pay * Employee.doubleRaise)

emp1 = Employee('Corey','Schafer',50000)
emp2 = Employee('Ron','Jacker',78000)

'''
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)


print(emp2.pay)
emp2.double_raise()
print(emp2.pay)

#what is the raise amount 
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

# using python dictionary to access information of an instance of class
print(emp1.__dict__)
print(emp2.__dict__)
'''
