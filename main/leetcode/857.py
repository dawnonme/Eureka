class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        
        workers = []
        for i in range(len(quality)):
            workers.append((wage[i] / quality[i], quality[i]))
        workers.sort(key=lambda x: x[0])
        
        ans = float('inf')
        pool = []
        sumq = 0
        for ratio, q in workers:
            heapq.heappush(pool, -q)
            sumq += q

            if len(pool) > K:
                sumq += heapq.heappop(pool)

            if len(pool) == K:
                ans = min(ans, ratio * sumq)

        return float(ans)
