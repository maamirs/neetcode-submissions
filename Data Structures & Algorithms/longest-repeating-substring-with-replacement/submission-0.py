class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        hashmap = {}
        result = 0
        max_freq = 0


        for end in range (len(s)): 

            window_size = (end - start + 1)

            hashmap[s[end]] = hashmap.get(s[end], 0) + 1
            max_freq = max(max_freq, hashmap[s[end]])

            replacement_needed = window_size - max_freq

            if replacement_needed > k:
                hashmap[s[start]] -= 1
                start +=1


            
            result = max(result, end - start + 1 )
            

        return result