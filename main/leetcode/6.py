class Solution:
    def convert(self, s: str, numRows: int) -> str:
        output = [''] * numRows
        pointer = 0
        backward = False
        for i in range(len(s)):
            output[pointer] += s[i]
            if pointer == numRows - 1:
                backward = True
                pointer -= 1
            elif backward and pointer > 0:
                pointer -= 1
            elif backward and pointer == 0:
                backward = False
                pointer += 1
            else:
                pointer += 1
        out = ''
        for substr in output:
            out += substr
        return out
