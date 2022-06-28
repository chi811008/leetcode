from collections import defaultdict


# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         hash_map = dict()      
#         for element in strs:
#             tmp_map = [0] * 26
#             for charactor in element:
#                 tmp_map[ord(charactor) - 97] += 1
#             val = hash_map.get(tuple(tmp_map), [])
#             val.append(element)
#             hash_map[tuple(tmp_map)] = val
#         return [v for v in hash_map.values()]

strs = ["eat","tea","tan","ate","nat","bat"]
hash_map = defaultdict(list)      
for element in strs:
    tmp_map = [0] * 26
    for charactor in element:
        tmp_map[ord(charactor) - 97] += 1
    val = hash_map.get(tuple(tmp_map), [])
    val.append(element)
    hash_map[tuple(tmp_map)] = val
ans = [v for v in hash_map.values()]
print(ans)