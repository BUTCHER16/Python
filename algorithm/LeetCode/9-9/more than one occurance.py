class Solution:
    def search(self, nums, target):
        result = []
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = l + (r - l) // 2
            if target == nums[m]:
                result.append(m)
                l = m + 1  # Move left pointer to find other occurrences
            elif target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
        
        return result if result else [-1]  # Return -1 if no occurrences are found

nums = [3,3]
target = 2
solution = Solution()
print(solution.search(nums, target))