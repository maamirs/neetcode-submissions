class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        n = len(nums)
        result = [1] * n

        for i in range (n):
            result[i] = prefix
            prefix = prefix * nums[i]

        suffix = 1

        for i in range(n-1, -1, -1):
            result[i] *= suffix
            suffix = suffix * nums[i]

        
        return result


        




#  1,2,3,0,4,5,0