class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int],
                              num_wanted: int, use_limit: int) -> int:
        from collections import Counter

        combined = sorted(zip(values, labels), reverse=True)
        total_value = idx = 0
        counter = Counter()
        while num_wanted > 0 and idx < len(combined):
            val, lab = combined[idx]
            if counter[lab] < use_limit:
                total_value += val
                num_wanted -= 1
                counter[lab] += 1
            idx += 1
        return total_value