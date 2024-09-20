class Solution:
    def romanToInt(self, s: str) -> int:
        conversion = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        num = 0
        last_symbol = 'I'

        for symbol in reversed(s):
            if conversion[symbol] < conversion[last_symbol]:  # IV, IX, XL, etc
                num -= conversion[symbol]
            else:
                num += conversion[symbol]
            last_symbol = symbol

        return num