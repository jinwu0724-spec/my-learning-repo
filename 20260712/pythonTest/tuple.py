tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"
print(type(tup3))
# 元组中的元素值是不允许修改的

# tup2
# 元素:     1     2     3     4     5
# 正向索引: 0     1     2     3     4
# 反向索引: -5   -4    -3    -2    -1
print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])
print ("tup2[-3:-1]: ", tup2[-3:-1])

tup4 = tup1 + tup2
print(f"tup4: {tup4}")

tup1 += tup2
print(f"tup1: {tup1}")



tup = ('Google', 'Runoob', 1997, 2000)

print (tup)
del tup
print ("del tup : ")

# print (tup)
# Traceback (most recent call last):
#   File "F:\my-learning-repo\20260712\pythonTest\tuple.py", line 25, in <module>
#     print (tup)
# NameError: name 'tup' is not defined

a = (x for x in range(1,10))
print(a)
# <generator object <genexpr> at 0x0000023DF8F993C0>  # 返回的是生成器对象

print(tuple(a))       # 使用 tuple() 函数，可以直接将生成器对象转换成元组
# (1, 2, 3, 4, 5, 6, 7, 8, 9)
