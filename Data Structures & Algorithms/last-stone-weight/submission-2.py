import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # max heap
        stoneheap = [-n for n in stones]
        heapq.heapify(stoneheap)

        while len(stoneheap) > 1:
            # get largest stone
            x = -heapq.heappop(stoneheap)
            y = -heapq.heappop(stoneheap)

            if (y < x):
                heapq.heappush(stoneheap, -(x-y))
        

        return -stoneheap[0] if stoneheap else 0
            

            

