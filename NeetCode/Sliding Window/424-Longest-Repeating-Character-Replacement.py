from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxlength = 0
        character_frequence = defaultdict(int)
        maxf = 0
        for r in range(len(s)):
            character_frequence[s[r]] += 1
            maxf = max(maxf, character_frequence[s[r]])
            while (r - l + 1) - maxf > k:
                character_frequence[s[l]] -= 1
                l += 1
            maxlength = max(maxlength, r - l + 1)
        return maxlength