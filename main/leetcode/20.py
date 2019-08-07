class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        stack = []
        l_brac = ['(', '[', '{']
        r_brac = [')', ']', '}']
        for bracket in s:
            if bracket in l_brac:
                stack.append(bracket)
            else:
                idx = r_brac.index(bracket)
                if len(stack) > 0 and stack[-1] == l_brac[idx]:
                    stack.pop()
                else:
                    return False
        return (len(stack) == 0)