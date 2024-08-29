class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        def returnFrequency(digits: list[int]) -> list[int, int]:
            frequencies = dict()

            for digit in digits:
                if digit not in frequencies:
                    frequencies[digit] = 1
                else:
                    frequencies[digit] += 1

            return frequencies

        answer = []
        digits_freqs = returnFrequency(digits)

        for i in range(100, 1000, 2):  # iterate through all 3 digit evens
            i_digits = [int(d) for d in str(i)]
            i_freqs = returnFrequency(i_digits)

            for digit, freq in i_freqs.items():
                if digit not in digits_freqs:
                    break
                if digits_freqs[digit] < freq:
                    break
            else:
                answer.append(i)

        return answer