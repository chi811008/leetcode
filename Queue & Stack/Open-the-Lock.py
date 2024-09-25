from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        if "0000" in deadends:
            return -1

        def children(lock):
            res = []
            for i in range(4):
                digit = (int(lock[i]) + 1) % 10
                res.append(lock[:i]+str(digit)+lock[i+1:])
                digit = (int(lock[i]) - 1) if int(lock[i]) - 1 > -1 else 9
                res.append(lock[:i]+str(digit)+lock[i+1:])
            return res
        
        q = deque()
        q.append(["0000", 0])
        while q:
            lock, turn = q.popleft()
            
            if lock == target:
                return turn
            
            if lock not in visited:
                visited.add(lock)
                for child in children(lock):
                    q.append([child, turn+1])
        return -1