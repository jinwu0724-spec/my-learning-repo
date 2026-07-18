list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]
list4 = ['red', 'green', 'blue', 'yellow', 'white', 'black']

print(list4)

# for example
len1 = len(list1)
for i in range(len1):
	print(list1[i], end=" ")
	if i + 1 == len1:
		print()

# len3 = len(list3)
# for j in range(len(list2)):
# 	list3[len3 + j] = list2[j]
# print(list3)
# 
# Traceback (most recent call last):
#   File "F:\my-learning-repo\20260712\pythonTest\lisy.py", line 15, in <module>
#     list3[len3 + j] = list2[j]
# IndexError: list assignment index out of range

list3.extend(list2)
print(f"list3:{list3}")


list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]

for j in range(len(list2)):
    list3.append(list2[j])

print(f"list3:{list3}")


list1 = "agfuegfblkn"
list2 = [i > 'c' for i in list1]
print(list2)
list3 = [i for i in list1 if i > 'c']
print(list3)
