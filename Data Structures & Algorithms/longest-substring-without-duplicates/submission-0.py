class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        i = -1

        prevIndex = collections.defaultdict(lambda: -1)
        for j in range(0, len(s)):
            if i < prevIndex[s[j]]:
                i = prevIndex[s[j]]

            prevIndex[s[j]] = j
            res = max(res, j - i)

        return res
        