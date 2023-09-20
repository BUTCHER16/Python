"""class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove non-alphanumeric characters and convert to lowercase
        s = ''.join(filter(str.isalnum, s)).lower()
        # Check if the cleaned string is equal to its reverse
        return s == s[::-1]"""

#using two pointer
class Solution:
    def isPalindrome(self, s):
        left, right = 0, len(s)-1
        while left < right:
            while left < right and not s[left].isalnum():
                left+=1
            while left < right and not s[right].isalnum():
                right-=1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -=1
        return True 



# Example usage:
sol = Solution()
input_string = "A man, a plan, a canal: Panama"
result = sol.isPalindrome(input_string)
print(result)