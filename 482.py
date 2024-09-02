class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        data = "".join(s.split("-")).upper()  # remove dashes and convert upper
        license_key = []  # list of characters in license key

        for i in range(len(data)):  # construct license key in reverse order
            if i % k == 0:
                license_key.append("-")
            license_key.append(data[-i - 1])

        return "".join(license_key[::-1])[:-1]  # reverse, remove trailing dash