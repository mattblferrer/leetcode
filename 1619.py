class Solution:
    def trimMean(self, arr: list[int]) -> float:
        arr.sort()
        to_remove = len(arr) // 20
        arr = arr[to_remove:-to_remove]  # remove top and bottom 5%
        return sum(arr) / len(arr)  # get average of new arr