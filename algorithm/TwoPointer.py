"""def TwoPointer(nums, target):
    nums.sort()
    left, right = 0, len(nums)-1

    while left < right:
        curr_sum = nums[left] + nums[right]
        if curr_sum == target:
            return [nums[left], nums[right]]
        elif curr_sum < target:
            left += 1
        else:
            right -=1
    return -1

numbers = [3,4,5,6,7,2,9,8]
target = 16
result = TwoPointer(numbers, target)
print(result)

"""













def twoPointer(arr, target):
    arr.sort()
    left, right = 0, len(arr)-1

    for _ in range(right):
        curr = arr[left] + arr[right]

        if curr == target:
            return [arr[left] , arr[right]]
        elif curr > target:
            right-=1
        else:
            left+=1
    return -1

numbers = [3,4,5,6,7,2,9,8]
target = 11
result = twoPointer(numbers, target)
print(result)