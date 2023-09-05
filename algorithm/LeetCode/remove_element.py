class Solution:
    def removeElement(self, nums, val):
        d=[]
        for i in nums:
            if i!=val:
                d.append(i)
        return d
solution = Solution()
print(solution.removeElement([3,2,2,3], 3))


#accepted code
"""class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        
        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
        
        return left
"""