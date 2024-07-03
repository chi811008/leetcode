class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        max_length = 0
        if len(s) == 1:
            return 1
        check = set()
        while r < len(s):
            check.add(s[l])
            if s[r] in check:
                while s[l] != s[r]:
                    check.remove(s[l])
                    l += 1
                l += 1
            else:
                check.add(s[r])
            r += 1
            if (r - l) > max_length:
                max_length = (r - l)

        return max_length

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        head = 0
        for i in range(len(s)):
            while s[i] in s[head:i]:
                head += 1
            maxLength = max(maxLength, len(s[head:i+1]))

        return maxLength