class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(strs) + "#" + ",".join([str(len(s)) for s in strs])

    def decode(self, s: str) -> List[str]:
        splitIndex = len(s) - s[::-1].find("#") - 1
        lengths = s[splitIndex + 1:].split(",") if splitIndex != len(s) - 1 else []
        res = []
        start = 0
        for l in lengths:
            res.append("".join(s[start: start + int(l)]))
            start += int(l)

        return res
