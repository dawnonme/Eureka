class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        if len(str) == 0 or (len(str) == 1 and not str.isdigit()):
            return 0
        elif str[0] in ['+', '-'] or str[0].isdigit():
            sign = -1 if str[0] == '-' else 1
            num_digits = 0
            start = 1 if str[0] in ['+', '-'] else 0
            flag = False
            for i in range(start, len(str)):
                num_digits = i
                if not str[i].isdigit():
                    flag = True
                    break
            if not flag:
                num_digits += 1
            value = 0
            for i in range(num_digits - 1, start - 1, -1):
                value += int(str[i]) * 10**(num_digits - i - 1)
            max_int = 2**31
            value *= sign
            if value > max_int - 1:
                return max_int - 1
            elif value < -max_int:
                return -max_int
            return value
        return 0
