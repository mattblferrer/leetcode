class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(" ", "").replace("-", "")
        new_number = ""
        digits_left = len(number)
        for i in range(0, len(number) - 4, 3):  # blocks of 3 until 4 or fewer
            new_number += number[i:i + 3] + "-"
            digits_left -= 3

        # final 4 or fewer digits
        if digits_left == 4:  # 2 blocks of length 2
            new_number += number[-4: -2] + "-" + number[-2:]
        elif digits_left == 3 or digits_left == 2:  # single block 
            new_number += number[-digits_left:]

        return new_number