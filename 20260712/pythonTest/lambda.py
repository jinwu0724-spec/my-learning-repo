func = lambda: "Hello World !"
print(func)
print(func())


func = lambda a : a ** 2
print(func(2))

func = lambda a, b, c : a + b * c
print(func(1, 2, 3))

func = lambda a, b, c : 'error' if c == 0 else a + b / c
print(func(2, 4, 6))
print(func(8, 10, 0))


nums = []
for i in range(10):
	nums.append(2 * i)
print(nums)

# for i in range(1, 11, 1):  [1, 11)
# 	nums.append(2 * i)
# print(nums)

squared = list(map(lambda x : 2 * x, nums))
print(squared)

def double(n):
	return 2 * n

squared = list(map(double, nums))
print(squared)

def double(n, a):
	return a * n

squared = list(map(lambda x : double(x, 2), nums))
print(squared)

# 函数参数个数 == map 中可迭代对象个数
# map(func,       iterable1)              # func(a)
# map(func,       iterable1, iterable2)   # func(a, b)
# map(func,       iterable1, iterable2, iterable3)  # func(a, b, c)
