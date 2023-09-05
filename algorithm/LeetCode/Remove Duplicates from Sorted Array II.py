"""def removeDuplicate(nums):
    if len(nums) <=2:
        return len(nums)
    
    i=2
    for j in range(2, len(nums)):
        if nums[j] != nums[i-2]:
            nums[i] = nums[j]
            i+=1
    return i
print(removeDuplicate(nums=[1,1,1,2,2,3]))"""

class Solution:
    def removeDuplicates(self, nums):
        if len(nums) <= 2:
            return len(nums)

        i = 2  # Start from the third element
        for j in range(2, len(nums)):
            if nums[j] != nums[i - 2]: # for the first iteration that is nums[2] != nums[0] the next will be done and the 
                nums[i] = nums[j]
                i += 1

        return i
solution = Solution()
print(solution.removeDuplicates(nums=[1,1,1,2,2,3]
))