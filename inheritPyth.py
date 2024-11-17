class Employee:

    raise_amount = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang

class Manager(Employee):
     def __init__(self,first,last,pay,employees = None):
            super().__init__(first,last,pay)
        if employees is none:
          self.employees = []
        else:
          self.employees = employees



    


dev_1 = Developer('Corey','Schafer',50000,'Python')
dev_2 = Developer('Sauharda','Shrestha',80000,'JavaScript')

print(dev_1.email)
print(dev_1.prog_lang)


'''
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
'''