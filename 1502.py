class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr.sort()
        difference = arr[1] - arr[0]
        for num1, num2 in zip(arr, arr[1:]):  # check differences if match
            if num2 - num1 != difference:
                return False

        return True