''' Longest Valid Parentheses '''


class Solution:
    def longest_valid_parentheses_dp(self, s):
        ''' Dynamic Programming: Time: O(n), Space: O(n)
        Idea: 
            Define dp[i] = Length of the longest sub-string which ends at i-th index.
            Then:
                1. dp[i] = 0 if s[i] == '(' because it won't be a valid string
                2. dp[i] = dp[i - 2] + 2 if s[i] == ')' and s[i - i] == '('
                3. dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2 if s[i] == s[i - 1] == ')' and
                    s[i - dp[i - 1] - 1] == '(' because s[i] will be matched to a '(' which occurs
                    before at index i - dp[i - 1] - 1
        '''
        dp, ans = [0] * len(s), 0
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2 if i >= 2 else 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + (dp[i - dp[i - 1] - 2]
                                         if i - dp[i - 1] >= 2 else 0) + 2
                ans = max(ans, dp[i])
        return ans

    def longest_valid_parentheses_stack(self, s: str) -> int:
        ''' Stack: Time: O(n), Space: O(n)
        Idea: Keep a stack with initial element -1. Check each character in s.
            1. c == '(', push the index to the stack
            2. c == ')', pop the top element from stack
                2.1. stack is empty after popping, push the index to the stack
                2.2. stack is not empty, update the max length of the sub-string
        '''
        stack, ans = [-1], 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                # can be treated as a ) will match the nearest (
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    # calculate the length of new string, which is current index - top of stack index
                    ans = max(ans, i - stack[-1])
        return ans

    def longest_valid_parentheses_constant_space(self, s):
        ''' Two Pass Constant Space: Time: O(n), Space: O(1)
        Idea: Do a left-to-right scan and the do a right-to-left scan.
        '''
        l, r, ans = 0, 0, 0

        # left-to-right scan
        for i in range(len(s)):
            if s[i] == '(':
                l += 1
            else:
                r += 1
            if l == r:
                ans = max(ans, 2 * r)
            elif l <= r:
                l, r = 0, 0

        l, r = 0, 0

        # right-to-left scan
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':
                l += 1
            else:
                r += 1
            if l == r:
                ans = max(ans, 2 * l)
            elif l >= r:
                l, r = 0, 0

        return ans