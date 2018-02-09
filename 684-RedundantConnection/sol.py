class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        parent = {}
        def find_root(v):
            return find_root(parent[v]) if v in parent else v

        for ind, edge in enumerate(edges):
            r1, r2 = (find_root(edge[0]), find_root(edge[1]))
            if r1 == r2:
                return edge
            else:
                print r1, r2
                parent[r1] = parent[r2] = str(ind)
                print parent

a = Solution()
print a.findRedundantConnection([[1,2],[1,3],[2,3]])