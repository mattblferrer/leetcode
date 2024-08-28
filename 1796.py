class Solution:
    def secondHighest(self, s: str) -> int:
        digit_appears = [False] * 10
        for char in s:  # check which digits appear in s
            if char.isdigit():
                digit_appears[int(char)] = True

        second_digit = -1
        ctr = 0
        for i in range(9, -1, -1):  # iterate from 9 to 0
            if digit_appears[i]:
                ctr += 1
            if ctr == 2:  # second largest digit encountered
                second_digit = i
                break

        return second_digit