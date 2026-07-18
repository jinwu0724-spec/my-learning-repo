set1 = {1, 2, 3, 4}
set2 = set([4, 5, 6, 7])
set_a = set('abracadabra')
print(set_a)


set3 = set1 & set2
print(f"set3: {set3}")

set3 = set1 | set2
print(f"set3: {set3}")

set3 = set1 - set2
print(f"set3: {set3}")

set3 = set1 ^ set2  # A + B - AB
print(f"set3: {set3}")

set3 = set1 and set2
print(set3)

set3 = set1 or set2
print(set3)

setnew = {i**2 for i in (1,2,3)}
print(setnew)
