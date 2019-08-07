class Solution:
    def checkValidString(self, s: str) -> bool:
        ''' Greedy: Time (O(N)), Space (O(1))
        Idea: Keep a range of how many ( a pattern has.
        '''
        lo = hi = 0
        for c in s:
            lo += 1 if c == '(' else -1
            hi += 1 if c != ')' else -1
            if hi < 0:
                break
            lo = max(lo, 0)
        return lo == 0