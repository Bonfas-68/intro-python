numbers = [2,4,6,8,3,5,6,3]
numbers.insert(0,11)
numbers.remove(5)
numbers.append(20)
# numbers.clear()
numbers.pop()
numbers.sort()
numbers.reverse()
numbers2 = numbers.copy()
numbers.append(1)
print(numbers.index(4))
print(numbers.count(3))
print(numbers, numbers2)
print(set(numbers))


###############
##challenge one - write a program to remove duplicates from a list
numbers = [1,2,3,3,4,2,3,5,6,2,6,5]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
