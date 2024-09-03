class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        arr = []
        pref = pref[::-1]  # reverse pref 
        for a, b in zip(pref, pref[1:]):  # adjacent a, b
            arr.append(a ^ b)

        return [pref[-1]] + arr[::-1]  # reverse arr to get correct order