class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        if preorder == '#':
            return True
        preorder = list(preorder.split(sep=','))
        if not preorder or preorder[0] == '#':
            return False
        stack = [[preorder[0], 0]]
        for ch in preorder[1:]:
            if ch != '#':
                if not stack:
                    return False
                stack[-1][1] += 1
                stack.append([ch, 0])
            else:
                if not stack:
                    return False
                stack[-1][1] += 1
                while stack and stack[-1][1] == 2:
                    stack.pop()
        return not stack
