# Python学习项目 - 中级内容：模块和包
# 学习序号：第3阶段 第2课 - 模块和包
# 建议学习时间：60-90分钟
# 前置知识：第3阶段 第1课 - 函数基础
# 下一课：第4阶段 第1课 - 面向对象基础 (oop_basics.py)
# 本模块介绍Python模块的导入、使用和管理

# ===== 1. 模块基础 =====

print("=== 模块基础 ===")

# 导入标准库模块
import math
import datetime
import random

# 使用模块中的函数
print(f"圆周率: {math.pi}")
print(f"当前时间: {datetime.datetime.now()}")
print(f"随机数: {random.randint(1, 100)}")

# ===== 2. 不同的导入方式 =====

print("\n=== 不同的导入方式 ===")

# 方式1: import 模块名
import os
print(f"当前工作目录: {os.getcwd()}")

# 方式2: from 模块名 import 函数名
from sys import platform, version
print(f"平台: {platform}")
print(f"Python版本: {version}")

# 方式3: from 模块名 import *
from collections import Counter, defaultdict, deque
counter = Counter([1, 2, 2, 3, 3, 3])
print(f"计数器: {counter}")

# 方式4: import 模块名 as 别名
import numpy as np  # 假设安装了numpy
import pandas as pd  # 假设安装了pandas

# ===== 3. 自定义模块 =====

print("\n=== 自定义模块 ===")

# 创建一个简单的自定义模块示例
# 我们将创建一个名为utils的模块

# 首先创建utils.py文件（这里用代码模拟）
utils_code = '''
def greet(name):
    """问候函数"""
    return f"Hello, {name}!"

def calculate_area(radius):
    """计算圆面积"""
    import math
    return math.pi * radius ** 2

def get_current_time():
    """获取当前时间"""
    import datetime
    return datetime.datetime.now()

PI = 3.14159
AUTHOR = "Python学习项目"
'''

# 将代码写入文件
with open('python_learning/utils/utils_module.py', 'w', encoding='utf-8') as f:
    f.write(utils_code)

# 导入自定义模块
import sys
sys.path.append('python_learning/utils')

try:
    import utils_module

    print(f"自定义模块问候: {utils_module.greet('张三')}")
    print(f"圆面积: {utils_module.calculate_area(5):.2f}")
    print(f"PI值: {utils_module.PI}")
    print(f"作者: {utils_module.AUTHOR}")

except ImportError as e:
    print(f"导入错误: {e}")

# ===== 4. 包(Package)的概念 =====

print("\n=== 包(Package)的概念 ===")

# 创建包结构
package_structure = '''
python_learning/
├── __init__.py
├── utils/
│   ├── __init__.py
│   ├── math_utils.py
│   └── string_utils.py
└── ...
'''

print("包结构示例:")
print(package_structure)

# 创建包文件
math_utils_code = '''
def add(a, b):
    """加法"""
    return a + b

def multiply(a, b):
    """乘法"""
    return a * b

def power(base, exp):
    """幂运算"""
    return base ** exp
'''

string_utils_code = '''
def capitalize_words(text):
    """首字母大写"""
    return text.title()

def count_words(text):
    """统计单词数"""
    return len(text.split())

def reverse_string(text):
    """反转字符串"""
    return text[::-1]
'''

# 创建__init__.py文件（使目录成为包）
init_code = '''
# 包初始化文件
print("utils包已加载")

__version__ = "1.0.0"
__author__ = "Python学习项目"
'''

# 写入文件
with open('python_learning/utils/__init__.py', 'w', encoding='utf-8') as f:
    f.write(init_code)

with open('python_learning/utils/math_utils.py', 'w', encoding='utf-8') as f:
    f.write(math_utils_code)

with open('python_learning/utils/string_utils.py', 'w', encoding='utf-8') as f:
    f.write(string_utils_code)

# 导入包和子模块
try:
    from utils import math_utils, string_utils

    print(f"数学运算: 2^3 = {math_utils.power(2, 3)}")
    print(f"字符串处理: {string_utils.capitalize_words('hello world')}")
    print(f"单词统计: {string_utils.count_words('This is a test sentence')}")

except ImportError as e:
    print(f"导入包错误: {e}")

# ===== 5. 相对导入 =====

print("\n=== 相对导入 ===")

# 在包内部的相对导入示例
subpackage_example = '''
utils/
├── __init__.py
├── math_utils.py
├── string_utils.py
└── advanced/
    ├── __init__.py
    └── calculations.py  # 在这里可以使用 from ..math_utils import add
'''

print("相对导入示例:")
print(subpackage_example)

