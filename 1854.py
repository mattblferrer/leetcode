class Solution:
    def maximumPopulation(self, logs: list[list[int]]) -> int:
        population = [0] * 101  # 1950 to 2050, inclusive
        for birth, death in logs:
            for year in range(birth, death):
                population[year - 1950] += 1

        maximum = 0
        max_year = 0
        for year, p in enumerate(population, start=1950):
            if p > maximum:
                maximum = p
                max_year = year
        
        return max_year