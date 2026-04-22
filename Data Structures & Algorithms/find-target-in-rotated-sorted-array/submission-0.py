class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # 3,4,5,6,7,0 1 2 3 4
        # if the side is sorted, see if target exists in that range, 
        # if it does i do binary search on it, 
        # else it is not on the sorted side and we switch sides, and do binary search on that?

        left = 0 
        right = len(nums) - 1


        while left <= right:
            mid = left +(right - left) // 2

            if target == nums[mid]:
                return mid
            # check which side is sorted
            if nums[mid] <= nums[right]:
                # it is sorted now find if the target exists here
                if target >= nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                # this side is sorted
                if target >= nums[left] and target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1


        return -1


        