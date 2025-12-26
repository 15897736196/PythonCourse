# Python学习项目 - 高级特性：生成器和迭代器
# 学习序号：第7阶段 第2课 - 生成器和迭代器
# 建议学习时间：90-120分钟
# 前置知识：第7阶段 第1课 - 装饰器
# 下一课：第7阶段 第3课 - 上下文管理器 (context_managers.py)
# 本模块介绍Python生成器和迭代器的概念、使用方法和实际应用

"""
生成器(Generators)和迭代器(Iterators)是Python中处理序列数据的高效方式。

主要概念：
1. 可迭代对象(Iterable): 可以使用for循环遍历的对象
2. 迭代器(Iterator): 实现了__iter__()和__next__()方法的对象
3. 生成器函数: 使用yield语句的函数，返回生成器对象
4. 生成器表达式: 类似列表推导式，但返回生成器

生成器的优势：
- 内存高效：不需要一次性加载所有数据
- 惰性求值：按需计算值
- 可以表示无限序列
- 简化代码逻辑
"""

import time
import sys
from typing import Generator, Iterator, Iterable, Any, List

# ===== 1. 迭代器基础 =====

print("=== 迭代器基础 ===")

# 创建一个简单的迭代器
class Countdown:
    """倒计时迭代器"""

    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

# 使用迭代器
countdown = Countdown(5)
print("倒计时:")
for num in countdown:
    print(f"  {num}")

# 手动使用迭代器
countdown_iter = iter(Countdown(3))
try:
    while True:
        print(f"手动迭代: {next(countdown_iter)}")
except StopIteration:
    print("迭代结束")

# ===== 2. 生成器函数 =====

print("\n=== 生成器函数 ===")

def fibonacci_generator(n):
    """斐波那契数列生成器"""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# 使用生成器
fib_gen = fibonacci_generator(10)
print("斐波那契数列:")
for num in fib_gen:
    print(f"  {num}", end=" ")
print()

# 生成器是迭代器
print(f"fib_gen 是迭代器: {hasattr(fib_gen, '__next__')}")

# 生成器只能遍历一次
fib_gen = fibonacci_generator(3)
print(f"第一次遍历: {list(fib_gen)}")
print(f"第二次遍历: {list(fib_gen)}")  # 空的，因为生成器已耗尽

# ===== 3. 生成器表达式 =====

print("\n=== 生成器表达式 ===")

# 列表推导式 vs 生成器表达式
numbers = range(1, 11)

# 列表推导式 - 立即计算所有值
squares_list = [x**2 for x in numbers]
print(f"列表推导式结果: {squares_list}")
print(f"列表内存占用: {sys.getsizeof(squares_list)} bytes")

# 生成器表达式 - 惰性求值
squares_gen = (x**2 for x in numbers)
print(f"生成器表达式对象: {squares_gen}")
print(f"生成器内存占用: {sys.getsizeof(squares_gen)} bytes")

# 使用生成器
print("生成器遍历结果:")
for square in squares_gen:
    print(f"  {square}", end=" ")
print()

# ===== 4. yield语句详解 =====

print("\n=== yield语句详解 ===")

def complex_generator():
    """复杂的生成器示例"""
    print("开始执行")
    yield 1

    print("第一次yield后")
    yield 2

    print("第二次yield后")
    yield 3

    print("结束")

gen = complex_generator()
print("创建生成器后，还没有开始执行")
print(f"第一次调用next: {next(gen)}")
print(f"第二次调用next: {next(gen)}")
print(f"第三次调用next: {next(gen)}")

try:
    next(gen)
except StopIteration:
    print("生成器执行完毕")

# ===== 5. 生成器的send()方法 =====

print("\n=== 生成器的send()方法 ===")

def echo_generator():
    """可以接收数据的生成器"""
    received = None
    while True:
        received = yield received
        print(f"收到数据: {received}")

echo_gen = echo_generator()
next(echo_gen)  # 启动生成器

echo_gen.send("Hello")
echo_gen.send("World")
echo_gen.send(42)

echo_gen.close()  # 关闭生成器

# ===== 6. 生成器的实际应用 =====

print("\n=== 生成器的实际应用 ===")

