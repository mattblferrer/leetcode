class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        def returnFrequency(nums: list[int]) -> dict[int, int]:
            frequencies = dict()
            for n in nums:
                if n not in frequencies:
                    frequencies[n] = 1
                else:
                    frequencies[n] += 1

            return frequencies

        frequencies = returnFrequency(nums)
        answer = [0, 0]
        for num, freq in frequencies.items():
            answer[0] += freq // 2  # number of pairs formed
            answer[1] += freq % 2  # number of leftover integers after pairs
        
        return answer