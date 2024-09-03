class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = dict()
        for string in strs:
            sort = "".join(sorted(string))  # anagrams same when sorted
            if sort not in anagrams:
                anagrams[sort] = [string]
            else:
                anagrams[sort].append(string)

        return [group for group in anagrams.values()]  # unpack dict to list