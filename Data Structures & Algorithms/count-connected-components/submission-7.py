class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n
        count = n
        def find(i):
            p = par[i]
            while par[p] != p:
                par[p] = par[par[p]]
                p = par[p]
            return p
        def union(n1, n2):
            nonlocal count
            p1,p2 = find(n1), find(n2)
            if p1 == p2:
                return

            count -= 1
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]

        for edge in edges:
            union(edge[0],edge[1])
        return count