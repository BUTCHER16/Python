def greetname(name):
    return f'Hello, {name}! Welcome Back'

print(greetname("Albert"))

def is_even(number):
    return True if number % 2 == 0 else False

print(is_even(10))

def Calulate_area(length, width):
    return length * width
    
print(Calulate_area(10, 20))

def sum_all(*args):
    return sum (args)

print(sum_all(1,2,3,4,5))

def user_profile(**kwargs):
    return kwargs

print(user_profile(FirstName = "Albert", LastName = "Ravidoss", Role = "Junior System Administrator"))

