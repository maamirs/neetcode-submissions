from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            group[key].append(word)

        result = []
        for words in group:
            result.append(group[words])

        return result

        
        