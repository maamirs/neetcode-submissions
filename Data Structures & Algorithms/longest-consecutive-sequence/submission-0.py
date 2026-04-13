class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numset= set(nums)
        result = 0
        # 1,2,3,4,100,200
        for num in numset:

            if num - 1 not in numset: # only start from sequence beginning
                length = 1
            
                while num + length in numset: # extend as far as possible
                    length += 1
                
                result = max(result, length)

        return result

        