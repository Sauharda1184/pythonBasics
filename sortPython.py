# Sorting in Python
'''
my_list = [9,3,4,10,31,21,11,2,102]
sortmy_list = sorted(my_list)
reverse_sorted_l = sorted(my_list, reverse=True)
print(sortmy_list)
my_list.sort()
print(my_list)
print(reverse_sorted_l)

# Sorting tuples in Python
tup = (9,1,4,8,2,3,6,0)
STup = sorted(tup)
print(STup)

my_dickt = {'name':'Corey','Job':'Programming','age':None, 'OS':'MacOSX'}
s_dickt = sorted(my_dickt)
print(s_dickt)
'''

class Employee():
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},{})'.format(self.name,self.age,self.salary)
    
e1 = Employee('Sauharda',22,30000000)
e2 = Employee('Jenisha',22,4000000)
e3 = Employee('Alex',24,2000000)

employees = [e1,e2,e3]

def e_sort(emp):
    return emp.name

s_employees = sorted(employees,key=e_sort)

print(s_employees)