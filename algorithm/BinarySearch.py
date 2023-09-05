def BinSearch(arr, target):
    low, high = 0, len(arr)-1
    for i in range(high):
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid -1
    return -1

arr = [1,9,2,8,3,7,4,6,5]
target = 3
print(BinSearch(arr, target))