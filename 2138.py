class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        arr = []
        for i in range(0, len(s), k):
            substr = s[i:i + k]
            if len(substr) < k:   # if string does not have k chars remaining
                substr += fill * (k - len(substr))
            arr.append(substr)

        return arr