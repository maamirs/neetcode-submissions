class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = {}

        for x in nums:
            hashmap[x] = hashmap.get(x, 0) + 1
        
        # use maxheap
        # data = []
        # for val in hashmap:
        #     tuplles = (-hashmap[val], val)
        #     data.append(tuplles)


        # heapq.heapify(data)
        # result = []
        # for i in range(k):
        #     count,value = heapq.heappop(data)
        #     result.append(value)
        # return result

        freq = [ [] for i in range  (len(nums) + 1) ]

        for val, count in hashmap.items():
            freq[count].append(val)

        result = []
        for i in range ( len(freq) -1 ,0, -1):
            for x in freq[i]:
                result.append(x)
                if len(result) == k:
                    return result



