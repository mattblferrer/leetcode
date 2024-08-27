class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        b_num = int("".join(str(d) for d in b))  # express b in numeric form
        return pow(a, b_num, 1337)