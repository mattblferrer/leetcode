class SmallestInfiniteSet:

    def __init__(self):
        self.not_in_set = set()

    def popSmallest(self) -> int:
        i = 1
        while True:  # count up from 1 to find smallest element in set
            if i not in self.not_in_set:  # i in set
                self.not_in_set.add(i)
                return i
            i += 1

    def addBack(self, num: int) -> None:
        if num in self.not_in_set:
            self.not_in_set.remove(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)