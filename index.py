##################PYTHON##########################
###Practice With Bonfas Daily 2hours python daily
price = 10
# price = 20#integer a number without decimal
rating = 4.9#floating
name = "Bonny"
is_published = False#use capital for booleans
# print(price)
#############################################################
##Exercise
full_name = "John Smith"
age = 20
is_new = True
# int(), float(),bool(),print(),input(),len(to count the number of items in a list)
####how to receive input from user
#name = input('What is your? ')
#print('Hi ' + name)#concatination of expression
#############################################################
##Exercise
fname = input('What is your name? ')
color = input('What is your favorite color? ')
print(fname + ' likes ' + color)
#############################################################
##types
birth_year = input('Birth year: ')#returns a string
my_age = 2023 - int(birth_year)
print( my_age)
print(type(my_age))#returns an int
#############################################################
##Exercise
weight = input('What is your weight(in pounds)? ')
weight_inkg = int(weight) / 1000
print(weight_inkg)
#############################################################
##case sensitive language
student_count = 1000
rating = 4.99
is_published = False
course_name = "Python Programming"
print(student_count, course_name)
print("MY name is Bonfas Oluoch")
print("0----")
print(' ||||')
print("*" * 10)#expression
print("^^^^^")
print(" !!!")
print("  * ")
############################################################
##STRINGS
course = "Python's Course for Beginners"
intro = '''
Hallo Bonfas,

We are glad for your support.

Thank you,
Support Team
'''
#print(course)
p_name = 'Jennifer'
print(p_name[1:-1]) # remove the first character and the last character
#print(course[0:5])#returns Pytho
#another = course[:]
#print(intro)
############################################################
##Formatted STRINGS
last = 'Oluoch'
first = 'Bonny'
message = first + ' [' + last + '] is a coder'
msg = f'{first} [{last}] is a coder'#formatted string 
print(message)
print(msg)
############################################################
##STRINGS Methods
python = 'Python For Beginners'
print(len(python))
print(python.upper())#Return a copy of the string converted to uppercase.
print(python.lower())#Return a copy of the string converted to lowercase.
print(python.find('P'))#returns the lowest index and it is case sensitive
print(python.replace('Beginners', 'Absolute Beginners'))#Return a copy with all occurrences of substring old replaced by new.
print('Python' in python)#True
print('python' in python)#False

############################################################
##ARITHMETIC OPERATIONS
# +,-,/,//,%,*,**
print(10 ** 3)
x = 10
x = x + 3
x += 3
print(x)
# operator precendence
x = 10 + 3 * 2 ** 2
print(x)
x = (2 + 3) * 10 - 3 #47
print(x)
# PARENTHESIS //have authority overwrites the order
# exponetiation 2**3
# multiplication or Division
# addition or substraction
############################################################
##Maths Functions
import math
print(math.ceil(2.9))
print(math.floor(2.9))
x= 2.9
# print(round(x))
# print(abs(-2.9))#returns a positive number
############################################################
##If statement
is_hot = False
is_cold = True
if is_hot:
    print('It is a hot day')
    print("Drink Plenty of Water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm cloths")
else:
    print("It's a lovely day, enjoy Your Day")

############################################################
##Exercise
price = 1000000
has_good_credit = False
if has_good_credit:
    down_pay = price * (10 / 100)
else:
    down_pay = price * (20 / 100)
print(f'Down payment is ${down_pay}')

print("Enter marks Obtained in 5 subjects: ")
mark_one = int(input())
mark_two = int(input())
mark_three = int(input())
mark_four = int(input())
mark_five = int(input())

total = mark_one+mark_two+mark_three+mark_four+mark_five
average = total / 5

print("Average=%.2f"%average)
if(average >= 70 and average <= 100):
    print("Your grade is A")
elif(average >= 60 and average <= 69):
    print("Your Grade is B")
elif(average >= 50 and average <= 59):
    print("Your Grade is C")
elif(average >= 40 and average <=49):
    print("Your Grade is D")
elif(average >= 0 and average <= 30):
    print('Your Grade is F')
else:
    print("Invalid input")

# Geuse my number game
secret_number = 9
trial_count = 3
initial_start = 0
while initial_start < trial_count:
    guess = int(input("Guess: "))
    initial_start += 1
    if(guess == secret_number):
        print('You won,Hureeey!')
        break
    else:
        print('Sorry pal, you have lost it')

