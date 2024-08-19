class Solution:
    def sumOfEncryptedInt(self, nums: list[int]) -> int:
        def encrypt(num: int) -> int:
            digits = [int(d) for d in str(num)]
            return int(str(max(digits)) * len(digits))

        return sum(encrypt(num) for num in nums)
    