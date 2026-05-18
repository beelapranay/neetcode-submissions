class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i, j = 0, 0
        while j < len(s):
            if s[j] == "#":
                length = int(s[i:j])
                res.append(s[j + 1: j + 1 + length])
                i = j = j + 1 + length
            else:
                j += 1
        
        return res

