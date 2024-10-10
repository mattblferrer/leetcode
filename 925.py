class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        def runLength(word: str) -> list[tuple[int, int]]:
            previous = word[0]  # previous character
            count = 1  # current count of number of characters 
            runs = []

            for c in word[1:]:
                if previous == c:
                    count += 1
                else:
                    runs.append((previous, count))
                    count = 1
                previous = c

            runs.append((previous, count))  # append final character
            return runs

        name_runs = runLength(name)
        typed_runs = runLength(typed)
        if len(name_runs) != len(typed_runs):  # not the same characters used
            return False
        for (char1, count1), (char2, count2) in zip(name_runs, typed_runs):
            if char1 != char2:
                return False
            if count1 > count2:
                return False

        return True