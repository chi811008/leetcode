from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for ele in strs:
            ele_map = [0] * 26
            for c in ele:
                ele_map[ord(c) - ord("a")] += 1
            ele_map = tuple(ele_map)
            anagram_map[ele_map].append(ele)
        return [v for v in anagram_map.values()]