class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        frequencies = dict()
        for num in arr:
            if num not in frequencies:
                frequencies[num] = 1
            else:
                frequencies[num] += 1

        arr.sort()
        for num in reversed(arr):
            if num == 0:  # check if more than one zero exists in nums
                if frequencies[0] > 1:
                    return True
            elif num % 2 == 0 and num // 2 in frequencies:
                return True

        return False