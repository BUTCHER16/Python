grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
"""t = []
count = 0
for i in grid:
    for j in i:
        t.append(j)
for i in t:
    if i <=0:
        count+=1
print(count)"""
    
count = 0
for i in grid:
    for j in i:
        if j < 0:
            count += 1
print(count)