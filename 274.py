class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse=True)
        for i, c in enumerate(citations):
            if c < i + 1:  # since 1-indexed
                return i

        return len(citations)