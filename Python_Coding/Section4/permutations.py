from itertools import permutations

s,r = input().split()
r = int(r)


result = sorted(permutations(s, r))

for perm in result:
    print(''.join(perm))
