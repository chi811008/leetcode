class Solution:
    def reverseWords(self, s: str) -> str:
        
        def reverse(head, tail, l):
            
            while head < tail:
                l[head], l[tail] = l[tail], l[head]
                head += 1
                tail -= 1
        
        l = list(s)
        start = 0
        for i in range(len(l)):
            if l[i] == " ":
                reverse(start, i-1, l)
                start = i + 1
        reverse(start, len(l)-1, l)
        
        return "".join(l)

def runTest():
	s = "Let's take LeetCode contest"
	sol = Solution()
	print(sol.reverseWords(s))

if __name__ == "__main__":
	runTest()
