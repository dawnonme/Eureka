class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ''' Dynamic Programming
        Idea: Solutions at the i-th index can be formed by solutions at j-th index,
        (i < j). Check all js that is larger than i, if s[i:j] is a palindrome,
        then all the solutions at j-th index left append s[i:j] can be one solution
        at i.
        '''

        # store the ans for each index
        dp = [[] for _ in range(len(s) + 1)]

        # if s == '', ans = [[]]
        dp[-1] = [[]]

        # from back to start
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s) + 1):

                # if s[i:j] is a palindrome
                if s[i:j] == s[i:j][::-1]:
                    for each in dp[j]:
                        dp[i].append([s[i:j]] + each)
        
        return dp[0]