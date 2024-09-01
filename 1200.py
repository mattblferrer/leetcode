class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        min_diff = float('inf')  # minimum absolute difference
        pair_list = []  # list of pairs with minimum absolute difference

        for a, b in zip(arr, arr[1:]):
            if b - a < min_diff:
                min_diff = b - a
                pair_list = [[a, b]]
            elif b - a == min_diff:
                pair_list.append([a, b])
        
        return pair_list