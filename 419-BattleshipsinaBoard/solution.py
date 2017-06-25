class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == 'X':
                    if x == 0 and y == 0:
                        count = count + 1
                    elif x == 0 and board[x][y-1] != 'X':
                        count = count + 1
                    elif y == 0 and board[x-1][y] != 'X':
                        count = count + 1
                    elif board[x-1][y] != 'X' and board[x][y-1] != 'X':
                        count = count + 1
        return count

a = Solution()
print a.countBattleships(["X..X","...X","...X"])