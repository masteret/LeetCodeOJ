"""
Define all possible moves
convert array to str
create a dict for seen, key=str board_state, val=int min_move
create a list for queue of pair, (str board_state, int index_of_0)
while (queue is not empty and queue[0] is not 123450):
    for move in possible moves:
        new_board_state = q[0][0]
        # swap zero to a possible location
        swap(new_board_state[q[0][1]], new_board_state[q[0][move]])
        if new_board_state not in seen:
            seen[new_board_state] = seen[q[0][0]]+1
            queue.append((new_board_state, move))
return -1 if q is empty else seen[q[0][0]]
"""

class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        possible_moves = {0: [1,3], 1: [0,2,4], 2: [1,5], 3: [0,4], 4: [1,3,5], 5: [2,4]}
        state = "".join([str(x) for x in board[0]]) + "".join([str(x) for x in board[1]])
        
        seen = {state: 0}
        q = [[state, state.find("0")]]

        while q and q[0][0] != "123450":
            cur = q.pop(0)
            for move in possible_moves[cur[1]]:
                new_state = [int(x) for x in cur[0]]
                new_state[cur[1]], new_state[move] = new_state[move], new_state[cur[1]]
                new_state = "".join([str(x) for x in new_state])
                if new_state not in seen:
                    seen[new_state] = seen[cur[0]]+1
                    q.append([new_state, move])
        return -1 if not q else seen[q[0][0]]