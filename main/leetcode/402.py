class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return '0'

        stack = []
        removedcount = 0
        for ch in num:
            while stack and ch < stack[-1] and removedcount < k:
                stack.pop()
                removedcount += 1
            stack.append(ch)

        for _ in range(k - removedcount):
            stack.pop()

        return str(int(''.join(stack)))