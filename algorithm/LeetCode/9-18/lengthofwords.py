class Solution:
    def lenWords(self, s):
        words = s.split()
        return len(words[-1])

solution = Solution()
print(solution.lenWords(s ="Hello World"))