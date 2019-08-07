import heapq


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity

        # main hash map to store the keys and values
        self.dic = {}

        # number of the elements in dic
        self.occupied = 0

        # frequency of all the key
        self.count = {}

        # a heap to retrieve the smallest occurred element
        self.heap = []

        # time for an element to be used last time
        self.time = {}

        # current time, for setting the time hash map
        self.curtime = 0

    def get(self, key: int) -> int:
        if self.capacity == 0:
            return -1

        if key in self.dic:
            self.count[key] += 1
            self.time[key] = self.curtime
        self.curtime += 1

        return (self.dic.get(key, -1))

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic[key] = value
            self.count[key] += 1
            self.time[key] = self.curtime
            return

        if self.capacity == 0:
            return

        if self.capacity <= self.occupied:
            # count, time, key
            (c, t, k) = heapq.heappop(self.heap)

            # when pushed to the heap, the tuple will be first sorted by the freq and then the last occurred time
            while c < self.count[k] or t < self.time[k]:
                heapq.heappush(self.heap, (self.count[k], self.time[k], k))
                (c, t, k) = heapq.heappop(self.heap)
            del self.dic[k]
            del self.count[k]
            del self.time[k]
        else:
            self.occupied += 1

        self.dic[key] = value
        self.count[key] = 1
        self.time[key] = self.curtime
        heapq.heappush(self.heap, (1, self.curtime, key))
        self.curtime += 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)