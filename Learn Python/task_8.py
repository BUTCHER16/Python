"""def Lamda_fun():

    add_ten = lambda x: x + 10

    multiply = lambda x,y : x * y

    return True if multiply % 2 == 0 else False


print(Lamda_fun.add_ten(5))

print(Lamda_fun.multiply(4,7))"""



nums = [1,2,3,4,5,6,10,11,12,15]
greater = list(filter(lambda x: x>=10, nums))

print(greater)

