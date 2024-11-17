#This is a practice file for the classes

class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade
    
    def get_age(self):
        return self.age
    
    def get_name(self):
        return self.name
    
    def student_info(self):
        return '{} is {} years old and has a grade of {}'.format(self.name,self.age,self.grade)
    
student1 = Student('Tim',21,95)
student2 = Student('Bill',23,99)
student3 = Student('Jill',20,94)


print(student1.get_grade())
print(student2.get_grade())
print(student3.get_name())
        
   

print(student1.student_info())
print(student2.student_info())
print(student3.student_info())