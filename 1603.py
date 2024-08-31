class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:  # big car
            if self.big <= 0:  # not enough parking
                return False
            self.big -= 1  # park the car
            return True

        elif carType == 2:  # medium car
            if self.medium <= 0:  # not enough parking
                return False
            self.medium -= 1  # park the car
            return True

        else:  # small car
            if self.small <= 0:  # not enough parking
                return False
            self.small -= 1  # park the car
            return True

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)