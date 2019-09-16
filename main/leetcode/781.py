class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        from collections import Counter

        ctr = Counter(answers)
        ret = 0
        for val, num in ctr.items():
            num_rabbits_color = val + 1
            while num > num_rabbits_color:
                num -= num_rabbits_color
                ret += num_rabbits_color
            ret += num_rabbits_color
        return ret