# 应用1: 处理大文件
def read_large_file(file_path, chunk_size=1024):
    """逐块读取大文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                yield chunk
    except FileNotFoundError:
        yield f"文件 {file_path} 不存在"

# 模拟大文件处理
print("模拟大文件处理:")
large_file_gen = read_large_file("nonexistent_file.txt")
for chunk in large_file_gen:
    print(f"读取块: {chunk[:50]}...")

# 应用2: 无限序列
def infinite_primes():
    """生成无限素数序列"""
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

prime_gen = infinite_primes()
print("前10个素数:")
for i, prime in enumerate(prime_gen):
    if i >= 10:
        break
    print(f"  {prime}", end=" ")
print()

# 应用3: 数据管道
def data_pipeline(data):
    """数据处理管道"""

    # 阶段1: 过滤
    def filter_positive(numbers):
        for num in numbers:
            if num > 0:
                yield num

    # 阶段2: 转换
    def square(numbers):
        for num in numbers:
            yield num ** 2

    # 阶段3: 过滤偶数平方
    def filter_even_squares(numbers):
        for num in numbers:
            if num % 2 == 0:
                yield num

    # 组合管道
    positive = filter_positive(data)
    squared = square(positive)
    even_squared = filter_even_squares(squared)

    return even_squared

data = [-2, -1, 0, 1, 2, 3, 4, 5]
result = list(data_pipeline(data))
print(f"数据管道结果: {result}")

# ===== 7. itertools模块 =====

print("\n=== itertools模块 ===")

import itertools

# count - 无限计数
print("count示例:")
for i, num in enumerate(itertools.count(10, 2)):
    if i >= 5:
        break
    print(f"  {num}", end=" ")
print()

# cycle - 循环序列
print("cycle示例:")
colors = ['红', '绿', '蓝']
color_cycle = itertools.cycle(colors)
for i, color in enumerate(color_cycle):
    if i >= 6:
        break
    print(f"  {color}", end=" ")
print()

# repeat - 重复元素
print("repeat示例:")
repeated = itertools.repeat("Python", 3)
for item in repeated:
    print(f"  {item}", end=" ")
print()

# chain - 连接多个可迭代对象
print("chain示例:")
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [4, 5, 6]
chained = list(itertools.chain(list1, list2, list3))
print(f"  {chained}")

# combinations - 组合
print("combinations示例:")
items = ['A', 'B', 'C']
combos = list(itertools.combinations(items, 2))
print(f"  {combos}")

# permutations - 排列
print("permutations示例:")
perms = list(itertools.permutations(items, 2))
print(f"  {perms}")

# ===== 8. 生成器的高级模式 =====

print("\n=== 生成器的高级模式 ===")

# 子生成器和委派生成器
def sub_generator():
    """子生成器"""
    yield 1
    yield 2
    yield 3

def main_generator():
    """主生成器（委派生成器）"""
    yield from sub_generator()
    yield 4
    yield 5

main_gen = main_generator()
print("委派生成器结果:")
for value in main_gen:
    print(f"  {value}")

# 异常处理
def robust_generator():
    """带有异常处理的生成器"""
    try:
        yield 1
        yield 2
        raise ValueError("模拟错误")
        yield 3
    except GeneratorExit:
        print("生成器被关闭")
    finally:
        print("清理资源")

gen = robust_generator()
print(next(gen))
print(next(gen))
try:
    next(gen)
except ValueError as e:
    print(f"捕获异常: {e}")

# ===== 9. 协程和异步生成器 =====

print("\n=== 协程和异步生成器 ===")

# 简单的协程示例
def simple_coroutine():
    """简单协程"""
    print("协程启动")
    while True:
        value = yield
        print(f"收到值: {value}")

coroutine = simple_coroutine()
next(coroutine)  # 启动协程

coroutine.send("Hello")
coroutine.send("World")
coroutine.close()

# ===== 10. 性能对比 =====

print("\n=== 性能对比 ===")

def memory_comparison():
    """内存使用对比"""

    # 大数据集
    n = 100000

    print(f"处理 {n} 个元素:")

    # 使用列表
    start_time = time.time()
    squares_list = [x**2 for x in range(n)]
    list_time = time.time() - start_time
    list_memory = sys.getsizeof(squares_list)

    print(".4f")
    print(f"  内存占用: {list_memory} bytes")

    # 使用生成器
    start_time = time.time()
    squares_gen = (x**2 for x in range(n))
    # 只计算前1000个来模拟使用
    result = sum(next(squares_gen) for _ in range(1000))
    gen_time = time.time() - start_time
    gen_memory = sys.getsizeof(squares_gen)

    print(".4f")
    print(f"  内存占用: {gen_memory} bytes")
    print(".1f")

memory_comparison()

# ===== 练习 =====

print("\n=== 练习时间 ===")

# 练习1: 创建一个文件读取生成器
def read_file_lines(file_path):
    """逐行读取文件的生成器"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                yield line_num, line.rstrip('\n')
    except FileNotFoundError:
        yield None, f"文件 {file_path} 不存在"

