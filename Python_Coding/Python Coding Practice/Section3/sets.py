#my_set = {1,2,3,4,5}
my_set = {4,5}
your_set = {4,5,6,7,8,9,10}

#.differnce()
print (my_set.difference(your_set))

# #.discard
# my_set.discard(5)
# print (my_set)

# #.difference_update()
# my_set.difference_update(your_set)
# print(my_set)

#.intersection
print(my_set.intersection(your_set))

#.isdisjoint()
print(my_set.isdisjoint(your_set))

#.union()
print(my_set.union(your_set))

#issubset()
print(my_set.issubset(your_set))

#issuperset()
print(my_set.issuperset(your_set))
print(your_set.issuperset(my_set))