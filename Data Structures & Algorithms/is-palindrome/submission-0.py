class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join(c for c in s if c.isalnum())

        right = len(s) -1

        left = 0

        while left <= right:
            if s[left] != s[right]:
                return False
            
            right -= 1
            left += 1
        

        return True