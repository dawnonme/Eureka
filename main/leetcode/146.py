class DoublyLinkedListNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity

        self.dic = {}
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1

        value, node = self.dic[key]
        l_node, r_node = node.left, node.right

        if r_node:
            if not l_node:
                self.head = self.head.right
                self.head.left = None
            else:
                l_node.right = r_node
                r_node.left = l_node

            self.tail.right = node
            node.right = None
            node.left = self.tail
            self.tail = self.tail.right

        return value

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key][1]
            l_node, r_node = node.left, node.right
            if r_node:
                if not l_node:
                    self.head = self.head.right
                    self.head.left = None
                else:
                    l_node.right = r_node
                    r_node.left = l_node

                self.tail.right = node
                node.right = None
                node.left = self.tail
                self.tail = self.tail.right
            self.dic[key] = (value, node)
            return

        if not self.head and not self.tail:
            first_node = DoublyLinkedListNode(key)
            self.head = first_node
            self.tail = first_node
            cur = first_node
        else:
            if len(self.dic) == self.capacity:
                lru_node = self.head
                self.head = self.head.right
                if self.head:
                    self.head.left = None
                self.dic.pop(lru_node.val)

            self.tail.right = DoublyLinkedListNode(key)
            ori = self.tail
            self.tail = self.tail.right
            self.tail.left = ori
            cur = self.tail

        self.dic[key] = (value, cur)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)