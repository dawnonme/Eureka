from random import random


class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = {}
        self.array = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.table:
            return False
        self.table[val] = len(self.array)
        self.array.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.table:
            idx, last = self.table[val], self.array[-1]
            self.array[idx] = last
            self.table[last] = idx
            self.table.pop(val)
            self.array.pop()
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        idx = int(random() * len(self.array))
        return self.array[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()