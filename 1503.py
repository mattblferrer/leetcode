class Solution:
    def getLastMoment(self, n: int, left: list[int], right: list[int]) -> int:
        if left and right:
            return max(max(left), n - min(right))
        elif left:  # if right array empty
            return max(left)
        elif right:  # if left array empty
            return n - min(right)