class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> list[int]:
        if tomatoSlices % 2 == 1:  # since each burger uses either 2 or 4
            return []
        if tomatoSlices > 4 * cheeseSlices:  # at most 4 tomato / burger
            return []
        if tomatoSlices < 2 * cheeseSlices:  # at least 2 tomato / burger
            return []
            
        small_tomato = cheeseSlices * 2
        total_jumbo = (tomatoSlices - small_tomato) // 2
        total_small = cheeseSlices - total_jumbo
        return [total_jumbo, total_small]