class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        nums.sort()
        start = 0
        end = len(nums) - 1

        # nums = [-1,0,1,2,-1,-4]
        # [-4 -1 -1 0 1 2]

        results = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:   # skip duplicate i
                continue
            

            start = i + 1
            end = len(nums) -1
            num1 = nums[i]
            while start < end:
                target = nums[i] + nums[start] + nums[end]
                if (target == 0):
                    results.append([nums[i], nums[start], nums[end]])
                    while start < end and nums[start] == nums[start + 1]: #remove duplicate
                        start +=1
                    while start < end and nums[end] == nums[end - 1]: #remove duplicate
                        end -=1

                    end -= 1
                    start += 1

                # -4 + -1 + 2 = -3 < 0
                elif (target < 0):
                    start += 1
                else:
                    end -= 1
                
        
        return results

                