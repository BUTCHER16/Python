class task3:

    def __init__(self):
        self.number = int(input("Enter the Number: "))

    def PNZ(self):
        if self.number == 0:
            return "Zero"
        elif self.number > 0 :
            return "positive"
        else:
            return "negative"
    
    def Odd_or_Even(self):
        return "Odd" if self.number % 2 !=0 else "Even"
    
    def FizzBuzz(self):
        if self.number % 3 == 0 and self.number % 5 == 0:
            return "FizzBuzz"
        if self.number % 5 == 0:
            return "Buzz"
        if self.number % 3 == 0:
            return "Fizz"
        
t = task3()

print(t.PNZ())
print(t.Odd_or_Even())
print(t.FizzBuzz())
