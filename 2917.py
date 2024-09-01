class Solution:
    def findKOr(self, nums: list[int], k: int) -> int:
        total_bits = [0] * 32  # since limit = 2 ** 31 - 1
        for num in nums:  # get frequency of each bit position in nums
            current_bit = -1
            while num > 0:  # get bits of num
                total_bits[current_bit] += num % 2
                num //= 2
                current_bit -= 1

        # convert k-or to decimal
        k_or_bits = [1 if bit >= k else 0 for bit in total_bits]
        k_or = 0
        for i, bit in enumerate(k_or_bits):
            if bit:
                k_or += 2 ** (31 - i)

        return k_or