class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        return "".join(s[(k + i) % len(s)] for i in range(len(s)))