class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
            }
        
        res = []
        def backtracking(i, currStr):
            if len(currStr) == len(digits):
                res.append(currStr)
                return
            
            for c in digitToChar[digits[i]]:
                backtracking(i+1, currStr+c) 
        
        if digits:
            backtracking(0, "")
        return res

def runTest():
    digits = ""
    sol = Solution()
    print(sol.letterCombinations(digits))
    
if __name__ == "__main__":
    runTest()
                