from collections import defaultdict


class TimeMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = defaultdict(lambda: defaultdict(str))
        # self.key_time = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[timestamp][key] = value
        # self.key_time[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        # if self.key_time[key]:
        while timestamp >= 0:
            if self.dic[timestamp][key]:
                return self.dic[timestamp][key]
            timestamp -= 1

        return ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)