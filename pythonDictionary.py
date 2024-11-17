# Using dictionary in python for key-value pairs
my_dict = {'key1':100, 'key2':300}
print(my_dict)

#student = {'name':'John','age':25,'courses':['MATH','CompSCI']}
#student.update({'name':'Jello','age':26,'rollNum':222})

#print(student)
#print(student['courses'])
#print(student.get('phone'))

myEmployee = {'name':'Ayahn','age':33,'salary':50000}
myEmployee.update({'name':'Jenisha','age':23,'location':'Saint Cloud'})
#del myEmployee['age']
#age = myEmployee.pop('age')

#print(myEmployee)
#print(myEmployee.items())
#print(age)
for key in myEmployee:
    print(key)