def decorator_function(original_function):
    def wrapper(*args, **kwargs):
        # 调用前
        print("Before execution")

        result = original_function(*args, **kwargs) # 说明：使用 *args, **kwargs 可以兼容任意参数函数。

        # 调用后
        print("After execution")

        return result
    return wrapper

@decorator_function
def target_function():
    print("Execution of the original function")

target_function()
print()

wrapper_ref = decorator_function(target_function)
wrapper_ref()
print()



# 说明：这是"装饰器工厂"，外层函数用于接收参数。
def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
        func(*args, **kwargs)
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

say_hello()