# 创建一个测试文件
with open('test_file.txt', 'w', encoding='utf-8') as f:
    f.write("第一行\n")
    f.write("第二行\n")
    f.write("第三行\n")

print("文件读取生成器测试:")
for line_num, content in read_file_lines('test_file.txt'):
    print(f"  第{line_num}行: {content}")

# 测试不存在的文件
for line_num, content in read_file_lines('nonexistent.txt'):
    print(f"  {content}")

# 练习2: 实现一个简单的分页生成器
def paginate(items, page_size):
    """分页生成器"""
    page = []
    for item in items:
        page.append(item)
        if len(page) == page_size:
            yield page
            page = []
    if page:  # 剩余的项目
        yield page

# 测试分页
data = list(range(1, 23))  # 22个项目
print(f"\n分页测试 (每页5个项目):")
for page_num, page in enumerate(paginate(data, 5), 1):
    print(f"  第{page_num}页: {page}")

# 练习3: 创建一个树形结构遍历生成器
class TreeNode:
    """树节点"""
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []

def traverse_tree_dfs(node):
    """深度优先遍历生成器"""
    yield node.value
    for child in node.children:
        yield from traverse_tree_dfs(child)

def traverse_tree_bfs(root):
    """广度优先遍历生成器"""
    from collections import deque
    queue = deque([root])
    while queue:
        node = queue.popleft()
        yield node.value
        queue.extend(node.children)

# 创建树结构
root = TreeNode("A", [
    TreeNode("B", [TreeNode("D"), TreeNode("E")]),
    TreeNode("C", [TreeNode("F")])
])

print("
树遍历测试:")
print("  DFS遍历:", list(traverse_tree_dfs(root)))
print("  BFS遍历:", list(traverse_tree_bfs(root)))

# 练习4: 实现一个合并排序的生成器
def merge_sorted_generators(*generators):
    """合并多个已排序的生成器"""
    import heapq

    # 使用heapq来维护最小堆
    heap = []
    for i, gen in enumerate(generators):
        try:
            value = next(gen)
            heapq.heappush(heap, (value, i, gen))
        except StopIteration:
            pass

    while heap:
        value, gen_index, gen = heapq.heappop(heap)
        yield value

        try:
            next_value = next(gen)
            heapq.heappush(heap, (next_value, gen_index, gen))
        except StopIteration:
            pass

# 测试合并排序生成器
gen1 = iter([1, 4, 7, 10])
gen2 = iter([2, 5, 8, 11])
gen3 = iter([3, 6, 9, 12])

print("
合并排序生成器测试:")
merged = list(merge_sorted_generators(gen1, gen2, gen3))
print(f"  合并结果: {merged}")
print(f"  是否有序: {merged == sorted(merged)}")

# 练习5: 创建一个缓存生成器装饰器
def cached_generator(func):
    """缓存生成器结果的装饰器"""
    cache = {}

    def wrapper(*args, **kwargs):
        # 创建缓存键
        key = (args, tuple(sorted(kwargs.items())))

        if key not in cache:
            # 第一次调用，执行生成器并缓存结果
            cache[key] = list(func(*args, **kwargs))

        # 返回缓存的结果生成器
        return iter(cache[key])

    return wrapper

@cached_generator
def expensive_calculation(n):
    """模拟耗时的计算"""
    print(f"执行 expensive_calculation({n})")
    time.sleep(0.1)  # 模拟耗时
    return (x**2 for x in range(n))

print("
缓存生成器测试:")
print("第一次调用:")
result1 = list(expensive_calculation(5))
print(f"结果: {result1}")

print("第二次调用 (应该从缓存获取):")
result2 = list(expensive_calculation(5))
print(f"结果: {result2}")

# 清理测试文件
import os
if os.path.exists('test_file.txt'):
    os.remove('test_file.txt')

print("\n生成器和迭代器学习完成！生成器是Python最强大的特性之一，掌握它能让你高效处理大量数据和复杂的数据流。")
