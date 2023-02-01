#if statement
#--------------------------------------------
#if condition:
#       block statement
#elif condition:
#       elif block statement
#else:
#   else block statement

bill = 2500
bill =  1900
discount1 = 100
if bill > 2000:
    print("Bill is greater than 2000")
    final_bill =  bill + discount1
    print("Final bill: " + str(final_bill))
else:
    print("Bill is less than 2000!")



a = int(input("Enter a? ")); 
b = int(input("Enter b? ")); 
c = int(input("Enter c? ")); 
if a>b and a>c: 
  print("a is largest"); 
if b>a and b>c: 
  print("b is largest"); 
if c>a and c>b: 
  print("c is largest");
#########Example using elif statement
number = int(input("Enter the number?")) 
if number==10: 
  print("number is equals to 10") 
elif number==50: 
  print("number is equal to 50"); 
elif number==100: 
  print("number is equal to 100"); 
else: 
  print("number is not equal to 10, 50 or 100"); 


######Example two using elif statement
marks = int(input("Enter the marks? ")) 
if marks > 85 and marks <= 100: 
  print("Congrats ! you scored grade A ...") 
elif marks > 60 and marks <= 85: 
  print("You scored grade B + ...") 
elif marks > 40 and marks <= 60: 
  print("You scored grade B ...") 
elif (marks > 30 and marks <= 40): 
  print("You scored grade C ...") 
else: 
  print("Sorry below average ?") 

####################
##match case in python
# match subject:
#     case <pattern_1>:
#         <action_1>
#     case <patter_2>:
#         <action_2>
#         |
#         |
#         |
#     case _: #default
#         <action_wildcard>

number = 1
match number:
    case "1":
        print("one")
    case "2":
        print("two")
    case _:
        print("none or unknown")
