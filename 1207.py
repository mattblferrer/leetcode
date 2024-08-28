class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        occurrences = dict()
        for n in arr:  # count number of occurrences of each value
            if n not in occurrences:
                occurrences[n] = 1
            else:
                occurrences[n] += 1

        occurrences_unique = set()
        for o in occurrences.values():  # uniqueness check
            if o in occurrences_unique:
                return False
            occurrences_unique.add(o)
        return True