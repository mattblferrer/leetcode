class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        index_1 = {string:i for i, string in enumerate(list1)}
        index_2 = {string:i for i, string in enumerate(list2)}
        common = {}  # i + j: [string1, string2, ...] pairs

        for string in index_1:  # find common strings between list1 and list2
            if string in index_2:
                index_sum = index_1[string] + index_2[string]
                if index_sum not in common:
                    common[index_sum] = [string]
                else:
                    common[index_sum].append(string)

        min_index_sum = min(common.keys())
        return common[min_index_sum]
        