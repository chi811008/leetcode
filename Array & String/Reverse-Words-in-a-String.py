class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        head, tail = 0, len(l)-1
        
        while head < tail:
            l[head], l[tail] = l[tail], l[head]
            
            head += 1
            tail -=1
        
        return " ".join(l)