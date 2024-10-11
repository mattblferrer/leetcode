class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = {
            1000: "M",
            500: "D",
            100: "C",
            50: "L",
            10: "X",
            5: "V",
            1: "I"
        }
        roman = ""

        while num > 0:
            num_log = len(str(num)) - 1  # log10 of the number
            largest = num // (10 ** num_log)  # leftmost (largest) digit

            if largest in [4, 9]:  # subtractive form
                symbol1 = symbols[10 ** num_log]
                symbol2 = symbols[(largest + 1) * 10 ** num_log]
                roman += symbol1 + symbol2
                num -= largest * 10 ** num_log

            elif largest > 4:  # for symbols V, L, D
                symbol = symbols[5 * 10 ** num_log]
                roman += symbol
                num -= 5 * 10 ** num_log

            else:  # base case (for symbols I, X, C, M)
                symbol = symbols[10 ** num_log]
                roman += largest * symbol
                num -= largest * 10 ** num_log

        return roman
