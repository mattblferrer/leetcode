class Solution:
    def sumZero(self, n: int) -> list[int]:
        arr = []

        if n % 2 == 0:  # even length
            for i in range(1, n // 2 + 1):  # i + (-i) = 0
                arr.append(i) 
                arr.append(-i)
            return arr

        else:  # odd length
            return [0] + self.sumZero(n - 1)