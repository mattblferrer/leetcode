class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        def search(candidates: list[int], target: int, last: int) -> list[list[int]]:
            comb_list = []  # list of combinations that sum to target
            for c in candidates:
                if c > last:  # prevent duplicates, descending chosen numbers
                    break
                if c > target:  # no possible combination
                    break
                if c == target:  # form a combination
                    comb_list.append([c])
                else:  # recursively search for combinations w/ smaller target
                    found = search(candidates, target - c, c)
                    comb_list += [[c] + combination for combination in found]
            
            return comb_list

        return search(candidates, target, candidates[-1])