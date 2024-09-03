class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        groups = []
        group_size_dict = dict()
        
        for i, group_size in enumerate(groupSizes):
            if group_size not in group_size_dict:
                group_size_dict[group_size] = [i]
            else:
                group_size_dict[group_size].append(i)

        # get list of indices per group size
        for group_size, i_list in group_size_dict.items():  
            for i in range(len(i_list) // group_size):  # create group
                group = []
                for j in range(group_size):
                    group.append(i_list[i * group_size + j])
                groups.append(group)

        return groups