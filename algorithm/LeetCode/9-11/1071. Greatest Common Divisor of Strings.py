from math import gcd
class Solution:
    def GCD(self, str1, str2):
        if str1 + str2 != str2 + str1:
            return ""
        max_length = gcd(len(str1), len(str2))
        print(max_length)
        return str1[:max_length]



solution = Solution()
print(solution.GCD(str1 = "LEET", str2 = "CODE"))