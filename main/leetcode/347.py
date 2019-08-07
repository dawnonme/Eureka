from heapq import nlargest
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        ls = list(counter.items()).sort(key=lambda x: x[1], reverse=True)
        return [tup[0] for tup in ls[:k]]

    def top_k_frequent_heap(self, nums, k):
        counter = Counter(nums)   
        return nlargest(k, counter.keys(), key=counter.get) 
