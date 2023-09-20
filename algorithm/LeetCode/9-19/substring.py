#accepted
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_ptr, t_ptr = 0, 0
        while s_ptr < len(s) and t_ptr < len(t):
            if s[s_ptr] == t[t_ptr]:
                s_ptr += 1
            t_ptr +=1
        return s_ptr == len(s) 

"""class Solution:
    def isSubsequence(self, s, t):
        result = False
        for i in s:
            if i in t:
                result = True
            else:
                result = False
                break
        return result"""
solution = Solution()
print(solution.isSubsequence(s = "aa", t = "aab"))
