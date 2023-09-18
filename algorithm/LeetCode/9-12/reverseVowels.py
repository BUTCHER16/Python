def revVow(s):
    s = list(s)
    low, high = 0, len(s)-1
    v = "aeiouAEIOU"
    while low < high:
        while low < high and s[low] not in v: low+=1
        while low < high and s[high] not in v: high-=1
        s[low], s[high] = s[high], s[low]
        low+=1
        high-=1
    return "".join(s)        




print(revVow(s = "hello"))

13/09/23 - 15/09/23