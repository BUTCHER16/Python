class Solution:
    def longestCommonPrefix(self, strs):
        min_len = min(len(s) for s in strs)
        pre =''
        for i in range(min_len):
            if all(s[i] == strs[0][i] for s in strs):
                pre += strs[0][i]
            else:
                break
        return pre



solution = Solution()
print(solution.longestCommonPrefix(strs = ["cir", "car"]))