class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        # step = 0
        # for x in key:
        #     left = ring.find(x)
        #     right = ring.rfind(x)
        #     if left <= len(ring)-right:
        #         ring = ring[left:]+ring[:left]
        #         step += left
        #     else:
        #         ring = ring[right:]+ring[:right]
        #         step += len(ring)-right
        #     step += 1
        # return step
        def find_dist(i, j):
            return min(abs(i-j), len(ring)-abs(i-j))

        pos = {}
        for i, v in enumerate(ring):
            pos[v] = pos.get(v, []) + [i]

        cur_possible_states = {0:0}
        for x in key:
            possible_next_moves = pos[x]
            next_possible_states = {}
            for next_pos in possible_next_moves:
                tmp = float('inf')
                for cur_pos in cur_possible_states:
                    tmp = min(tmp, find_dist(cur_pos, next_pos)+cur_possible_states[cur_pos])
                next_possible_states[next_pos] = tmp
            cur_possible_states = next_possible_states

        # need to press button for every key, so add len(key)
        return min(cur_possible_states.values()) + len(key)


a = Solution()
print a.findRotateSteps("godding", "gd")
print a.findRotateSteps("iotfo", "fioot")