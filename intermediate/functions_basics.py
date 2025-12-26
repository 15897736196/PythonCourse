# Python学习项目 - 中级内容：函数基础
# 学习序号：第3阶段 第1课 - 函数基础
# 建议学习时间：90-120分钟
# 前置知识：第1-2阶段 - 基础语法和数据结构
# 下一课：第3阶段 第2课 - 模块和包 (modules.py)
# 本模块介绍Python函数的定义、使用和相关概念

# ===== 1. 函数定义和调用 =====

print("=== 函数定义和调用 ===")

# 函数定义
def greet(name):
    """简单的问候函数"""
    return f"Hello, {name}!"

# 函数调用
result = greet("张三")
print(result)

# 函数可以没有返回值
def print_greeting(name):
    """打印问候语的函数"""
    print(f"Hello, {name}!")

print_greeting("李四")

# 函数可以没有参数
def say_hello():
    """无参数函数"""
    print("Hello, World!")

say_hello()

# ===== 2. 函数参数 =====

print("\n=== 函数参数 ===")

# 位置参数
def add_numbers(a, b):
    """两个数相加"""
    return a + b

print(f"5 + 3 = {add_numbers(5, 3)}")

# 默认参数
def greet_person(name, greeting="Hello"):
    """带默认参数的问候函数"""
    return f"{greeting}, {name}!"

print(greet_person("张三"))
print(greet_person("李四", "你好"))

# 关键字参数
def describe_person(name, age, city):
    """描述一个人"""
    return f"{name}今年{age}岁，住在{city}。"

print(describe_person(name="王五", age=25, city="北京"))
print(describe_person(city="上海", name="赵六", age=30))

# 可变参数 *args
def sum_all(*numbers):
    """求任意个数的和"""
    total = 0
    for num in numbers:
        total += num
    return total

print(f"求和 1+2+3+4 = {sum_all(1, 2, 3, 4)}")
print(f"求和 10+20 = {sum_all(10, 20)}")

# 关键字可变参数 **kwargs
def print_info(**info):
    """打印信息"""
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="张三", age=25, city="北京")

# 参数组合
def complex_function(a, b=10, *args, **kwargs):
    """参数组合示例"""
    print(f"a = {a}, b = {b}")
    print(f"args = {args}")
    print(f"kwargs = {kwargs}")

complex_function(1, 2, 3, 4, 5, x=10, y=20)

# ===== 3. 函数返回值 =====

print("\n=== 函数返回值 ===")

# 单个返回值
def get_square(x):
    """返回平方数"""
    return x ** 2

result = get_square(5)
print(f"5的平方是: {result}")

# 多个返回值（返回元组）
def get_user_info():
    """返回用户信息"""
    name = "张三"
    age = 25
    city = "北京"
    return name, age, city

user_name, user_age, user_city = get_user_info()
print(f"用户信息: {user_name}, {user_age}岁, {user_city}")

# 返回列表或字典
def get_student_grades():
    """返回学生成绩"""
    return {
        "math": 85,
        "english": 92,
        "physics": 78
    }

grades = get_student_grades()
print(f"学生成绩: {grades}")

# ===== 4. 函数文档字符串 =====

print("\n=== 函数文档字符串 ===")

def calculate_bmi(weight, height):
    """
    计算BMI指数

    Args:
        weight (float): 体重（公斤）
        height (float): 身高（米）

    Returns:
        float: BMI值

    Examples:
        >>> calculate_bmi(70, 1.75)
        22.857142857142858
    """
    return weight / (height ** 2)

print(f"BMI计算: {calculate_bmi(70, 1.75):.2f}")
print(f"函数文档: {calculate_bmi.__doc__}")

# ===== 5. 函数作用域 =====

print("\n=== 函数作用域 ===")

# 全局变量
global_var = "我是全局变量"

def test_scope():
    """测试变量作用域"""
    local_var = "我是局部变量"
    print(f"函数内部: global_var = {global_var}")
    print(f"函数内部: local_var = {local_var}")

test_scope()

# 尝试访问局部变量（会报错）
# print(local_var)  # NameError

# 使用global关键字修改全局变量
def modify_global():
    """修改全局变量"""
    global global_var
    global_var = "全局变量已被修改"

modify_global()
print(f"修改后的全局变量: {global_var}")

# nonlocal关键字（用于嵌套函数）
def outer_function():
    """外层函数"""
    outer_var = "外层变量"

    def inner_function():
        """内层函数"""
        nonlocal outer_var
        outer_var = "外层变量已被内层函数修改"
        print(f"内层函数: {outer_var}")

    inner_function()
    print(f"外层函数: {outer_var}")

outer_function()

# ===== 6. 函数作为对象 =====

print("\n=== 函数作为对象 ===")

def multiply(x, y):
    return x * y

def add(x, y):
    return x + y

# 函数赋值给变量
operation = multiply
result = operation(5, 3)
print(f"5 * 3 = {result}")

operation = add
result = operation(5, 3)
print(f"5 + 3 = {result}")

# 函数作为参数传递
def apply_operation(func, x, y):
    """应用操作函数"""
    return func(x, y)

print(f"应用乘法: {apply_operation(multiply, 4, 5)}")
print(f"应用加法: {apply_operation(add, 4, 5)}")

