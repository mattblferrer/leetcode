class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        def addLeadingZeros(num: int) -> str:
            num_str = str(num)
            while len(num_str) < 4:
                num_str = "0" + num_str

            return num_str

        key = ""
        num1 = addLeadingZeros(num1)
        num2 = addLeadingZeros(num2)
        num3 = addLeadingZeros(num3)
        for i in range(4):
            key += str(min(int(num1[i]), int(num2[i]), int(num3[i])))

        return int(key)