class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        num_stations = len(gas)
        diff_gas = []
        lo = -1

        for i in range(num_stations):
            diff = gas[i] - cost[i]
            diff_gas.append(diff)
            if lo == -1 and diff >= 0:
                lo = i

        if lo == -1:
            return -1

        hi = lo + 1
        gas_now = diff_gas[lo]

        while lo < num_stations:
            if hi >= num_stations:
                hi -= num_stations

            gas_temp = gas_now + diff_gas[hi]
            if gas_temp >= 0:
                gas_now = gas_temp
                hi += 1
            else:
                if hi < lo:
                    return -1
                lo = hi + 1
                while lo < num_stations and diff_gas[lo] < 0:
                    lo += 1
                if lo == num_stations:
                    return -1
                hi = lo + 1
                gas_now = diff_gas[lo]

            if lo == hi % num_stations:
                return lo
        return -1
    
    # More clean solution.
    def can_complete_circuit(self, gas: List[int], cost: List[int]) -> int:
        pass
