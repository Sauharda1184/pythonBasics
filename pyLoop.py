#loops and iterations in Python
#myNum = [1,2,3,4,5,6]

#for num in myNum:
    #print(num)
'''
nums = [1,2,3,4,5,6]

for num in nums:
    for letter in 'abcd':
        print(num,letter)
        
for i in range(1,12):
    print(i)
'''
x = 0
while x<12:
    print(x)
    x+=2

y = 0
while y<12:
    if y==5:
        break
    print(y)
    y+=1

z=0
while True:
    if z==20:
        break
    print(z)
    z +=2
    