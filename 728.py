class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        def isSelfDividing(num: int) -> bool:
            digits = [int(d) for d in str(num)]

            for d in digits:  # check divisibility of digits
                if d == 0 or num % d != 0:
                    return False
            return True

        self_div = [i for i in range(left, right + 1) if isSelfDividing(i)]
        return self_div