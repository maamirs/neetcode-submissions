class Solution:
    def maxArea(self, height: List[int]) -> int:

        area = 0

        start = 0
        end = len(height) - 1

        while start <= end:
            width = min(height[start], height[end])
            length = end - start
            area = max(area, length * width)
            # 1 < 7
            if(height[start] < height[end]):
                start +=1
            else:
                end -= 1

        
        return area
            
        