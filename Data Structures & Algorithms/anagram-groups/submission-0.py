class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram2Group = collections.defaultdict(list)

        for s in strs:
            anagram2Group["".join(sorted(s))].append(s)

        return list(anagram2Group.values())
        