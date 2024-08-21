class Solution:
    def numberOfSteps(self, num: int) -> int:
        binary = bin(num)[2:]
        return binary.count('1') + len(binary) - 1