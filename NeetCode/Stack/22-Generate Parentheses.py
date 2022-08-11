n = 3
ans = ["((()))","(()())","(())()","()(())","()()()"]
openN = 0
closeN = 0
stack = []
res = []

def backtracking(openN, closeN):
    if openN == closeN == n:
        print("openN == closeN == n")
        print(f"0 {stack}")
        ans = "".join(stack)
        res.append(ans)
        print(res)
        return res
    
    if openN < n:
        print("enter openN")
        stack.append("(")
        print(f"1 {stack}")
        backtracking(openN + 1, closeN)
        print(f"2 {stack}")
        stack.pop()
        print(f"3 {stack}")
    
    if closeN < openN:
        print("enter closeN")
        stack.append(")")
        print(f"4 {stack}")
        backtracking(openN, closeN + 1)
        print(f"5 {stack}")
        stack.pop()
        print(f"6 {stack}")

backtracking(0, 0)
print(res)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        openN = 0
        closeN = 0
        stack = []
        res = []

        def backtracking(openN, closeN):
            if openN == closeN == n:
                ans = "".join(stack)
                res.append(ans)
                return res

            if openN < n:
                stack.append("(")
                backtracking(openN + 1, closeN)
                stack.pop()

            if closeN < openN:
                stack.append(")")
                backtracking(openN, closeN + 1)
                stack.pop()

        backtracking(0, 0)
        return res