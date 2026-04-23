from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        # key: value []
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp, value])


        

    def get(self, key: str, timestamp: int) -> str:

        left = 0 
        array = self.store[key]
        # array = [[1, bar] [4, bar2]]
        # not sorted 
        # 5 6 7 2 1 4 5
        right = len(array) - 1
        result = ''
        while left <= right:

            mid = left + (right - left) // 2

            if (array[mid][0]<= timestamp):
                result =  array[mid][1]
                left = mid + 1
            else:
                right = mid - 1
            
        
        return result

        


# key value timestamp
# for key i should get the value for the timestamp that is less than or equal to it

# foo bar 1
# foo 3 -> bar            
#     bar2 4 
# foo 6  -> bar2


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)