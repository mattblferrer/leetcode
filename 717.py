class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        i = 0
        while i < len(bits) - 2:  # ans depends on position of i on last char
            if bits[i]:  # 10 or 11
                i += 2
            else:  # 0
                i += 1

        if i == len(bits) - 1:  # one-bit character
            return True
        elif i == len(bits) - 2 and bits[i]:  # two-bit character
            return False
        return True  # [0, 0]