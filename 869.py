class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        power_str = [2 ** n for n in range(40)]
        powers_sorted = [sorted(str(p)) for p in power_str]
        return sorted(str(n)) in powers_sorted