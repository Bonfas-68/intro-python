def welcome():
    user_name = input('Enter your user name: ')
    print(f"Welcome {user_name}!!")


welcome()

def jambo():
    print("Jambo africa, Welcome to PLP!!")
    print('We are learning python')

#function calling
jambo()

"""def find_area():
    radius = float(input("Enter the radius: "))
    area = radius ** 2 * 3.142
    print(f'The area of a circle whose radius is {radius} is {area}')

# function calling
find_area()"""

def details(f_name, l_name):
    print(f"Hello!! my name is {f_name} {l_name}")
# function calling
details('Bonfas','Oluoch')
# function

def greet_use(f_name, l_name):
    print('Hi there!', f_name , l_name)
    print("Welcome aboard")

print('Start')
greet_use("John","Smith")
greet_use("Bonfas","oluoch")
print("Finish")