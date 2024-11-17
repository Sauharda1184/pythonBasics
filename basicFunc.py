#Learning basic functions in Python

#def my_func(greeting,name='Me'):
    #return '{}, {}'.format(greeting,name)
#print(my_func('Hi','Jenisha'))
# Using args and kwargs in Python
def employee_infor(*args,**kwargs):
    print(args)
    print(kwargs)

company = ['Apple','Microsoft']
info = {'name':'Damien','age':25}

employee_infor(*company,**info)