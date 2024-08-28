class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        # create dictionary of origin, destination pairs
        path_dict = dict()
        for origin, destination in paths: 
            if origin not in path_dict:
                path_dict[origin] = [destination]
            else:
                path_dict[origin].append(destination)
 
        # check which city has no outgoing path in the dictionary
        for _, destination in paths:
            if destination not in path_dict:
                return destination