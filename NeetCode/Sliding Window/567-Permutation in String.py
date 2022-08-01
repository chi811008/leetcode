# s1 = "ab"
# s2 = "a"
# s1_map = [0] * 26
# for i in range(len(s1)):
#     s1_map[ord(s1[i]) - ord("a")] += 1
# print(s1_map)

# s2_map = [0] * 26
# for i in range(len(s1)):
#     s2_map[ord(s2[i]) - ord("a")] += 1
# if s2_map == s1_map:
#     print(True)
# else:
#     for r in range(len(s1), len(s2)):
#         s2_map[ord(s2[r - len(s1)]) - ord("a")] -= 1
#         s2_map[ord(s2[r]) - ord("a")] += 1
#         if s2_map == s1_map:
#             print(True)
#     print(False)
from nis import match


s1 = "abc"
s2 = "bbbca"
if len(s1) > len(s2):
    print(False)
s1_map = [0] * 26
for i in range(len(s1)):
    s1_map[ord(s1[i]) - ord("a")] += 1
print(s1_map)

s2_map = [0] * 26
for i in range(len(s1)):
    s2_map[ord(s2[i]) - ord("a")] += 1
# count matches
matches = 0
for c in range(26):
    if s1_map[c] == s2_map[c]:
        matches += 1
        
if matches == 26:
    print(True)
else:
    for r in range(len(s1), len(s2)):
        s2_map[ord(s2[r - len(s1)]) - ord("a")] -= 1
        if s2_map[ord(s2[r - len(s1)]) - ord("a")] == s1_map[ord(s2[r - len(s1)]) - ord("a")]:
            matches += 1
        else:
            matches -= 1
        s2_map[ord(s2[r]) - ord("a")] += 1
        if s2_map[ord(s2[r]) - ord("a")] == s1_map[ord(s2[r]) - ord("a")]:
            matches += 1
        else:
            matches -= 1
        print(s2_map)
        print(matches)
        if matches == 26:
            print(True)
    print(False)