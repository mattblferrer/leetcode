class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1
        two_sum = float('inf')  # placeholder
        while two_sum != target:
            two_sum = numbers[left] + numbers[right]
            if two_sum > target:
                right -= 1
            elif two_sum < target:
                left += 1

        return [left + 1, right + 1]  # since 1-indexed
        