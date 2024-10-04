class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        skill.sort()
        pairs = []
        total_skill = []
        total_chemistry = 0

        for i in range(len(skill) // 2):
            a, b = (skill[i], skill[-i - 1])  # pair min with max, ...
            total_skill.append(a + b)
            if total_skill[-1] != total_skill[0]:
                return -1
            total_chemistry += a * b

        return total_chemistry
            