class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        right = len(numbers) - 1
        left = 0 

        while left <= right:
            targetsum = numbers[right] + numbers[left]
            if (targetsum == target):
                return [left+1, right+1]
                # 5 < 3
            elif (targetsum < target):
                left +=1
            else:
                right-=1
        
        return []
        