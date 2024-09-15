class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        def bitCount(n: int) -> int:
            binary = bin(n)[2:]
            return sum(1 for bit in binary if bit == '1')

        valid = []  # valid times with (turnedOn) number of LEDs turned on
        for mins in range(720):  # from 00:00 to 11:59
            hh, mm = mins // 60, mins % 60
            if bitCount(hh) + bitCount(mm) == turnedOn:
                time_str = str(hh) + ':' + str(f"{mm:02d}")  # leading zero 
                valid.append(time_str)

        return valid