class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)

        if l2 < l1:
            return False

        freqS1 = collections.defaultdict(int)
        freqS2 = collections.defaultdict(int)

        charSet = set(s1)

        for i in range(0, l2):
            if i < l1:
                freqS1[s1[i]] += 1
            else:
                if all([freqS1[c] == freqS2[c] for c in charSet]):
                    return True

                freqS2[s2[i - l1]] -= 1

            freqS2[s2[i]] += 1

        return all([freqS1[c] == freqS2[c] for c in charSet])
