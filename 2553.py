class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        answer = []
        for num in nums:
            digits = [int(d) for d in str(num)]
            answer += digits

        return answer