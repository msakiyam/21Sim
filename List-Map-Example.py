




list_num = list(range(0,100))

print(list_num)

even = list()


for i in list_num:
    if i % 2 == 0:
        even.append(i)

print(even)

#Filter and Map

even = list(filter (lambda i:  i % 2 == 0,list_num))
print(even)

even = list(map(lambda i:  i % 2 == 0,list_num))
print(even)