# ===== 6. 模块搜索路径 =====

print("\n=== 模块搜索路径 ===")

import sys

print("Python模块搜索路径:")
for i, path in enumerate(sys.path, 1):
    print(f"{i}. {path}")

# 添加自定义路径
custom_path = "python_learning"
if custom_path not in sys.path:
    sys.path.insert(0, custom_path)
    print(f"\n已添加自定义路径: {custom_path}")

# ===== 7. 内置模块探索 =====

print("\n=== 内置模块探索 ===")

# 查看所有内置模块
import builtins

print("一些常用的内置函数:")
builtin_functions = [
    'abs', 'all', 'any', 'bin', 'bool', 'bytearray', 'bytes', 'chr',
    'dict', 'enumerate', 'filter', 'float', 'format', 'frozenset',
    'int', 'len', 'list', 'map', 'max', 'min', 'ord', 'pow', 'range',
    'reversed', 'round', 'set', 'slice', 'sorted', 'str', 'sum', 'tuple',
    'type', 'zip'
]

for func in builtin_functions[:10]:  # 只显示前10个
    print(f"  - {func}")

# ===== 8. 模块重载 =====

print("\n=== 模块重载 ===")

import importlib

# 重新加载模块
try:
    importlib.reload(utils_module)
    print("模块已重新加载")
except NameError:
    print("模块不存在，无法重载")

# ===== 9. 查看模块信息 =====

print("\n=== 查看模块信息 ===")

def inspect_module(module):
    """检查模块信息"""
    print(f"模块名: {module.__name__}")
    print(f"文件路径: {getattr(module, '__file__', 'N/A')}")

    if hasattr(module, '__doc__') and module.__doc__:
        print(f"文档: {module.__doc__.strip()[:100]}...")

    # 查看模块中的属性
    attrs = [attr for attr in dir(module) if not attr.startswith('_')]
    print(f"公开属性 ({len(attrs)}个): {attrs[:10]}...")  # 只显示前10个

# 检查math模块
inspect_module(math)

# ===== 10. 常见标准库模块 =====

print("\n=== 常见标准库模块 ===")

# os模块 - 操作系统接口
print("OS模块示例:")
print(f"  当前目录: {os.getcwd()}")
print(f"  目录列表: {os.listdir('.')[:5]}...")  # 只显示前5个

# json模块 - JSON数据处理
import json

data = {"name": "张三", "age": 25, "city": "北京"}
json_str = json.dumps(data, ensure_ascii=False)
parsed_data = json.loads(json_str)

print(f"JSON编码: {json_str}")
print(f"JSON解码: {parsed_data}")

# re模块 - 正则表达式
import re

text = "邮箱: user@example.com, 电话: 138-1234-5678"
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
phones = re.findall(r'\d{3}-\d{4}-\d{4}', text)

print(f"找到邮箱: {emails}")
print(f"找到电话: {phones}")

# ===== 练习 =====

print("\n=== 练习时间 ===")

# 练习1: 创建一个简单的计算器模块
calculator_code = '''
def add(a, b):
    """加法"""
    return a + b

def subtract(a, b):
    """减法"""
    return a - b

def multiply(a, b):
    """乘法"""
    return a * b

def divide(a, b):
    """除法"""
    if b == 0:
        raise ValueError("除数不能为0")
    return a / b

def power(a, b):
    """幂运算"""
    return a ** b

def sqrt(a):
    """平方根"""
    import math
    if a < 0:
        raise ValueError("不能计算负数的平方根")
    return math.sqrt(a)
'''

with open('python_learning/utils/calculator.py', 'w', encoding='utf-8') as f:
    f.write(calculator_code)

try:
    from utils import calculator

    print("计算器模块测试:")
    print(f"5 + 3 = {calculator.add(5, 3)}")
    print(f"10 - 4 = {calculator.subtract(10, 4)}")
    print(f"6 * 7 = {calculator.multiply(6, 7)}")
    print(f"15 / 3 = {calculator.divide(15, 3)}")
    print(f"2^3 = {calculator.power(2, 3)}")
    print(f"√16 = {calculator.sqrt(16)}")

except ImportError as e:
    print(f"计算器模块导入错误: {e}")

# 练习2: 包的__init__.py文件
init_content = '''
"""
Utils工具包

提供各种实用工具函数
"""

from .math_utils import add, multiply, power
from .string_utils import capitalize_words, count_words
from .calculator import add as calc_add, subtract, multiply as calc_multiply

__version__ = "1.0.0"
__author__ = "Python学习项目"

def get_version():
    """获取版本信息"""
    return f"Utils v{__version__} by {__author__}"
'''

