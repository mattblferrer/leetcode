class Solution:
    def maxPower(self, s: str) -> int:
        max_power = 1
        power = 1
        last_char = ''

        for c in s: 
            if c == last_char:  # continue the substring of one unique char
                power += 1
            else:  # different char encountered, reset
                max_power = max(max_power, power)
                power = 1
            last_char = c
    
        return max(max_power, power)