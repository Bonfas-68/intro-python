for item in range(5, 10, 2):
    print(item)

prices = [10, 20, 30]
total = 0
for cost in prices:
    total += cost
    print(total)


####Challenge one write a program to print f using x for the structure 

"""
xxxx
x
xxxx
x
x
"""
numbers = [5, 2, 5, 2, 2]
for fiy in numbers:
        af = ''
        for count in range(fiy):
            af = 'x' * count
        print(af)
print('__________--------------______________')
#print L
numbers = [2, 2, 2, 5]
for fiy in numbers:
        af = ''
        for count in range(fiy):
            af = 'x' * count
        print(af)

# A program to find the largest number in the list
numbers = [1,54,3,5,54,23,54,21]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)