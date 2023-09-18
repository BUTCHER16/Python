class Solution:
    def merge(self, nums1,nums2) -> None:
        num1 = []
        num2 = []
        for i in nums1:
            if i >= 1:
                num1.append(i)
        for j in nums2:
            if j >= 1:
                num2.append(j)
        result = num1 + num2
        ans = sorted(result)
        return ans
solution = Solution()
nums1 = [0]
nums2 = [1]
print(solution.merge(nums1,nums2))


#leetcode Accepted code
"""class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Start from the end of both arrays
        i = m - 1
        j = n - 1
        k = m + n - 1

        # Merge nums2 into nums1 in reverse order
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If there are remaining elements in nums2, copy them to nums1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1"""
