def Lamda_fun():

    add_ten = lambda x: x + 10

    multiply = lambda x,y : x * y

    return True if multiply % 2 == 0 else False


print(Lamda_fun.add_ten(5))

print(Lamda_fun.multiply(4,7))