with open('python_learning/utils/__init__.py', 'w', encoding='utf-8') as f:
    f.write(init_content)

# 重新导入包
try:
    import importlib
    import utils
    importlib.reload(utils)

    print(f"\n包版本: {utils.get_version()}")
    print(f"直接调用add: {utils.add(10, 5)}")
    print(f"字符串处理: {utils.capitalize_words('hello python')}")

except Exception as e:
    print(f"包重新导入错误: {e}")

# 练习3: 探索标准库
def explore_stdlib():
    """探索标准库模块"""

    modules_to_explore = [
        ('os', '操作系统接口'),
        ('sys', '系统相关'),
        ('datetime', '日期时间'),
        ('json', 'JSON处理'),
        ('re', '正则表达式'),
        ('collections', '容器数据类型'),
        ('itertools', '迭代器工具'),
        ('functools', '函数工具'),
    ]

    print("标准库模块探索:")
    for module_name, description in modules_to_explore:
        try:
            module = __import__(module_name)
            attrs_count = len([attr for attr in dir(module) if not attr.startswith('_')])
            print(f"  {module_name} ({description}): {attrs_count}个公开属性")
        except ImportError:
            print(f"  {module_name} ({description}): 不可用")

explore_stdlib()

# ===== 清理创建的文件 =====
print("\n清理临时文件...")
import os
temp_files = [
    'python_learning/utils/utils_module.py',
    'python_learning/utils/calculator.py'
]

for file_path in temp_files:
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"已删除: {file_path}")

# ===== 11. __name__ 属性和 __main__ =====

print("\n=== __name__ 属性和 __main__ ===")

# 每个Python模块都有一个内置的 __name__ 属性
print(f"当前模块的 __name__: {__name__}")

# 当模块被直接运行时，__name__ 的值是 "__main__"
# 当模块被其他模块导入时，__name__ 是模块的文件名（不含.py扩展名）

# 这是一个重要的模式，用于区分模块是被直接运行还是被导入
if __name__ == "__main__":
    print("这个模块是被直接运行的!")
    print("通常在这里放置测试代码或主程序逻辑")
else:
    print("这个模块被其他模块导入了")

# ===== 实际应用示例 =====

# 创建一个示例模块来演示
main_example_code = '''
def hello():
    """打招呼函数"""
    return "Hello from example module!"

def calculate(x, y):
    """计算函数"""
    return x + y

# 这部分代码只在模块被直接运行时执行
if __name__ == "__main__":
    print("=== 模块直接运行测试 ===")
    print(hello())
    print(f"计算结果: {calculate(5, 3)}")

    # 这里可以添加更多的测试代码
    import sys
    print(f"命令行参数: {sys.argv}")
'''

with open('python_learning/utils/main_example.py', 'w', encoding='utf-8') as f:
    f.write(main_example_code)

print("\n创建了示例模块 main_example.py")

# 演示不同的运行方式
print("演示模块的不同运行方式:")

# 方式1: 导入模块（__name__ 不会是 "__main__"）
print("\n1. 导入模块:")
try:
    import sys
    sys.path.append('python_learning/utils')

    # 这里只是演示，实际导入会设置 __name__ 为模块名
    print("当模块被导入时，__name__ = 'main_example'")

except ImportError as e:
    print(f"导入错误: {e}")

# ===== __name__ == "__main__" 的最佳实践 =====

print("\n=== __name__ == '__main__' 的最佳实践 ===")

# 最佳实践1: 用于测试代码
def fibonacci(n):
    """计算斐波那契数"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def is_prime(n):
    """检查是否为素数"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 测试代码只在直接运行时执行
if __name__ == "__main__":
    print("\n=== 函数测试 ===")

    # 测试斐波那契函数
    print("斐波那契数列:")
    for i in range(10):
        print(f"  F({i}) = {fibonacci(i)}")

    # 测试素数检查
    print("\n素数检查:")
    test_numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    for num in test_numbers:
        result = "是素数" if is_prime(num) else "不是素数"
        print(f"  {num} {result}")

