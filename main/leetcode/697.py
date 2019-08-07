from math import inf


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freqDict = {}
        degree = 1
        for i in range(len(nums)):
            if nums[i] in freqDict:
                freqDict[nums[i]][0] += 1
                freqDict[nums[i]][2] = i
                if degree < freqDict[nums[i]][0]:
                    degree = freqDict[nums[i]][0]
            else:
                freqDict[nums[i]] = [1, i, i]
        minLen = inf
        for k, v in freqDict.items():
            if v[0] == degree and v[2] - v[1] + 1 < minLen:
                minLen = v[2] - v[1] + 1
        return minLen
