class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # [30,38,30,36,35,40,28]
        # [1,4,1,2,1,0,0]
        # find next higher number the ones remaining inside the stack havent find the next largest
        # 38 36 35 40
        # 30 38
        #  do we need a tuple

        tempstack = []
        result = [0] * len(temperatures)

        for i , x in enumerate (temperatures):
            # keep popping 
            while tempstack and temperatures[tempstack[-1]] < x:
                point = tempstack.pop() 
                # 30 0
                result[point] = i - point 
            tempstack.append(i)
        
        return result


