
#itertools: product, permutations, combinations, accumalate, groupby, and infinite itertors
from itertools import product,permutations,combinations,combinations_with_replacement,groupby
import pprint
a = [1,2,3]
b = [3,4]

prod = product(a,b)
print(list(prod))

perm = permutations(a,2)
print(list(perm))

z = [1,3,5,10,2,4]
print(min(a))

persons = [
{'name':'Tim','age':25},
{'name':'Tim','age':25},
{'name':'Tim1','age':225},
{'name':'Tim2','age':215}

]
group_obj = groupby(persons, key=lambda x:x['age'])
print(group_obj)
pprint.pprint(vars(groupby))
for key,value in group_obj:
	print(key,list(value))