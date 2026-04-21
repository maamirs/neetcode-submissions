class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        result = nums[0]

        while left <= right:
            mid = left + (right - left) // 2
            result = min(result, nums[mid])

            if nums[mid] <= nums[right]:
                right = mid - 1       # right half sorted — go left
            else:
                left = mid + 1        # left half sorted — go right

        return result
