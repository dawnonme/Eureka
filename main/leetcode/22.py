class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.n = n
        self.backtrack('', 0, 0)
        return self.res
    

    def backtrack(self, cur, open, close):
        if len(cur) == 2 * self.n:
            self.res.append(cur)
            return
        if open < self.n:
            self.backtrack(cur + '(', open + 1, close)
        if close < open:
            self.backtrack(cur + ')', open, close + 1)
