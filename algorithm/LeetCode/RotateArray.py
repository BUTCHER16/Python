class Solution:
    def rotate(self, nums, k):
        return nums[-k:] + nums[:-k]
    
solution = Solution()
print(solution.rotate(nums=[-1,-100,3,99], k=2))


#accepted format
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]