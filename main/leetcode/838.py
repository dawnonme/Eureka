class Solution:
    def pushDominoes(self, dominoes: str) -> str:

        dominoes = list(dominoes)

        def set_states(d, l, r, s):
            for i in range(l, r + 1):
                d[i] = s

        lo = 0

        for hi in range(1, len(dominoes)):
            if dominoes[hi] != '.':
                if dominoes[lo] != 'R' and dominoes[hi] == 'L':
                    set_states(dominoes, lo, hi, 'L')
                elif dominoes[lo] == 'R':
                    if dominoes[hi] == 'L':
                        mid = (lo + hi) // 2
                        if (lo + hi) % 2 != 0:
                            dominoes[mid] = 'R'
                        set_states(dominoes, lo, mid - 1, 'R')
                        set_states(dominoes, mid + 1, hi, 'L')
                    else:
                        set_states(dominoes, lo, hi, 'R')
                lo = hi

        if dominoes[lo] == 'R' and dominoes[-1] == '.':
            set_states(dominoes, lo, len(dominoes) - 1, 'R')

        return ''.join(dominoes)