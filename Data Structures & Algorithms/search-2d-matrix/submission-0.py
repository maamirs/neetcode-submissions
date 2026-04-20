class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #  ordered 
        # get target, 
        # matrix =  [[1,3,5,7],
        #           [10,11,16,20],
        #           [23,30,34,60]],

        rowsend = len(matrix) -1
        rowsbegin = 0
        colsend = len(matrix[0]) -1
        colsbegin = 0

        while rowsbegin <= rowsend:
            mid = rowsbegin + (rowsend - rowsbegin) // 2
            targetcolumn = matrix[mid]

            if target >= targetcolumn[0] and target <= targetcolumn[colsend]:
                # target is in this column
                # do binary search again
                right = colsend
                left = 0
                while left <= right:
                    colmid = left + (right - left)//2
                    if target == targetcolumn[colmid]:
                        return True
                        # 16 > 11
                    elif target > targetcolumn[colmid]:
                        left = colmid + 1
                    else:
                        right = colmid - 1
                return False

            elif  target < targetcolumn[0]:
                rowsend = mid - 1
            else:
                rowsbegin = mid + 1
        

        return False



        


