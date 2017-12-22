#print -- 10 minutes

print('hello world')
print(12345)


#excercise
# write a program to say your name
# write a program to display your age.

# use format
name = 'John'
print('hello {0}'.format(name))

# do the math -- 10 minites

print(1+2)
print(2*3)
print(4%7)
print(9/3)
print(10-5)

print((8-2)*4)

#excercise

#explore the math operators


# Variables -- 20 minutes

int_var = 10

print(int_var * 8)
print(int_var - 2)
print(int_var + 2)
print(int_var % 2)
print(int_var / 2)

str_var = '1'

print(str_var * 8)

str_var2 = '2'

print(str_var  + str_var2)

# Input

#user_input = input('Please enter your name: ')

#print('Hello {0}'.format(user_input))

import random
number = random.randint(0,10)

print(number)
while True:

    n = input('Guess the number : ')

    if int(n) == number:

        break
print('Congrats!')

# range, list , comprehension and loop


print(range(1,10))

print(list(range(1,10)))

for i in list(range(1,10)):
    print(i)

print([i*2 for i in list(range(1,10))])
print([i**2 for i in list(range(1,100))])
print([lambda i : i**2,list(range(1,100))])

mylist = [lambda i: i**2,list(range(1,100))]

for j in mylist:
    print(j)


import random
l = list(range(1,1000))

n = random.choice(l)

print('random number is {0}'.format(n))

#class

