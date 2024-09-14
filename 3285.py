class Solution:
    def stableMountains(self, height: list[int], threshold: int) -> list[int]:
        indices = []
        for i, h in enumerate(height[:-1]):  
            if h > threshold:
                indices.append(i + 1)

        return indices