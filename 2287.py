class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        def getFrequency(s: str) -> dict[str, int]:
            frequencies = dict()
            for char in s:
                if char not in frequencies:
                    frequencies[char] = 1
                else:
                    frequencies[char] += 1

            return frequencies

        s_f = getFrequency(s)
        target_f = getFrequency(target)
        max_copies = float('inf')  # number of copies of target from s
        
        for char, freq in target_f.items():
            if char not in s_f:  # letter in target not in s, not possible
                return 0
            max_copies = min(max_copies, s_f[char] // freq)

        return max_copies