class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        isAlphaNumeric = lambda c: (ord("a") <= ord(c) <= ord("z")) or (ord("A") <= ord(c) <= ord("Z")) or (ord("0") <= ord(c) <= ord("9"))

        while i < j:
            if not isAlphaNumeric(s[i]):
                i += 1
                continue

            if not isAlphaNumeric(s[j]):
                j -= 1
                continue

            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
                continue

            return False

        return True
        