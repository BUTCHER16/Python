class Solution:
    def removeDuplicates(self, nums) :
        set1 = set(nums)
        l1=list(set1)
        l2=[]
        for i in l1:
            l2.append(i)
        print(l2)
solution = Solution()
solution.removeDuplicates(nums = [1,1,2])

# accepted 
"""class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0  # Handle the case where nums is empty

        # Initialize two pointers, one for iterating and one for insertion
        i = 0

        # Iterate through the list starting from the second element
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1  # The length of the modified list"""