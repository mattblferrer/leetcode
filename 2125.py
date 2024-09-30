class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        high, low = 0, 1
        beams = 0

        while low < len(bank):
            # find first row with security device
            if bank[high].count("1") == 0:  
                high += 1
                low += 1

            else:
                high_devices = bank[high].count("1")
                low_devices = bank[low].count("1")
                if low_devices > 0:  # found row with security devices
                    beams += high_devices * low_devices # beam between every device
                    high = low
                low += 1

        return beams