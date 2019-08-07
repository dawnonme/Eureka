import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = []
        dic = Counter(words)
        for w, v in dic.items():
            heap.append((-v, w))
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for i in range(k)]
        