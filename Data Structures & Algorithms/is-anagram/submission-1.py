class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqDiff = collections.defaultdict(int)
        for s_i in s:
            freqDiff[s_i] += 1
        
        for t_i in t:
            freqDiff[t_i] -= 1

        for c in freqDiff:
            if freqDiff[c] != 0:
                return False

        return True
        