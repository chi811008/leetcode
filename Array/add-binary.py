class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        aList = [int(n) for n in a]
        bList = [int(n) for n in b]
        
        if len(aList) > len(bList):
            l = len(bList)
            res = aList
        else:
            l = len(aList)
            res = bList
            
        advance = 0
        for i in range(1, l+1):
            res[-i] = aList[-i] + bList[-i] + advance
            advance = 0
            if res[-i] >= 2:
                res[-i] %= 2
                advance = 1
        while advance:
            if l == len(res):
                res[-l] %=2
                res.insert(0, 1)
                advance = 0
                
            else:
                res[-(l+1)] += 1
                advance = 0
                if res[-(l+1)] >= 2:
                    res[-(l+1)] %= 2
                    advance = 1
                    l += 1
        return "".join([str(n) for n in res])
