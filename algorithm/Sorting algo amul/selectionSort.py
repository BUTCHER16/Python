print("For min  list")
list = [56, 3, 2, 78, 6, 0]
print(list)

for i in range(len(list)):
    min_val = min(list[i:])
    min_ind = list.index(min_val)
    list[i], list[min_ind] = list[min_ind], list[i]
print(list)

#for max order
print("\nFor max list")
list = [56, 3, 2, 78, 6, 0]
print(list)

for i in range(len(list)):
    max_val = max(list[i:])
    max_ind = list.index(max_val)
    list[i], list[max_ind] = list[max_ind], list[i]
print(list)


#For duplicates in the list

print('\nFor duplicate values in list')
list = [56, 3, 2, 78, 0, 0]
print(list)

for i in range(len(list)):
    min_val = min(list[i:])
    min_ind = list.index(min_val, i)
    list[i], list[min_ind] = list[min_ind], list[i]
print(list)

#if you want all the iteration
print('\nFor all the iterations list')
list = [56, 3, 2, 78, 0, 0]
print(list)

for i in range(len(list)):
    min_val = min(list[i:])
    min_ind = list.index(min_val, i)
    list[i], list[min_ind] = list[min_ind], list[i]
    print(list)

