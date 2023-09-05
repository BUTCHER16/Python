from collections import Counter

"""class Solution:
    def majorityElement(self, nums):
        myCounter = Counter(nums)
        most = myCounter.most_common()

        if most:
            return most[0][0]
solution = Solution()
print(solution.majorityElement(nums=[3,2,3]))"""

#it is accepted

nums = [3,2,3]
my_counter = Counter(nums)
most = my_counter.most_common()

