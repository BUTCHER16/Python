tup = ('apple', 'orange', 'banana', 'pomogranate', 'grape')

#tup(2) == 'albert'
#print(tup[2],tup[4])
#print(tup[0:3])


set1 = {1,2,3,4,5}
set2 = {4,5,6,7}

#set1.add(18)
#print(set1.union(set2))
#print(set1.intersection(set2))
#print(set1.difference(set2))

employees = {"Albert": 35000, "Ravidoss": 40000}

employees['Justie'] = 56000

employees["Albert"] = 45000

for a,b in employees.items():
    print(f"{a} : {b}")

print(employees.get("Albert"))

print(employees.get("Ravidoss"))

