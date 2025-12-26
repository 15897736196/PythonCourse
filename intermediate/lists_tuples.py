# Python学习项目 - 中级内容：列表和元组
# 学习序号：第2阶段 第1课 - 列表和元组
# 建议学习时间：60-90分钟
# 前置知识：第1阶段 - 基础语法
# 下一课：第2阶段 第2课 - 字典 (dictionaries.py)
# 本模块介绍Python中的列表和元组数据结构

# ===== 1. 列表(List)基础 =====

print("=== 列表(List)基础 ===")

# 创建列表
empty_list = []
numbers = [1, 2, 3, 4, 5]
fruits = ["苹果", "香蕉", "橙子"]
mixed = [1, "hello", 3.14, True]

print(f"空列表: {empty_list}")
print(f"数字列表: {numbers}")
print(f"水果列表: {fruits}")
print(f"混合列表: {mixed}")

# 列表推导式
squares = [x**2 for x in range(1, 6)]
print(f"平方数列表: {squares}")

even_numbers = [x for x in range(10) if x % 2 == 0]
print(f"偶数列表: {even_numbers}")

# ===== 2. 列表操作 =====

print("\n=== 列表操作 ===")

# 访问元素
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
print(f"第一个水果: {fruits[0]}")
print(f"最后一个水果: {fruits[-1]}")
print(f"前两个水果: {fruits[:2]}")
print(f"从第二个到最后: {fruits[1:]}")
print(f"每隔一个取一个: {fruits[::2]}")

# 修改元素
fruits[1] = "梨"
print(f"修改后的水果列表: {fruits}")

# 添加元素
fruits.append("西瓜")
print(f"追加元素后: {fruits}")

fruits.insert(1, "草莓")
print(f"在索引1处插入: {fruits}")

# 扩展列表
more_fruits = ["菠萝", "芒果"]
fruits.extend(more_fruits)
print(f"扩展列表后: {fruits}")

# 删除元素
removed = fruits.pop()  # 删除最后一个
print(f"弹出元素: {removed}, 剩余: {fruits}")

fruits.remove("橙子")  # 删除指定元素
print(f"删除'橙子'后: {fruits}")

del fruits[0]  # 删除指定索引的元素
print(f"删除第一个元素后: {fruits}")

# ===== 3. 列表方法详解 =====

print("\n=== 列表方法详解 ===")

numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# 排序
numbers_copy = numbers.copy()
numbers_copy.sort()
print(f"原列表: {numbers}")
print(f"排序后: {numbers_copy}")

numbers_copy.sort(reverse=True)
print(f"逆序排序: {numbers_copy}")

# 反转
numbers_copy = numbers.copy()
numbers_copy.reverse()
print(f"反转后: {numbers_copy}")

# 查找
print(f"元素1的索引: {numbers.index(1)}")
print(f"元素1出现的次数: {numbers.count(1)}")

# 清空列表
temp_list = [1, 2, 3]
temp_list.clear()
print(f"清空后的列表: {temp_list}")

# ===== 4. 列表推导式进阶 =====

print("\n=== 列表推导式进阶 ===")

# 嵌套列表推导式
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print("3x3乘法表:")
for row in matrix:
    print(row)

# 条件列表推导式
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [x**2 for x in numbers if x % 2 == 0]
odd_cubes = [x**3 for x in numbers if x % 2 != 0]

print(f"偶数的平方: {even_squares}")
print(f"奇数的立方: {odd_cubes}")

# 多重条件
filtered = [x for x in range(20) if x % 2 == 0 and x % 3 == 0]
print(f"能被2和3整除的数: {filtered}")

# ===== 5. 元组(Tuple)基础 =====

print("\n=== 元组(Tuple)基础 ===")

# 创建元组
empty_tuple = ()
single_element = (42,)  # 注意逗号
coordinates = (10, 20)
colors = ("红", "绿", "蓝")
mixed_tuple = (1, "hello", 3.14)

print(f"空元组: {empty_tuple}")
print(f"单元素元组: {single_element}")
print(f"坐标: {coordinates}")
print(f"颜色: {colors}")
print(f"混合元组: {mixed_tuple}")

# 访问元组元素（与列表相同）
print(f"第一个颜色: {colors[0]}")
print(f"最后一个颜色: {colors[-1]}")
print(f"前两个颜色: {colors[:2]}")

# ===== 6. 元组的不可变性 =====

print("\n=== 元组的不可变性 ===")

# 元组一旦创建就不能修改
point = (3, 4)
print(f"原点: {point}")

# 尝试修改会报错
try:
    # point[0] = 5  # 这会报错
    pass
except TypeError as e:
    print(f"错误: {e}")

# 但是可以重新赋值
point = (5, 6)
print(f"新点: {point}")

# ===== 7. 元组解包 =====

print("\n=== 元组解包 ===")

# 基本解包
x, y = (10, 20)
print(f"x = {x}, y = {y}")

# 交换变量（利用元组解包）
a, b = 5, 10
print(f"交换前: a = {a}, b = {b}")
a, b = b, a
print(f"交换后: a = {a}, b = {b}")

