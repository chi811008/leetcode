class Solution:
    def countComponentsS(self, n: int, edges: list[list[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n

        def find_parent(node):
            p = parent[node]
            while p != parent[p]:
                parent[node] = parent[p]
                p = parent[parent[p]]
            return p

        def union(n1, n2):
            p1, p2 = find_parent(n1), find_parent(n2)
            if p1 == p2:
                return 0 
            elif rank[p1] >= rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return 1
        res = n
        for n1, n2 in edges:
            n -= union(n1, n2)
        return res