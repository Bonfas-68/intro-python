has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit :
    print("Eligible for loan")

# Comparison operators
temperature = 37
if temperature >= 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

# Exercise 
name = input("Enter Your Name: ")
if len(name) <= 3 :
    print("Name must be at least 3 characters")
elif len(name) >= 50:
        print("name can be a maximum of 50 characters") 
else:
    print("name looks good!")




# weight converter challenge

weight = int(input("Weight: "))  
converter = input("(L)bs or (K)g: ")
if converter.upper() == "L":
    print(f"You are {weight * 0.45} pounds" )
elif converter.upper() == "K":
    print(f"You are {weight / 0.45} kilos" )
else:
    print("Must be either K or L")


##################################
##while loop
i = 1
while i <= 5:
    print("*" * i)
    i += 1
print("Done")
#### Guess My number game
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You Won!")
        break
else:
    print("Sorry pal, you failed!")
##################
##Car Game
car_tools = ""
started = False
while True:
    car_tools = input("> ").lower()
    if car_tools == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...")
    elif car_tools == "stop":
        if not started:
            print("Car already stopped!")
        else:
            started = False
            print("Car stopped...")
    elif car_tools == 'help':
        print("""
    start - to Start the car
    stop - to stop the car
    quit - to kill the process
        """)
    elif car_tools == 'quit':
        break
    else:
        print("Dont understand you, pal!!")

