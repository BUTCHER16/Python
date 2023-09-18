class Solution:
    def searchInsert(self, nums, target):

        left, right = 0, len(nums)-1
        if target in nums:
            for i in range(right):
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        else:
            nums.append(target)
            nums.sort()
            index = nums.index(target)
            return index
"""class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1
    
        while left <= right:
            mid = (left + right) // 2
        
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    
    # If the loop finishes without finding the target, 'left' will be the correct insertion point.
        return left
"""


nums = [1]
target = 1
solution = Solution()
print(solution.searchInsert(nums, target))