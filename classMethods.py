#Object-Oriented-Programming in Python
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

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount
    
    # A new class method to use it as an alternative constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str_1.split('-')
        cls(first,last,pay)
        


emp1 = Employee('Corey','Schafer',50000)
emp2 = Employee('Ron','Jacker',78000)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-40000'

first, last, pay = emp_str_1.split('-')

new_emp_1 = Employee(first,last,pay)

print(new_emp_1.email)
print(new_emp_1.first)
print(new_emp_1.last)
print(new_emp_1.pay)




#what is the raise amount 
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

Employee.set_raise_amt(1.06)
print(Employee.raise_amount)
print(emp1.raise_amount)
# using python dictionary to access information of an instance of class
print(emp1.__dict__)
print(emp2.__dict__)