# 最佳实践2: 用于命令行工具
def process_file(filename):
    """处理文件"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            return f"文件 {filename} 包含 {len(content)} 个字符"
    except FileNotFoundError:
        return f"文件 {filename} 不存在"

if __name__ == "__main__":
    print("\n=== 命令行工具示例 ===")
    import sys

    if len(sys.argv) > 1:
        # 从命令行获取文件名
        filename = sys.argv[1]
        result = process_file(filename)
        print(result)
    else:
        print("用法: python modules.py <文件名>")
        print("示例: python modules.py test.txt")

# 最佳实践3: 用于模块演示
class CalculatorDemo:
    """计算器演示类"""

    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

    def power(self, a, b):
        return a ** b

if __name__ == "__main__":
    print("\n=== 模块演示 ===")
    calc = CalculatorDemo()

    print("计算器功能演示:")
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"4 * 7 = {calc.multiply(4, 7)}")
    print(f"2^8 = {calc.power(2, 8)}")

# ===== 为什么需要 __name__ == "__main__" =====

print("\n=== 为什么需要 __name__ == '__main__' ===")

# 问题场景：如果没有这个检查，会发生什么？
print("如果没有 __name__ == '__main__' 检查:")

# 示例1: 导入时执行的代码
print("  - 导入模块时，所有顶层代码都会执行")
print("  - 可能导致意外的副作用")
print("  - 测试代码会在导入时运行")
print("  - 命令行参数处理会在导入时执行")

# 示例2: 演示导入时的行为
print("\n导入时的行为演示:")
print(f"当前模块的 __name__: {__name__}")

# ===== 练习 =====

print("\n=== 练习时间 ===")

# 练习1: 创建一个带有测试代码的模块
exercise_module_code = '''
"""
练习模块：数学工具
"""

import math

def area_of_circle(radius):
    """计算圆面积"""
    return math.pi * radius ** 2

def volume_of_sphere(radius):
    """计算球体积"""
    return (4/3) * math.pi * radius ** 3

def gcd(a, b):
    """计算最大公约数"""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """计算最小公倍数"""
    return abs(a * b) // gcd(a, b)

# 测试代码只在直接运行时执行
if __name__ == "__main__":
    print("=== 数学工具测试 ===")

    # 测试圆面积
    radius = 5
    area = area_of_circle(radius)
    print(f"半径为{radius}的圆面积: {area:.2f}")

    # 测试球体积
    volume = volume_of_sphere(radius)
    print(f"半径为{radius}的球体积: {volume:.2f}")

    # 测试最大公约数和最小公倍数
    a, b = 12, 18
    print(f"{a}和{b}的最大公约数: {gcd(a, b)}")
    print(f"{a}和{b}的最小公倍数: {lcm(a, b)}")

    # 批量测试
    test_pairs = [(15, 25), (100, 75), (7, 11)]
    print("\n批量测试GCD和LCM:")
    for x, y in test_pairs:
        print(f"  {x},{y} -> GCD: {gcd(x, y)}, LCM: {lcm(x, y)}")
'''

with open('python_learning/utils/math_tools.py', 'w', encoding='utf-8') as f:
    f.write(exercise_module_code)

print("创建了练习模块 math_tools.py")

# 练习2: 演示模块导入行为
print("\n练习2: 模块导入行为演示")

# 演示：导入时会执行顶层代码，但测试代码不会运行
print("导入 math_tools 模块...")
try:
    import sys
    if 'python_learning/utils' not in sys.path:
        sys.path.insert(0, 'python_learning/utils')

    # 导入模块（这会执行模块中的顶层代码，但不会执行测试代码）
    import math_tools

    print("模块导入成功！")
    print(f"可以调用函数: {math_tools.area_of_circle(3):.2f}")

except ImportError as e:
    print(f"导入失败: {e}")

# 练习3: 命令行脚本示例
print("\n练习3: 命令行脚本示例")

script_example = '''
#!/usr/bin/env python3
"""
命令行脚本示例
用法: python script_example.py <数字1> <数字2>
"""

import sys

def main():
    """主函数"""
    if len(sys.argv) != 3:
        print("用法: python script_example.py <数字1> <数字2>")
        sys.exit(1)

    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])

        print(f"输入的数字: {num1}, {num2}")
        print(f"相加: {num1 + num2}")
        print(f"相乘: {num1 * num2}")
        print(f"较大值: {max(num1, num2)}")

    except ValueError as e:
        print(f"错误: 请输入有效的数字")
        print(f"详细错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
'''

with open('python_learning/utils/script_example.py', 'w', encoding='utf-8') as f:
    f.write(script_example)

print("创建了命令行脚本示例 script_example.py")

# ===== 清理练习文件 =====
print("\n清理练习文件...")
exercise_files = [
    'python_learning/utils/main_example.py',
    'python_learning/utils/math_tools.py',
    'python_learning/utils/script_example.py'
]

for file_path in exercise_files:
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"已清理: {file_path}")
    except OSError as e:
        print(f"清理失败 {file_path}: {e}")

print("\n__name__ 和 __main__ 学习完成！")
print("记住：if __name__ == '__main__' 是Python编程的重要习惯！")

print("模块和包学习完成!")
