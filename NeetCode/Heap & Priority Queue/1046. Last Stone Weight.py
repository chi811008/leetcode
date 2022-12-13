import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [ -s for s in stones]
        heapq.heapify(stones)
        print(stones)
        while len(stones) > 1:
            first = heapq.heappop(stones) # -8
            second = heapq.heappop(stones) # -7
            if second > first:
                heapq.heappush(stones, first - second)
        stones.append(0)
        return abs(stones[0])

s = Solution()
l = [2,7,4,1,8,1]
ans = s.lastStoneWeight(l)
print(ans)