class task5:
    def Comp(self):

        rang = [x for x in range(1, 21)]
        even = []
        odd = []
        Three = []

        for i in rang:
            if i % 3 == 0:
                Three.append(i)
            elif i%2==0:
                even.append(i)
            else:
                odd.append(i)
        
        addnum = int(input("Enter the Number: "))
        rang.append(addnum)

        remnum = int(input("Enter the Number to Remove: "))
        rang.remove(remnum)

        
        return f"Full List {list(reversed(rang))}, Even Numbers {even}, Odd Numbers {odd}, Number Divisible bye 3 {Three}"
    

t = task5()
print(t.Comp())