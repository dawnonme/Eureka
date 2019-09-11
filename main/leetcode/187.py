class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        table = {}
        res = []
        for i in range(len(s) - 9):
            pattern = s[i:i + 10]
            if pattern in table and table[pattern]:
                res.append(pattern)
                table[pattern] = False
            elif pattern not in table:
                table[pattern] = True
        return res