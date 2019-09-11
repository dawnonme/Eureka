class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        lo, hi = 0, len(people) - 1
        ans = 0

        while lo < hi:
            if people[lo] + people[hi] <= limit:
                lo += 1
            ans += 1
            hi -= 1

        if lo == hi:
            ans += 1

        return ans
