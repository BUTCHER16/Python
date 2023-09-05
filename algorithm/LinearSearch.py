#Linear search

def linear_Search(arr, num):
    for index, _ in enumerate(arr):
        if _ == num:
            return index
    return False

arr = [1,2,3,4,5]
num = 6
print(linear_Search(arr, num))