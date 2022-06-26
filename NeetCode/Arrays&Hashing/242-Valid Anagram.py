class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap1 = [0] * 26
        hashmap2 = [0] * 26
        for i in range(len(s)):
            hashmap1[(ord(s[i]) - 97)] = hashmap1[(ord(s[i]) - 97)] + 1
            hashmap2[(ord(t[i]) - 97)] = hashmap2[(ord(t[i]) - 97)] + 1
        if hashmap1 == hashmap2:
            return True
        else:
            return False

s = "rat"
t = "car"
if len(s) != len(t):
    print(False, "len")
hashmap1 = [0] * 26
hashmap2 = [0] * 26
for i in range(len(s)):
    print(s[i], t[i])
    print((ord(s[i]) - 97))
    print((ord(t[i]) - 97))
    hashmap1[(ord(s[i]) - 97)] += 1
    hashmap2[(ord(t[i]) - 97)] += 1
    print(hashmap2, hashmap1)
if hashmap1 == hashmap2:
    print(True)
else:
    print(False, "diff")