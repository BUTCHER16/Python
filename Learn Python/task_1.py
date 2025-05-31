class Calc:

    def Add(self,input1, input2):
        return input1 + input2
    
    def Sub(self,input1, input2):
        return input1 - input2
    
    def Mul(self,input1, input2):
        return input1 * input2
    
    def Div(self, input1, input2):
        return input1 / input2
    
    def Mod(self, input1, input2):
        return input1 % input2
    
    def Exp(self, input1, input2):
        return input1 ** input2
    
    def str_rev(self, String):
        print(len(String))
        return String[::-1]

calulator = Calc()

print(calulator.Add(10,20))
print(calulator.Sub(10,20))
print(calulator.Mul(10,20))
print(calulator.Div(10,20))
print(calulator.Mod(10,20))
print(calulator.Exp(10,20))
print(calulator.str_rev("Albert"))