class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        nodes = set()
        for u, v in edges:
            if u in nodes:
                return u
            if v in nodes:
                return v
            nodes.add(u)
            nodes.add(v)