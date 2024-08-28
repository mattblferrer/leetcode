class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def factorialList(n: int) -> list[int]:
            k = 1
            arr = []
            for i in range(1, n + 2):
                arr.append(k)
                k *= i

            return arr
    
        sequence = ""
        k -= 1  # since permutation sequence k given is 1-indexed
        used_digits = [False] * 9  # 1 to 9

        for factorial in reversed(factorialList(n - 1)):
            d = k // factorial  # check for d'th unused digit
            ctr = 0  # counter for looking for d'th unused digit

            for i, is_used in enumerate(used_digits, start=1):  
                if not is_used:
                    if ctr == d:
                        used_digits[i - 1] = True  # used_digits 1-indexed
                        break
                    ctr += 1

            sequence += str(i)  # add unused digit to current sequence
            k %= factorial

        return sequence