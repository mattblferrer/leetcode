class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = str(num)
        k_beauty = 0

        for i in range(len(num_str) - k + 1):
            substr = num_str[i:i+k]
            if int(substr) == 0:  # since 0 not a divisor of any value
                continue
            if num % int(substr) == 0:
                k_beauty += 1

        return k_beauty