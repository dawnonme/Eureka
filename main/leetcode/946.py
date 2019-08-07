class Solution:
    def validateStackSequences(self, pushed: List[int],
                               popped: List[int]) -> bool:
        stack = []
        idx_pushed = idx_popped = 0
        while idx_pushed < len(pushed) and idx_popped < len(popped):
            if not stack or stack[-1] != popped[idx_popped]:
                stack.append(pushed[idx_pushed])
                idx_pushed += 1
            else:
                stack.pop()
                idx_popped += 1

        if idx_popped < len(popped):
            while idx_popped < len(popped):
                if not stack or popped[idx_popped] != stack[-1]:
                    return False
                idx_popped += 1
                stack.pop()

        return True