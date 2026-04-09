class Solution:
    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    #     hashmaprow = [0] *10
    #     hashmapcol = [0] *10

    #     for i in range (9):
    #         hashmaprow = [0] *10
    #         for j in range (9):
    #             val = board[i][j]
    #             if val.isnumeric():
    #                  hashmaprow[int(val)] +=1
    #             if val.isnumeric() and hashmaprow[int(val)] >= 2:
    #                 return False

    #     for i in range (9):
    #         hashmapcol = [0] *10
    #         for j in range (9):
    #             val = board[j][i]
    #             if val.isnumeric():
    #                  hashmapcol[int(val)] +=1
    #             if val.isnumeric() and hashmapcol[int(val)] >= 2:
    #                 return False

    #         maps = [0] * 10
    #     for i in range (0,9,3):
    #         for j in range (0,9,3):
    #             maps = [0] * 10
    #             for x in range(i,i+3):
    #                 for y in range (j, j+3):
    #                     val = board[x][y]
    #                     if val.isnumeric():
    #                         maps[int(val)] +=1
    #                         if maps[int(val)] >= 2:
    #                             return False

    #     return True
    def isValidSudoku(self, board):
        rows    = [set() for _ in range(9)]
        cols    = [set() for _ in range(9)]
        boxes   = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue

                box_index = (i // 3) * 3 + (j // 3)

                if val in rows[i] or val in cols[j] or val in boxes[box_index]:
                    return False

                rows[i].add(val)
                cols[j].add(val)
                boxes[box_index].add(val)

        return True
            



        