class Solution:
    def isPalindrome(self, s: str) -> bool:
        head, tail = 0, len(s) - 1
        while head < tail:
            if self.is_alpha_num(s[head]):
                if self.is_alpha_num(s[tail]):
                    if s[head].lower() != s[tail].lower():
                        return False
                    head += 1
                    tail -= 1
                else:
                    tail -= 1
            else:
                head += 1
        return True

    def is_alpha_num(self, c):
        return (ord("A") <= ord(c) <= ord("Z")) or (ord("a") <= ord(c) <= ord("z")) or (ord("0") <= ord(c) <= ord("9"))