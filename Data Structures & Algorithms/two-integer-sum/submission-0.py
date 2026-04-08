class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        hashmap = {}

        for i, x in enumerate (nums):
            tofind = target - x
            if tofind in hashmap:
                return [hashmap[tofind], i]
            hashmap[x] = i
        
        return []
        