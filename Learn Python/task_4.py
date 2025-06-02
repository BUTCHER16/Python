class task4:

    def lora(self):
        total_sum = 0
        for i in range(1, 101):
            if i % 7 ==0:
                continue
            elif i == 90:
                break
            elif i % 2 == 0:   
                total_sum += i
                print("Even", i)
            else:
                print("Odd", i)
        return total_sum

    

t = task4()

print(t.lora())