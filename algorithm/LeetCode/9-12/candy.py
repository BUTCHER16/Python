class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        result = []
        max_candies = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candies:
                result.append('true')
            else:
                result.append('false')
        return result
solution = Solution()
print(solution.kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3))