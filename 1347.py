class Solution:
    def minSteps(self, s: str, t: str) -> int:
        def getFrequency(s: str) -> dict[str, int]:
            frequencies = dict()
            for char in s:
                if char not in frequencies:
                    frequencies[char] = 1
                else:
                    frequencies[char] += 1

            return frequencies

        s, t = getFrequency(s), getFrequency(t)
        steps = 0

        for k, v in s.items():
            if k not in t:  # unique character in s
                steps += v
            else:  # common between s, t
                steps += abs(v - t[k])

        for k, v in t.items():
            if k not in s:  # unique character in t
                steps += v

        return steps // 2  # since each choose/replace changes both s, t by 1