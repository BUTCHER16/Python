class task_2:

    def __init__(self):
        self.name = input(" Enter the Name: ")

    def Uper_case(self):
        return self.name.upper()
    
    def lower_case(self):
        return self.name.lower()
    
    def cap(self):
        return self.name.capitalize()
    
    def count_the_char(self):
        full_name = self.name.replace(" ", "")
        return len(full_name)
    
    def Rev(self):
        return self.name[::-1]
    
    def Con(self):
        return True if "a" or "A" in self.name else False
    
    def Split(self):
        sp = self.name.split(" ")
        first_name = sp[0]
        last_name = sp[1]
        return f"Hello, {first_name}! You name has {len(self.name)} Characters."
    

t = task_2()

print(t.Uper_case())
print(t.lower_case())
print(t.cap())
print(t.count_the_char())
print(t.Rev())
print(t.Con())
print(t.Split())