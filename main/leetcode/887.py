class Solution:
    def superEggDrop(self, K: int, N: int) -> int:

        """
        dp[i][j]: The minimum number of operations needed to figure out the value of F with
        i eggs and j floors. As one can always try with one egg with floor sequence 1, 2, ...
        to get the value of F, all the entries in dp are initialized with N - 1. Our final 
        answer is dp[K][N].
        """
        dp = [[N - 1] * (N + 1) for _ in range(K + 1)]

        """
        To build the dp table, we need to figure out the state transition function.
        If we try to drop the egg from the n-th floor (n <= N), if the egg 
        """

        return dp[K][N]
