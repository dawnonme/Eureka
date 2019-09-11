class Solution:
    def combinationSum(self, candidates: List[int],
                       target: int) -> List[List[int]]:
        self.candidates, self.res = candidates, []
        self._combinationSum(0, target, [])
        return self.res

    def _combinationSum(self, idx, target, cur):
        if idx == len(self.candidates):
            return
        new_num = self.candidates[idx]

        cnt = 1
        while True:
            add_num = cnt * new_num
            if add_num > target:
                break
            if add_num == target:
                self.res.append(cur + [new_num] * cnt)
            else:
                self._combinationSum(idx + 1, target - add_num,
                                     cur + [new_num] * cnt)
            cnt += 1

        self._combinationSum(idx + 1, target, cur)
