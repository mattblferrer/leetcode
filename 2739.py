class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        usedFuel = 0
        while mainTank != 0:
            mainTank -= 1
            usedFuel += 1

            if usedFuel % 5 == 0:
                if additionalTank:  # transfer from additional to main tank
                    additionalTank -= 1
                    mainTank += 1

        return usedFuel * 10  # multiply fuel by mileage