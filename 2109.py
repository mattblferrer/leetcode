class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        s_list = []
        space_ptr = 0
        for i, char in enumerate(s):
            if space_ptr < len(spaces):  # still spaces left to add
                if spaces[space_ptr] == i:
                    s_list.append(" ")
                    space_ptr += 1
            s_list.append(char)

        return "".join(s_list)