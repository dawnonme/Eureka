import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        i = 1

        for num in nums:
            if i <= k:
                heapq.heappush(min_heap, num)

            else:
                if num > min_heap[0]:
                    heapq.heappushpop(min_heap, num)
            
            i += 1
        
        return min_heap[0]