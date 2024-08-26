class Solution:
    def digitSum(self, s: str, k: int) -> str:
        def splitIntoGroups(s: str, k: int) -> list[str]:
            group = ""
            groups = []
            ctr = 0
            for c in s:
                if ctr == k:  # append and reset for next group
                    groups.append(group)
                    group = ""
                    ctr = 0
                # add character to current group
                group += c
                ctr += 1

            if group:
                groups.append(group)  # add last (unfinished) group
            return groups

        while len(s) > k:
            groups = splitIntoGroups(s, k)
            s = ""  # reset string s
            for group in groups:
                s += str(sum(int(d) for d in group))

        return s
    