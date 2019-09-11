class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack, ans = [], [0] * len(T)
        for i, t in enumerate(T):
            while stack and stack[-1][0] < t:
                _, idx = stack.pop()
                ans[idx] = i - idx
            stack.append((t, i))
        return ans