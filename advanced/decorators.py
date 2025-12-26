# Python学习项目 - 高级特性：装饰器
# 学习序号：第7阶段 第1课 - 装饰器
# 建议学习时间：90-120分钟
# 前置知识：第1-6阶段 - 基础到标准库
# 下一课：第7阶段 第2课 - 生成器和迭代器 (generators.py)
# 本模块介绍Python装饰器的概念、使用方法和实际应用

"""
装饰器(Decorators)是Python的高级特性之一，它允许我们在不修改函数本身的情况下，
动态地修改函数的行为。装饰器本质上是一个接受函数作为参数并返回新函数的可调用对象。

装饰器的主要用途：
1. 日志记录 (Logging)
2. 性能监控 (Performance monitoring)
3. 缓存 (Caching)
4. 权限验证 (Authorization)
5. 错误处理 (Error handling)
6. 调试 (Debugging)
"""

import time
import functools
from typing import Callable, Any
import logging

# ===== 1. 装饰器基础 =====

print("=== 装饰器基础 ===")

# 基本装饰器示例
def simple_decorator(func):
    """最简单的装饰器"""
    def wrapper(*args, **kwargs):
        print(f"调用函数: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"函数 {func.__name__} 执行完成")
        return result
    return wrapper

@simple_decorator
def greet(name):
    """被装饰的函数"""
    return f"Hello, {name}!"

# 等价于: greet = simple_decorator(greet)
print(greet("Alice"))

# ===== 2. 带参数的装饰器 =====

print("\n=== 带参数的装饰器 ===")

def repeat(times):
    """让函数重复执行的装饰器"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for i in range(times):
                print(f"第{i+1}次执行 {func.__name__}")
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator

@repeat(times=3)
def say_hello(name):
    return f"Hello, {name}!"

results = say_hello("Bob")
print(f"执行结果: {results}")

# ===== 3. 使用functools.wraps保持函数元信息 =====

print("\n=== 使用functools.wraps保持函数元信息 ===")

def timing_decorator(func):
    """计时装饰器"""
    @functools.wraps(func)  # 保持原始函数的元信息
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(".4f")
        return result
    return wrapper

@timing_decorator
def slow_function(n):
    """模拟耗时函数"""
    time.sleep(0.1)  # 模拟0.1秒耗时
    return sum(range(n))

print(f"函数名: {slow_function.__name__}")  # 应该显示 slow_function
print(f"文档字符串: {slow_function.__doc__}")
result = slow_function(1000)

# ===== 4. 多个装饰器 =====

print("\n=== 多个装饰器 ===")

def uppercase_decorator(func):
    """将返回值转换为大写的装饰器"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return str(result).upper()
    return wrapper

def exclamation_decorator(func):
    """添加感叹号的装饰器"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"{result}!!!"
    return wrapper

@uppercase_decorator
@exclamation_decorator
def get_message(name):
    return f"hello {name}"

# 等价于: get_message = uppercase_decorator(exclamation_decorator(get_message))
print(f"装饰后的结果: {get_message('world')}")

# ===== 5. 类装饰器 =====

print("\n=== 类装饰器 ===")

class CountCalls:
    """统计函数调用次数的类装饰器"""

    def __init__(self, func):
        self.func = func
        self.call_count = 0
        functools.update_wrapper(self, func)  # 保持函数元信息

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        print(f"调用 {self.func.__name__}，这是第{self.call_count}次调用")
        return self.func(*args, **kwargs)

@CountCalls
def fibonacci(n):
    """计算斐波那契数"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(f"fibonacci(5) = {fibonacci(5)}")
print(f"fibonacci(3) = {fibonacci(3)}")

# ===== 6. 装饰器的实际应用 =====

print("\n=== 装饰器的实际应用 ===")

# 应用1: 日志记录装饰器
def logger(func):
    """日志记录装饰器"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"调用函数: {func.__name__}，参数: {args}, 关键字参数: {kwargs}")
        try:
            result = func(*args, **kwargs)
            logging.info(f"函数 {func.__name__} 执行成功，返回: {result}")
            return result
        except Exception as e:
            logging.error(f"函数 {func.__name__} 执行失败: {e}")
            raise
    return wrapper

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@logger
def divide(a, b):
    """除法运算"""
    return a / b

try:
    print(f"10 / 2 = {divide(10, 2)}")
    print(f"10 / 0 = {divide(10, 0)}")
except ZeroDivisionError:
    pass

# 应用2: 缓存装饰器
def cache(func):
    """简单的缓存装饰器"""
    cache_dict = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 创建缓存键
        key = str(args) + str(sorted(kwargs.items()))

        if key in cache_dict:
            print(f"从缓存获取: {func.__name__}{args}")
            return cache_dict[key]

        print(f"计算: {func.__name__}{args}")
        result = func(*args, **kwargs)
        cache_dict[key] = result
        return result

    # 添加清空缓存的方法
    wrapper.clear_cache = lambda: cache_dict.clear()
    return wrapper

@cache
def expensive_computation(n):
    """模拟耗时的计算"""
    time.sleep(0.1)  # 模拟耗时
    return n * n + n

print(f"\n第一次计算 expensive_computation(5): {expensive_computation(5)}")
print(f"第二次计算 expensive_computation(5): {expensive_computation(5)}")  # 从缓存获取
print(f"计算 expensive_computation(3): {expensive_computation(3)}")

# 清空缓存
expensive_computation.clear_cache()
print(f"清空缓存后再次计算 expensive_computation(5): {expensive_computation(5)}")

# 应用3: 权限验证装饰器
def require_permission(permission):
    """权限验证装饰器"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(user, *args, **kwargs):
            if not hasattr(user, 'permissions'):
                raise PermissionError("用户对象没有权限信息")

            if permission not in user.permissions:
                raise PermissionError(f"用户没有 {permission} 权限")

            print(f"权限验证通过: {user.name} 可以执行 {func.__name__}")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

class User:
    """用户类"""
    def __init__(self, name, permissions=None):
        self.name = name
        self.permissions = permissions or []

@require_permission("admin")
def delete_user(admin_user, target_user):
    """删除用户（需要管理员权限）"""
    return f"管理员 {admin_user.name} 删除了用户 {target_user.name}"

@require_permission("read")
def view_profile(user, profile_user):
    """查看用户资料（需要读取权限）"""
    return f"{user.name} 查看了 {profile_user.name} 的资料"

# 创建用户
admin = User("管理员", ["admin", "read", "write"])
normal_user = User("普通用户", ["read"])
guest = User("访客", [])

try:
    print(delete_user(admin, normal_user))
    print(view_profile(normal_user, admin))
    print(delete_user(normal_user, admin))  # 权限不足
except PermissionError as e:
    print(f"权限错误: {e}")

# ===== 7. 内置装饰器 =====

print("\n=== 内置装饰器 ===")

# @staticmethod 静态方法装饰器
class MathUtils:
    """数学工具类"""

    @staticmethod
    def add(a, b):
        """静态方法：加法"""
        return a + b

    @staticmethod
    def multiply(a, b):
        """静态方法：乘法"""
        return a * b

    @classmethod
    def create_from_string(cls, expression):
        """类方法：从字符串创建实例"""
        # 这里简化处理，实际应该解析表达式
        return cls()

    def __init__(self):
        self.operations = []

print(f"静态方法调用: MathUtils.add(5, 3) = {MathUtils.add(5, 3)}")

# @property 属性装饰器
class Temperature:
    """温度类"""

    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        """摄氏度属性"""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """设置摄氏度"""
        if value < -273.15:
            raise ValueError("温度不能低于绝对零度")
        self._celsius = value

    @property
    def fahrenheit(self):
        """华氏度属性（只读）"""
        return self._celsius * 9/5 + 32

temp = Temperature(25)
print(f"摄氏度: {temp.celsius}°C")
print(f"华氏度: {temp.fahrenheit}°F")

temp.celsius = 30
print(f"修改后摄氏度: {temp.celsius}°C, 华氏度: {temp.fahrenheit}°F")

# ===== 8. 装饰器模式与函数式编程 =====

print("\n=== 装饰器模式与函数式编程 ===")

# 函数式装饰器组合
def compose(*decorators):
    """组合多个装饰器"""
    def decorator(func):
        for dec in reversed(decorators):
            func = dec(func)
        return func
    return decorator

# 定义一些简单的装饰器
def add_brackets(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"[{result}]"
    return wrapper

def add_stars(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"*{result}*"
    return wrapper

def uppercase(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return str(result).upper()
    return wrapper

@compose(add_brackets, add_stars, uppercase)
def get_greeting(name):
    return f"hello {name}"

print(f"组合装饰器结果: {get_greeting('python')}")

# ===== 9. 装饰器的陷阱和最佳实践 =====

print("\n=== 装饰器的陷阱和最佳实践 ===")

# 陷阱1: 装饰器会改变函数的身份
def problematic_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    # 没有使用 @functools.wraps
    return wrapper

@problematic_decorator
def original_func():
    """原始函数"""
    pass

print(f"装饰后函数名: {original_func.__name__}")  # 显示 wrapper
print(f"装饰后文档: {original_func.__doc__}")     # 显示 None

# 最佳实践：总是使用 @functools.wraps

# 陷阱2: 可变默认参数
def bad_cache_decorator(func):
    cache = {}  # 这个字典在装饰器定义时就被创建了

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

@bad_cache_decorator
def add_counter(x):
    return x + 1

print(f"add_counter(5): {add_counter(5)}")
print(f"add_counter(5) again: {add_counter(5)}")  # 应该从缓存返回

# ===== 练习 =====

print("\n=== 练习时间 ===")

# 练习1: 创建一个性能监控装饰器
def performance_monitor(func):
    """性能监控装饰器"""
    call_count = 0
    total_time = 0

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal call_count, total_time

        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        execution_time = end_time - start_time
        call_count += 1
        total_time += execution_time

        avg_time = total_time / call_count

        print(f"函数 {func.__name__} 执行时间: {execution_time:.4f}s")
        print(f"平均执行时间: {avg_time:.4f}s (共调用{call_count}次)")

        return result
    return wrapper

@performance_monitor
def fibonacci_recursive(n):
    """递归计算斐波那契数"""
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

print(f"fibonacci_recursive(10) = {fibonacci_recursive(10)}")
print(f"fibonacci_recursive(15) = {fibonacci_recursive(15)}")

# 练习2: 创建一个重试装饰器
def retry(max_attempts=3, delay=1):
    """重试装饰器"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts == max_attempts:
                        print(f"函数 {func.__name__} 在 {max_attempts} 次尝试后仍然失败")
                        raise e
                    print(f"函数 {func.__name__} 第 {attempts} 次尝试失败: {e}")
                    time.sleep(delay)
            return None
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.5)
def unreliable_function():
    """不可靠的函数（随机失败）"""
    import random
    if random.random() < 0.7:  # 70% 的概率失败
        raise ConnectionError("网络连接失败")
    return "成功执行"

try:
    result = unreliable_function()
    print(f"最终结果: {result}")
except ConnectionError as e:
    print(f"所有重试都失败: {e}")

# 练习3: 创建一个类型检查装饰器
def type_check(*expected_types):
    """类型检查装饰器"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 检查位置参数
            for i, (arg, expected_type) in enumerate(zip(args, expected_types)):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"参数 {i+1} 期望类型 {expected_type.__name__}，"
                                  f"得到 {type(arg).__name__}")

            result = func(*args, **kwargs)

            # 如果有返回值类型检查（简化版）
            return result
        return wrapper
    return decorator

@type_check(int, int)
def add_integers(a, b):
    """只接受整数的加法函数"""
    return a + b

try:
    print(f"add_integers(5, 3) = {add_integers(5, 3)}")
    print(f"add_integers(5, '3') = {add_integers(5, '3')}")
except TypeError as e:
    print(f"类型检查错误: {e}")

# 练习4: 创建一个单例模式装饰器
def singleton(cls):
    """单例模式装饰器"""
    instances = {}

    @functools.wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class DatabaseConnection:
    """数据库连接类（单例）"""

    def __init__(self, host="localhost", port=5432):
        self.host = host
        self.port = port
        self.connected = False
        print(f"创建数据库连接: {host}:{port}")

    def connect(self):
        if not self.connected:
            self.connected = True
            print("数据库已连接")
        else:
            print("数据库已经连接")

# 测试单例模式
db1 = DatabaseConnection("localhost", 5432)
db2 = DatabaseConnection("remotehost", 5432)  # 应该返回同一个实例

print(f"db1 is db2: {db1 is db2}")  # 应该是 True
print(f"db1.host: {db1.host}, db2.host: {db2.host}")

db1.connect()
db2.connect()  # 应该显示已经连接

print("\n装饰器学习完成！装饰器是Python最强大的特性之一，掌握它能大大提高代码的可复用性和可维护性。")
