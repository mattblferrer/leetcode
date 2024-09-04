class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        pos, neg = [], []
        answer = []
        for n in nums:  # split nums into positive and negative integer arrays
            if n > 0:
                pos.append(n)
            else:
                neg.append(n)

        for p, n in zip(pos, neg):  # reconstruct new array
            answer.append(p)
            answer.append(n)
        return answer