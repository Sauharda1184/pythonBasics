"""Importing the modules and exploring standard library in Python"""

print('Imported myModule...')

test = 'Test String'

def find_index(to_search, target):
   
    for i, value in enumerate(to_search):
        if value == target:
            return i
    return -1