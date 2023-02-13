class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)
        
        def find_parent(n):
            p = parent[n]
            while p != parent[p]:
                parent[n] = parent[p]
                p = parent[parent[p]]
            return p
        
        def union(n1, n2):
            p1, p2 = find_parent(n1), find_parent(n2)
            if p1 == p2:
                return False
            elif rank[p1] > rank[p2]:
                parent[p2] = parent[p1]
                rank[p1] += rank[p2]
            else:
                parent[p1] = parent[p2]
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]


edges = [[1,5],[3,4],[3,5],[4,5],[2,4]]

parent = [i for i in range(len(edges) + 1)]
print(parent)
rank = [1] * (len(edges) + 1)
print(rank)
        
def find_parent(n):
    p = parent[n]
    while p != parent[p]:
        parent[n] = parent[p]
        p = parent[parent[p]]
    return p
        
def union(n1, n2):
    p1, p2 = find_parent(n1), find_parent(n2)
    if p1 == p2:
        return False
    elif rank[p1] > rank[p2]:
        parent[p2] = p1
        rank[p1] += rank[p2]
    else:
        parent[p1] = p2
        rank[p2] += rank[p1]
    return True

for n1, n2 in edges:
    if not union(n1, n2):
        print([n1, n2]) 

print(parent)
print(rank)