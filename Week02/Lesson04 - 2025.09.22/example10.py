"""
Merging sets
"""

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

combine_set = set1 | set2
print(set1, set2, combine_set)
# {'b', 'a', 'c'} {1, 2, 3} {1, 2, 3, 'b', 'a', 'c'}

combine_set2 = set1.union(set2)
print(combine_set2)
# {1, 2, 3, "b", "a", "c"}