# 函数作为返回值
def get_operation(operation_type):
    """返回操作函数"""
    if operation_type == "add":
        return add
    elif operation_type == "multiply":
        return multiply
    else:
        return None

add_func = get_operation("add")
multiply_func = get_operation("multiply")

print(f"动态获取的加法函数: {add_func(10, 5)}")
print(f"动态获取的乘法函数: {multiply_func(10, 5)}")

# ===== 7. Lambda表达式 =====

print("\n=== Lambda表达式 ===")

# 基本lambda
square = lambda x: x ** 2
print(f"lambda平方: {square(5)}")

# 多参数lambda
add_lambda = lambda x, y: x + y
print(f"lambda加法: {add_lambda(3, 4)}")

# lambda在函数式编程中的应用
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 使用lambda进行过滤
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"偶数: {even_numbers}")

# 使用lambda进行映射
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(f"平方数: {squared_numbers}")

# 使用lambda进行排序
words = ["apple", "Banana", "cherry", "Date"]
sorted_words = sorted(words, key=lambda x: x.lower())
print(f"忽略大小写排序: {sorted_words}")

# ===== 8. 高阶函数 =====

print("\n=== 高阶函数 ===")

# map函数
def double(x):
    return x * 2

numbers = [1, 2, 3, 4, 5]
doubled = list(map(double, numbers))
print(f"map双倍: {doubled}")

# filter函数
def is_even(x):
    return x % 2 == 0

even_nums = list(filter(is_even, numbers))
print(f"filter偶数: {even_nums}")

# reduce函数
from functools import reduce

def add_two(x, y):
    return x + y

total = reduce(add_two, numbers)
print(f"reduce求和: {total}")

# ===== 9. 函数注解 =====

print("\n=== 函数注解 ===")

def greeting(name: str, age: int = 25) -> str:
    """
    带类型注解的问候函数

    Args:
        name: 姓名
        age: 年龄，默认25

    Returns:
        问候字符串
    """
    return f"Hello, {name}! You are {age} years old."

print(greeting("张三", 30))
print(f"函数注解: {greeting.__annotations__}")

# ===== 10. 递归函数 =====

print("\n=== 递归函数 ===")

def factorial(n: int) -> int:
    """计算阶乘（递归）"""
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

print(f"5! = {factorial(5)}")

# 斐波那契数列
def fibonacci(n: int) -> int:
    """斐波那契数列（递归）"""
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(f"斐波那契第8项: {fibonacci(8)}")

# 递归深度限制
import sys
print(f"递归深度限制: {sys.getrecursionlimit()}")

# ===== 练习 =====

print("\n=== 练习时间 ===")

# 练习1: 数学计算器
def calculator():
    """简单的数学计算器"""

    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y == 0:
            return "除数不能为0"
        return x / y

    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }

    print("简单计算器:")
    print("支持操作: +, -, *, /")

    # 模拟计算
    result1 = operations['+'](10, 5)
    result2 = operations['*'](6, 7)
    result3 = operations['/'](15, 3)

    print(f"10 + 5 = {result1}")
    print(f"6 * 7 = {result2}")
    print(f"15 / 3 = {result3}")

# 练习2: 函数式编程示例
def functional_programming_demo():
    """函数式编程演示"""

    # 数据
    numbers = list(range(1, 21))  # 1-20

    # 使用函数式方法处理数据
    result = list(map(
        lambda x: x ** 2,  # 平方
        filter(
            lambda x: x % 2 == 0,  # 筛选偶数
            numbers
        )
    ))

    print(f"1-20的偶数平方: {result}")

    # 传统方法对比
    traditional_result = []
    for num in numbers:
        if num % 2 == 0:
            traditional_result.append(num ** 2)

    print(f"传统方法结果: {traditional_result}")
    print(f"结果是否相同: {result == traditional_result}")

# 练习3: 装饰器基础（预览）
def timing_decorator(func):
    """计时装饰器"""
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(".4f")
        return result
    return wrapper

@timing_decorator
def slow_function(n):
    """模拟耗时函数"""
    import time
    time.sleep(0.1)  # 模拟0.1秒耗时
    return sum(range(n))

# 练习4: 函数参数验证
def validate_params(func):
    """参数验证装饰器"""
    def wrapper(*args, **kwargs):
        # 检查参数类型
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError(f"参数必须是数字类型，得到的是 {type(arg)}")

        for value in kwargs.values():
            if not isinstance(value, (int, float)):
                raise TypeError(f"参数必须是数字类型，得到的是 {type(value)}")

        return func(*args, **kwargs)
    return wrapper

@validate_params
def safe_add(x, y):
    """安全的加法函数"""
    return x + y

# 运行练习
print("练习1: 数学计算器")
calculator()

print("\n练习2: 函数式编程示例")
functional_programming_demo()

print("\n练习3: 装饰器预览")
result = slow_function(1000)
print(f"函数结果: {result}")

print("\n练习4: 参数验证")
try:
    print(f"安全加法: {safe_add(5, 3)}")
    # print(safe_add(5, "3"))  # 这会报错
except TypeError as e:
    print(f"类型错误: {e}")
