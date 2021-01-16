import copy

old_list = [[1,1,1],[2,2,2],[3,3,3]]
new_list = copy.copy(old_list)

old_list[1][1] = 'AA'

print(old_list,new_list)

old_list1 = [[1,1,1],[2,2,2],[3,3,3]]
new_list1 = copy.deepcopy(old_list1)

old_list1[1][1] = 'AA'

print(old_list1,new_list1)