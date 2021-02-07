class Solution:
    def isValidSudoku(self, board):
        rows=[[],[],[],[],[],[],[],[],[]]
        cols=[[],[],[],[],[],[],[],[],[]]
        box=[[],[],[],[],[],[],[],[],[]]
        for i in range(9):
            for j in range(9):
                temp=board[i][j]
                if temp=='.':
                    continue
                if temp not in rows[i]:
                    rows[i].append(temp)
                else:
                    return False
                if temp not in cols[j]:
                    cols[j].append(temp)
                else:
                    return False
                boxno=3*(i//3)+j//3
                if temp not in box[boxno]:
                    box[boxno].append(temp)
                else:
                    return False
        return True