# 解包多个值
first, *middle, last = (1, 2, 3, 4, 5)
print(f"第一个: {first}, 中间: {middle}, 最后一个: {last}")

# 忽略不需要的值
name, _, age, _ = ("张三", "男", 25, "北京")
print(f"姓名: {name}, 年龄: {age}")

# ===== 8. 列表与元组的比较 =====

print("\n=== 列表与元组的比较 ===")

import sys

# 内存占用比较
list_data = [1, 2, 3, 4, 5]
tuple_data = (1, 2, 3, 4, 5)

print(f"列表大小: {sys.getsizeof(list_data)} bytes")
print(f"元组大小: {sys.getsizeof(tuple_data)} bytes")

# 性能比较
import time

# 创建大量数据进行测试
n = 1000000

# 列表创建时间
start = time.time()
list_large = list(range(n))
list_time = time.time() - start

# 元组创建时间
start = time.time()
tuple_large = tuple(range(n))
tuple_time = time.time() - start

print(".4f")
print(".4f")

# ===== 9. 列表和元组作为函数返回值 =====

print("\n=== 列表和元组作为返回值 ===")

def get_user_info():
    """返回用户信息（使用元组）"""
    return ("张三", 25, "北京")

def get_scores():
    """返回分数列表"""
    return [85, 92, 78, 96]

user_info = get_user_info()
print(f"用户信息: 姓名={user_info[0]}, 年龄={user_info[1]}, 城市={user_info[2]}")

scores = get_scores()
print(f"分数: {scores}, 平均分: {sum(scores)/len(scores):.1f}")

# ===== 10. 嵌套数据结构 =====

print("\n=== 嵌套数据结构 ===")

# 列表嵌套
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("矩阵:")
for row in matrix:
    print(row)

# 访问嵌套元素
print(f"第2行第3列: {matrix[1][2]}")

# 元组嵌套
student_records = (
    ("张三", 25, ("数学", "英语")),
    ("李四", 23, ("物理", "化学")),
    ("王五", 24, ("历史", "地理"))
)

print("\n学生记录:")
for name, age, subjects in student_records:
    print(f"{name}({age}岁): {', '.join(subjects)}")

# ===== 练习 =====

print("\n=== 练习时间 ===")

# 练习1: 列表操作
def list_operations_demo():
    """演示列表操作"""
    # 创建一个包含1-10的列表
    numbers = list(range(1, 11))
    print(f"原始列表: {numbers}")

    # 添加元素
    numbers.append(11)
    numbers.insert(0, 0)
    print(f"添加元素后: {numbers}")

    # 删除元素
    numbers.remove(5)
    popped = numbers.pop()
    print(f"删除元素后: {numbers}, 弹出的元素: {popped}")

    # 排序和反转
    numbers.sort(reverse=True)
    print(f"逆序排序: {numbers}")

    # 查找
    print(f"数字3的索引: {numbers.index(3)}")
    print(f"数字2出现的次数: {numbers.count(2)}")

# 练习2: 元组解包应用
def tuple_unpacking_demo():
    """元组解包演示"""
    # 坐标点
    points = [(1, 2), (3, 4), (5, 6)]

    print("坐标点距离原点:")
    for x, y in points:
        distance = (x**2 + y**2)**0.5
        print(".1f")

    # 学生信息
    students = [
        ("Alice", 25, "CS"),
        ("Bob", 23, "Math"),
        ("Charlie", 24, "Physics")
    ]

    print("\n学生信息:")
    for name, age, major in students:
        print(f"{name} ({age}岁) - {major}")

# 练习3: 列表推导式练习
def comprehension_practice():
    """列表推导式练习"""
    # 生成1-100的偶数平方
    even_squares = [x**2 for x in range(1, 101) if x % 2 == 0]
    print(f"1-100偶数的平方: {even_squares[:10]}...")  # 只显示前10个

    # 字符串处理
    words = ["apple", "Banana", "CHERRY", "date"]
    title_case = [word.title() for word in words]
    print(f"标题格式: {title_case}")

    # 嵌套推导式 - 坐标系
    coordinates = [(x, y) for x in range(3) for y in range(3)]
    print(f"坐标系: {coordinates}")

# 练习4: 数据处理
def data_processing_demo():
    """数据处理演示"""
    # 学生成绩数据
    grades = [
        {"name": "Alice", "scores": [85, 92, 78]},
        {"name": "Bob", "scores": [88, 76, 95]},
        {"name": "Charlie", "scores": [90, 85, 88]}
    ]

    print("学生平均分:")
    for student in grades:
        avg_score = sum(student["scores"]) / len(student["scores"])
        print(".1f")

    # 找出最高平均分的学生
    averages = [(student["name"], sum(student["scores"])/len(student["scores"]))
                for student in grades]
    best_student = max(averages, key=lambda x: x[1])
    print(f"\n最高平均分: {best_student[0]} ({best_student[1]:.1f})")

# 运行练习
print("练习1: 列表操作")
list_operations_demo()

print("\n练习2: 元组解包")
tuple_unpacking_demo()

print("\n练习3: 列表推导式")
comprehension_practice()

print("\n练习4: 数据处理")
data_processing_demo()
