class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search

        right = len(nums) -1
        left = 0

        while left <= right:
            mid = left + (right - left) // 2
            if (target == nums[mid]):
                return mid
            # 4 > 2
            elif (target > nums[mid]):
                left = mid + 1
            else:
                right = mid - 1
            
        
        return -1
