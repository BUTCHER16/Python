class Solution:
    def move_zeros(self, nums):
        left, right = 0, 0

        while right < len(nums):
            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1
            right +=1
        
        while left < len(nums):
            nums[left] = 0
            left+=1
        
        return nums
    
solution = Solution()
print(solution.move_zeros(nums=[1,0,1,0,2]))