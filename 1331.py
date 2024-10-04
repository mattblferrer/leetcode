class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        sorted_arr = sorted(arr)
        ranks = {}
        rank = 1
        previous = float('inf')

        for n in sorted_arr:  # get ranks for n in sorted arr for dictionary
            if n not in ranks:
                ranks[n] = rank
            if n != previous:
                rank += 1
            previous = n

        rank_transform = [ranks[n] for n in arr]
        return rank_transform