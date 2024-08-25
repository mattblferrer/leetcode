class Solution:
    def countEven(self, num: int) -> int:
        even = 0
        for i in range(1, num + 1):
            digit_sum = sum(int(d) for d in str(i))
            if digit_sum % 2 == 0:
                even += 1

        return even