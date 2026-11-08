class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freqDiff = collections.defaultdict(int)
        for s_i, t_i in zip(s, t):
            freqDiff[s_i] += 1
            freqDiff[t_i] -= 1

        for c in freqDiff:
            if freqDiff[c] != 0:
                return False
        return True
        