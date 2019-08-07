class Solution:
    def num_squares_dp(self, n: int) -> int:
        dp = [0]
        num = 1
        for i in range(1, n + 1):
            if i == num**2:
                dp.append(1)
                num += 1
            else:
                dp.append(
                    min([dp[i - j**2] for j in range(1,
                                                     int(i**0.5) + 1)]) + 1)
        return dp[n]

    def num_squares_bfs(self, n):
        #TODO
        set_power = set()
        cnt = 1
        while cnt * cnt <= n:
            cntsq = cnt * cnt
            if cntsq == n: return 1
            set_power.add(cntsq)
            cnt += 1
        level = 1
        same_Level_nodes = {n}
        while same_Level_nodes:
            tmp = set()
            for e in same_Level_nodes:
                for p in set_power:
                    if e - p in set_power:
                        return level + 1
                    if e - p >= 0:
                        tmp.add(e - p)
            same_Level_nodes = tmp
            level += 1
        return level
