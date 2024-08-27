class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def isSymmetric(n: int) -> bool:
            n_str = str(n)
            if len(n_str) % 2 == 1:  # odd number of digits
                return False
            sum_left = sum(int(d) for d in n_str[0:len(n_str) // 2])
            sum_right = sum(int(d) for d in n_str[len(n_str) // 2:])
            return sum_left == sum_right

        symmetric = 0
        for i in range(low, high + 1):
            if isSymmetric(i):
                symmetric += 1
        
        return symmetric