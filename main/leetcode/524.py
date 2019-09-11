class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:

        d_copy = d[:]
        ans = ''

        for ch in s:
            for i in range(len(d_copy)):
                if d_copy[i] and d_copy[i][0] == ch:
                    d_copy[i] = d_copy[i][1:]
                    if not d_copy[i]:
                        if len(d[i]) > len(ans):
                            ans = d[i]
                        elif len(d[i]) == len(ans) and d[i][0] < ans[0]:
                            ans = d[i]
        
        return ans