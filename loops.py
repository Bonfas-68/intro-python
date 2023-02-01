############################################################
##LOOPS
# For loop
numbers = [1,2,3,4,5,6,7,8,9]

sum = 0

for val in numbers:
    sum = sum + val
print('The sum is', sum)

str = 'KIRINYAGA'
for i in str:
    print(i + f" - {i}")

#using range(start,stop,step size(skip numbers from iteration)) and input() functions
###Calculator of different numbers
n = int(input('Enter the number: '))#4
for i in range(1, 11):
    c = n * i
    print(f"{n} * {i} = {c}")


########Program to print even numbers using step size in range
n = int(input("Enter the number: "))
for i in range(2,n,2):
    print(i)
########Program to print string using len( ) and range( )
list = ['Bonfas','James','Charity','Watson','Wayne']
for i in range(len(list)):
    print('Good morning', list[i])
rows = int(input("Enter the number of rows: "))
for i in range(0, rows + 1):
    for j in range(i):
        print(i, end = ' ')
    print()

#While loop
n = int(input("enter a number: "))
sum = 0
i = 1
while i <= n:
    sum = sum + i
    print(i)
    i = i + 1
print(f"The sum is: {sum}")