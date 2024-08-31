class Bitset:

    def __init__(self, size: int):
        self.bitset = dict()
        self.bitset[1] = set()
        self.bitset[0] = set(range(size))  # initialize all indices to 0
        self.size = size

    def fix(self, idx: int) -> None:
        self.bitset[1].add(idx)
        if idx in self.bitset[0]:  # if bit at idx is 1, don't do anything
            self.bitset[0].remove(idx)

    def unfix(self, idx: int) -> None:
        self.bitset[0].add(idx)
        if idx in self.bitset[1]:  # if bit at idx is 0, don't do anything
            self.bitset[1].remove(idx)

    def flip(self) -> None:
        self.bitset[0], self.bitset[1] = self.bitset[1], self.bitset[0]

    def all(self) -> bool:
        return len(self.bitset[1]) == self.size

    def one(self) -> bool:
        return len(self.bitset[1]) > 0

    def count(self) -> int:
        return len(self.bitset[1])

    def toString(self) -> str:
        string = ""
        for i in range(self.size):
            if i in self.bitset[1]:  # bit at index i is 1
                string += '1'
            else:  # bit at index i is 0
                string += '0'
            
        return string

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()