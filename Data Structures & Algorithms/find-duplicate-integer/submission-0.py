class Solution:
    def findDuplicate(self, nums: List[int]) -> int:


        # hashmap ={}

        # for n in nums:
        #     hashmap[n] = hashmap.get(n,0) + 1
        
        # for i in range(len(nums)):
        #     if hashmap[nums[i]] > 1:
        #         return nums[i]
            
        # return -1


        seen = set()

        for n in nums:
            if n in seen:
                return n
            seen.add(n)
        
        return -1