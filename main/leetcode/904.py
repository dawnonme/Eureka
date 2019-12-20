class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        from collections import defaultdict

        lo = hi = ans = 0
        basket = defaultdict(lambda: -1)

        while hi < len(tree):
            cur = tree[hi]
            if len(basket) >= 2:
                if cur not in basket:
                    ans = max(ans, hi - lo)
                    prev = tree[hi - 1]
                    other = [(t, i) for t, i in basket.items() if t != prev][0]
                    lo = other[1] + 1
                    basket.pop(other[0])
            basket[cur] = hi
            hi += 1

        return max(ans, hi - lo)