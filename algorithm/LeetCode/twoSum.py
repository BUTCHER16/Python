"""class Solution:
    def twoSum(self, nums, target):
        num_indices = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_indices:
                return [num_indices[complement], i]
            num_indices[num] = i
        return []
"""
class Solution:
    def twoSum(self, nums, target):
        nums_indices = {}
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in nums_indices:
                return [nums_indices[compliment], i]
            nums_indices[num] = i
        return []
    
solution = Solution()
print(solution.twoSum(nums=[2,4,6,8,4],target=14))