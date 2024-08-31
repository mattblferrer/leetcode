class Solution:
    def getLucky(self, s: str, k: int) -> int:
        converted = ""
        for letter in s:  # convert s to integer
            position = ord(letter) - 96  # a = 1, b = 2, ...
            converted += str(position)
        converted = int(converted)

        for _ in range(k):  # get sum of digits
            converted = sum(int(d) for d in str(converted))

        return converted