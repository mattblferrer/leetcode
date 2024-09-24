class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        covered_set = set()
        for left_i, right_i in ranges:
            for i in range(left_i, right_i + 1):
                covered_set.add(i)

        for i in range(left, right + 1):
            if i not in covered_set:
                return False

        return True