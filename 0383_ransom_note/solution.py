class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = dict()
        for i in magazine:
            value = d.get(i, 0)
            d[i] = value + 1

        for i in ransomNote:
            if d.get(i, 0) <= 0:
                return False
            val = d.get(i, 0)
            d[i] = val - 1
        return True
