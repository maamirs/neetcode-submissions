from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
                return False

        s1_count = Counter(s1)
        window_count = Counter()

        for end in range(len(s2)):
            window_count[s2[end]] += 1                      # add new character

            if end >= len(s1):                              # window is now too big — shrink
                left_char = s2[end - len(s1)]
                window_count[left_char] -= 1
                if window_count[left_char] == 0:
                    del window_count[left_char]

            if s1_count == window_count:                    # check every iteration
                return True

        return False


        