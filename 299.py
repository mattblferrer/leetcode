class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        def getFrequency(s: str) -> dict[str, int]:
            frequencies = dict() 
            for digit in s:
                if digit not in frequencies:  # initialize for first occurrence
                    frequencies[digit] = 1
                else:
                    frequencies[digit] += 1
            
            return frequencies

        secret_f = getFrequency(secret)
        guess_f = getFrequency(guess)
        bulls, cows = 0, 0

        for digit, freq in guess_f.items():  # count bulls + cows
            if digit not in secret_f:  # guess digit not in secret
                continue
            cows += min(secret_f[digit], freq)

        for a, b in zip(secret, guess):  # count bulls (same position)
            if a == b:
                bulls += 1
            
        return str(bulls) + "A" + str(cows - bulls) + "B"  # format bulls/cows