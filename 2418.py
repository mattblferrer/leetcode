class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        info = sorted(zip(heights, names))
        names = [x[1] for x in info][::-1]   # since descending order, reverse
        return names 