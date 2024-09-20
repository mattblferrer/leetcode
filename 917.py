class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left, right = 0, len(s) - 1
        s_list = list(s)

        while True:
            try:
                while not s_list[left].isalpha():  # find letter on left ptr
                    left += 1
                while not s_list[right].isalpha():  # find letter on right ptr
                    right -= 1
            except IndexError:  # if pointers out of range in s, return
                return "".join(s_list)
            if left > right:  # all letters reversed
                return "".join(s_list)

            s_list[left], s_list[right] = s_list[right], s_list[left]  # swap
            left += 1
            right -= 1