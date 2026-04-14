class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            
        start = 0
        result = 0
        window = set()

        # "pwwkew"
        # p
        # pw
        # 
        # 
        # 
        # 
        # 

        for end in range (len(s)):
            while s[end] in window:
                window.remove(s[start])
                start += 1
                
            window.add(s[end])
            result = max(result, len(window))

        return result

        