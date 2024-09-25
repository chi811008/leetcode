class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for ele in tokens:
            if ele not in ["+", "-", "*", "/"]:
                nums.append(int(ele))
                continue
            
            num2 = nums.pop()
            num1 = nums.pop()
            
            if ele == "+":
                res = num1 + num2
            elif ele == "-":
                res = num1 - num2
            elif ele == "*":
                res = num1 * num2
            elif ele == "/":
                res = int(num1 / num2)
            
            nums.append(res)
        
        return nums[0]