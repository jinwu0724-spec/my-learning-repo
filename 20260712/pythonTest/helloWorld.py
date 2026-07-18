import keyword

print("Hello World")

# 保留关键词
keyWord = keyword.kwlist
print(keyWord)

# ========== Python 关键字说明 ==========
# 【逻辑值】
# True        布尔真值
# False       布尔假值
# None        表示空值或无值

# 【逻辑运算】
# and         逻辑与运算
print(f"0 and 0 = {0 and 0}")
print(f"1 and 0 = {1 and 0}")
print(f"1 and 1 = {1 and 1}")
# or          逻辑或运算
print(f"0 or 0 = {0 or 0}")
print(f"1 or 0 = {1 or 0}")
print(f"1 or 1 = {1 or 1}")
# not         逻辑非运算
print(f"not 0 = {not 0}")
print(f"not 1 = {not 1}")

# 【条件控制】
# if          条件判断语句
# elif        否则如果（else if 的缩写）
# else        否则分支
if True:
	print(True)
else:
	print(False)

# 【循环控制】
# for         迭代循环
for i in range(10):
    print(i, end=" ")
print()

list1 = "agfuegfblkn"
list2 = [i > 'c' for i in list1]
print(list2)
list3 = [i for i in list1 if i > 'c']
print(list3)
# while       条件循环
# break       跳出循环
# continue    跳过当前循环的剩余部分，进入下一次迭代
temp = 5
while temp > 0:
    print(temp)
    temp -= 1

    if temp == 3:
        print("continue")
        continue

    if temp - 1 == 1:
        print("break")
        break

# 【异常处理】
# try         尝试执行代码块
# except      捕获异常
# finally     无论是否发生异常都会执行的代码块
# raise       抛出异常
file = open('./test.txt', 'r')
try:
    content = file.read()
finally:
    file.close()

# 【函数定义】
# def         定义函数
# return      从函数返回值
# lambda      创建匿名函数
def add(x, y):
	return print(f"{x} + {y} = {x + y}")

z = add(1.3, 3.9)

func = lambda x, y: x - y
a = 1.34
b = 0.12
res = func(a, b)
print(f"{a} - {b} = {res}")
# 1.34 - 0.12 = 1.2200000000000002
# Python 的 float 使用国际标准 IEEE 754 双精度浮点数保存小数。

# 【类与对象】
# class       定义类
# del         删除对象引用
class Student:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def show_info(self):
        print(f"name:{self.name}, age:{self.age}")

stu1 = Student("Xiao Ming", 18)
stu1.show_info()
print(stu1.name)
print(stu1.age)


class Student:
    def __init__(self, name):
        self.name = name

stu = Student("Xiao Hong")
print(stu.name)
del stu.name
# print(stu.name)
# Traceback (most recent call last):
#   File "F:\my-learning-repo\20260712\pythonTest\helloWorld.py", line 94, in <module>
#     print(stu.name)
# AttributeError: 'Student' object has no attribute 'name'


# 【模块导入】
# import      导入模块
# from        从模块导入特定部分
# as          为导入的模块或对象创建别名
import time

def set_loading_time():
	for i in range(1, 11, 1):
		print(i, end=" ")
		cnt = 0.1 * i
		time.sleep(cnt)

# 【作用域】
# global      声明全局变量
# nonlocal    声明非局部变量（用于嵌套函数）

# 【异步编程】
# async       声明异步函数
# await       等待异步操作完成
import asyncio

async def say_hello():
    print("...satrt waiting")
    await asyncio.sleep(2)
    print("waiting end ...")
    set_loading_time(); print()
    return "OVER"

async def main():
    res = await say_hello()
    print(res)

asyncio.run(main())


# 【其他关键字】
# assert      断言，用于测试条件是否为真
# in          检查成员关系
# is          检查对象身份（是否是同一个对象）
# pass        空语句，用于占位
# with        上下文管理器，用于资源管理
with open("./test.txt", "r", encoding="utf-8") as f:
    data = f.read()
    print(data[0:10])
    print(data)
# yield       从生成器函数返回值
def set_pass():
    # print("pass")
	pass

