class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        arr1 = [int(v) for v in version1.split(".")]
        arr2 = [int(v) for v in version2.split(".")]
        if len(arr1) < len(arr2):  # add trailing zeros to version1
            arr1 = arr1 + [0] * (len(arr2) - len(arr1))
        else:  # add trailing zeros to version2
            arr2 = arr2 + [0] * (len(arr1) - len(arr2))

        for v1, v2 in zip(arr1, arr2):  # compare version numbers one-to-one
            if v1 < v2:
                return -1
            elif v2 < v1:
                return 1
        return 0  # if all revision values are the same 