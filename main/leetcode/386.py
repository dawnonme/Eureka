class Solution:
    # def lexicalOrder(self, n: int) -> List[int]:
    #     self.output = []
    #     self.dfs(n, 1)
    #     return self.output

    # def dfs(self, n, cur):
    #     if cur > n:
    #         return
    #     self.output.append(cur)
    #     self.dfs(n, cur * 10)
    #     if cur % 10 < 9:
    #         self.dfs(n, cur + 1)
    def lexicalOrder(self, n: int) -> List[int]:
        ans = [1]
        while len(ans) < n:
            new = ans[-1] * 10
            while new > n:
                new //= 10
                new += 1
                # deal with case like 199+1=200 when we need to restart from 2.
                while new % 10 == 0:
                    new //= 10
            ans.append(new)
        return ans
