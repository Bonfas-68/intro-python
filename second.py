name = 'Bonfas Oluoch';
print(name)
is_new = True
p_name = 'John Smith'
p_age = 20
doc_msg = f'Patients name is {p_name} and he is a {p_age}  year old'
print(doc_msg)
x = 10.80
print(type(x))#<class 'float'>
#python arrays (list or tuples)
plp_student = ['Bonfas','Winnie','Job']
x = plp_student[0]
print(x)
# print(plp_student, type(plp_student))#list is mutable

tup = (21,24,25,12)#tuple is immutable
# tup(0) = 'copy' cannot be m
print(tup[0])
p_set = {1,2,3,4,5,6,7,7}
print(p_set)
####################
##using input()
# my_full_name = input("What is Your name? ")
# print("My name is " + my_full_name)
# x = int(input("Enter 1st number "))
# y = int(input("Enter 2nd number "))
# z = x * y
# print(z)
# ch =  input("Enter a char ")
# print(ch)
# ch =  eval(input("Enter an expr "))
# print(ch)
# complement(~ tilde operator)
# and 
# or
# xor
# left shift operator
# right shift operator
print(~12)
print(12 & 13)#prints 12
print(12 | 13)#prints 13
print(12 ^ 13)#prints 1
print(10 << 2) #prints 40 gaining bits
print(10 >> 2) #prints 40 losing bits

#############################
##Exercise one from plp
#A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask the user for their salary and year of service and print the net bonus amount. Write a python code to implement this scenario.
bonus = 0.05
my_years_of_service = int(input("Enter years of experience: "))
my_salary = input("Enter your salary: ")
is_more_than_5 = True
if(my_years_of_service >= 5):
    net_bonus = int(my_salary) * bonus
    print(net_bonus)
else:
    print('Need more years to earn a bonus:)')
#####################
##experimenting with python
first_name = "Bonfas"
print("Hello, Pyhton!")
print(first_name)
#  print(Hello, Python!)#SyntaxError: invalid syntax
# print "Hello, Python!"#SyntaxError: Missing parentheses in call to 'print'.
# print('Hello, Python!')

# '''prints the following only:
# Hello, Pyhton!
# Bonfas
# Hello, Python!'''

number = 1
match number:
    case 1:
        print('one')
    case 2:
        print('two')
