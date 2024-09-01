class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> list[int]:
        powerful = set()
        for i in range(0, 21):  # since bound <= 10**6, limit = log2(10**6)
            for j in range(0, 21):
                power = x**i + y**j
                if power > bound:  # no more power to be found below bound
                    break
                powerful.add(power)

        return list(powerful)