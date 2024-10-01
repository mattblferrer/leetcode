class Solution:
    def wateringPlants(self, plants: list[int], capacity: int) -> int:
        watering = 0  # current plant being watered
        current_water = capacity  # amount of water in the watering can
        steps = 1  # go to plant 0

        while True:
            water_amt = min(current_water, plants[watering])
            plants[watering] -= water_amt
            current_water -= water_amt

            if plants[watering] == 0:  # plant fully watered
                if watering == len(plants) - 1:  # watered last plant
                    return steps
                if plants[watering + 1] <= current_water:  # enough for next
                    steps += 1
                else:  # go back to river to refill
                    steps += (watering + 1) * 2 + 1
                    current_water = capacity
                watering += 1
                    
            else:  # go back to river to refill
                steps += (watering + 1) * 2
                current_water = capacity

