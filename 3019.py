class Solution:
    def countKeyChanges(self, s: str) -> int:
        key_changes = 0
        s = s.lower()
        for l1, l2 in zip(s, s[1:]):
            if l1 != l2:
                key_changes += 1

        return key_changes