# Python学习项目 - 中级内容：字典
# 学习序号：第2阶段 第2课 - 字典
# 建议学习时间：60-90分钟
# 前置知识：第2阶段 第1课 - 列表和元组
# 下一课：第2阶段 第3课 - 集合 (sets.py)
# 本模块介绍Python中的字典数据结构

# ===== 1. 字典基础 =====

print("=== 字典(Dictionary)基础 ===")

# 创建字典
empty_dict = {}
person = {
    "name": "张三",
    "age": 25,
    "city": "北京"
}

# 使用dict()构造函数
person2 = dict(name="李四", age=30, city="上海")

print(f"空字典: {empty_dict}")
print(f"人员信息字典: {person}")
print(f"使用构造函数创建: {person2}")

# 从列表创建字典
keys = ["name", "age", "city"]
values = ["王五", 28, "广州"]
person3 = dict(zip(keys, values))
print(f"从列表创建: {person3}")

# ===== 2. 访问字典元素 =====

print("\n=== 访问字典元素 ===")

person = {
    "name": "张三",
    "age": 25,
    "city": "北京",
    "hobbies": ["阅读", "编程", "旅行"]
}

# 直接访问
print(f"姓名: {person['name']}")
print(f"年龄: {person['age']}")

# 使用get()方法（更安全）
print(f"城市: {person.get('city')}")
print(f"不存在的键: {person.get('salary', '未设置')}")

# 检查键是否存在
print(f"有'name'键: {'name' in person}")
print(f"有'salary'键: {'salary' in person}")

# 获取所有键、值、键值对
print(f"所有键: {list(person.keys())}")
print(f"所有值: {list(person.values())}")
print(f"所有键值对: {list(person.items())}")

# ===== 3. 修改字典 =====

print("\n=== 修改字典 ===")

person = {"name": "张三", "age": 25}

# 添加新键值对
person["city"] = "北京"
person["job"] = "工程师"
print(f"添加键值对后: {person}")

# 修改现有值
person["age"] = 26
print(f"修改年龄后: {person}")

# update()方法
person.update({"age": 27, "salary": 10000})
print(f"使用update更新: {person}")

# 删除键值对
removed_value = person.pop("salary")
print(f"删除salary: {removed_value}, 剩余: {person}")

# 删除最后一个键值对
last_item = person.popitem()
print(f"删除最后一个: {last_item}, 剩余: {person}")

# 清空字典
temp_dict = {"a": 1, "b": 2}
temp_dict.clear()
print(f"清空字典: {temp_dict}")

# ===== 4. 字典推导式 =====

print("\n=== 字典推导式 ===")

# 基本字典推导式
squares = {x: x**2 for x in range(1, 6)}
print(f"平方字典: {squares}")

# 条件字典推导式
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(f"偶数平方字典: {even_squares}")

# 从其他字典创建
original = {"a": 1, "b": 2, "c": 3}
doubled = {k: v * 2 for k, v in original.items()}
print(f"值翻倍: {doubled}")

# 键值互换
swapped = {v: k for k, v in original.items()}
print(f"键值互换: {swapped}")

# ===== 5. 嵌套字典 =====

print("\n=== 嵌套字典 ===")

# 学生信息系统
students = {
    "stu001": {
        "name": "张三",
        "age": 20,
        "grades": {"math": 85, "english": 92, "physics": 78}
    },
    "stu002": {
        "name": "李四",
        "age": 21,
        "grades": {"math": 88, "english": 85, "physics": 90}
    }
}

print("学生信息:")
for stu_id, info in students.items():
    print(f"学号: {stu_id}")
    print(f"  姓名: {info['name']}")
    print(f"  年龄: {info['age']}")
    print(f"  成绩: {info['grades']}")
    avg_grade = sum(info['grades'].values()) / len(info['grades'])
    print(".1f")
    print()

# 访问嵌套数据
math_score = students["stu001"]["grades"]["math"]
print(f"张三的数学成绩: {math_score}")

# ===== 6. 字典的默认值 =====

print("\n=== 字典的默认值 ===")

from collections import defaultdict

# 使用defaultdict
word_count = defaultdict(int)
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

for word in words:
    word_count[word] += 1

print(f"单词统计: {dict(word_count)}")

# 自定义默认值函数
def default_list():
    return []

group_dict = defaultdict(default_list)
data = [("A", 1), ("B", 2), ("A", 3), ("C", 4), ("B", 5)]

for key, value in data:
    group_dict[key].append(value)

print(f"分组结果: {dict(group_dict)}")

# ===== 7. 字典排序 =====

print("\n=== 字典排序 ===")

scores = {"张三": 85, "李四": 92, "王五": 78, "赵六": 88}

# 按值排序（降序）
sorted_by_score = sorted(scores.items(), key=lambda x: x[1], reverse=True)
print("按分数降序:")
for name, score in sorted_by_score:
    print(f"  {name}: {score}")

# 按键排序
sorted_by_name = sorted(scores.items(), key=lambda x: x[0])
print("\n按姓名排序:")
for name, score in sorted_by_name:
    print(f"  {name}: {score}")

# ===== 8. 字典合并 =====

print("\n=== 字典合并 ===")

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

# Python 3.9+ 的合并运算符
try:
    merged = dict1 | dict2
    print(f"合并结果 (|): {merged}")
except TypeError:
    print("不支持 | 运算符")

# update()方法
dict1_copy = dict1.copy()
dict1_copy.update(dict2)
print(f"update()合并: {dict1_copy}")

# 字典推导式合并
merged_dict = {**dict1, **dict2}
print(f"解包合并: {merged_dict}")

# ===== 9. 字典应用场景 =====

print("\n=== 字典应用场景 ===")

# 场景1: 计数器
def word_frequency(text):
    """统计单词频率"""
    words = text.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

text = "Python is great and Python is easy to learn"
freq_result = word_frequency(text)
print(f"单词频率: {freq_result}")

# 场景2: 缓存/记忆化
def fibonacci_memo(n, memo={}):
    """使用字典进行记忆化的斐波那契数列"""
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

print(f"斐波那契数列第10项: {fibonacci_memo(10)}")

# 场景3: 配置管理
config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "mydb"
    },
    "api": {
        "base_url": "https://api.example.com",
        "timeout": 30
    }
}

print(f"数据库配置: {config['database']}")
print(f"API超时时间: {config['api']['timeout']}")

# ===== 10. 字典性能特点 =====

print("\n=== 字典性能特点 ===")

import time

# 测试查找性能
n = 100000
test_dict = {i: i*2 for i in range(n)}
test_list = list(range(n))

# 字典查找
start = time.time()
for _ in range(1000):
    _ = test_dict.get(n//2, None)
dict_time = time.time() - start

# 列表查找
start = time.time()
for _ in range(1000):
    _ = n//2 in test_list
list_time = time.time() - start

print(".4f")
print(".4f")
print(".1f")

# ===== 练习 =====

print("\n=== 练习时间 ===")

# 练习1: 学生成绩管理系统
def student_grade_system():
    """学生成绩管理系统"""
    students = {}

    # 添加学生信息
    students["stu001"] = {
        "name": "张三",
        "grades": {"math": 85, "english": 92, "physics": 78}
    }
    students["stu002"] = {
        "name": "李四",
        "grades": {"math": 88, "english": 85, "physics": 90}
    }
    students["stu003"] = {
        "name": "王五",
        "grades": {"math": 76, "english": 88, "physics": 82}
    }

    print("学生成绩单:")
    for stu_id, info in students.items():
        print(f"\n学号: {stu_id}, 姓名: {info['name']}")
        total = sum(info['grades'].values())
        avg = total / len(info['grades'])
        print(f"各科成绩: {info['grades']}")
        print(".1f")

# 练习2: 购物车系统
def shopping_cart():
    """简单的购物车系统"""
    cart = {}

    # 添加商品
    def add_item(name, price, quantity=1):
        if name in cart:
            cart[name]["quantity"] += quantity
        else:
            cart[name] = {"price": price, "quantity": quantity}

    # 计算总价
    def get_total():
        return sum(item["price"] * item["quantity"] for item in cart.values())

    # 添加一些商品
    add_item("苹果", 5.0, 3)
    add_item("香蕉", 3.0, 2)
    add_item("苹果", 5.0, 1)  # 再次添加苹果

    print("\n购物车内容:")
    for name, info in cart.items():
        subtotal = info["price"] * info["quantity"]
        print("2d")
    print(".1f")

# 练习3: 词频统计器
def word_counter():
    """高级词频统计器"""
    text = """
    Python is a programming language that is easy to learn and powerful.
    Python is widely used in data science, web development, and automation.
    Learning Python opens up many opportunities in the tech industry.
    """

    # 清理文本并统计
    import re
    words = re.findall(r'\b\w+\b', text.lower())

    # 使用字典统计
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1

    # 按频率排序
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    print("\n词频统计 (前10个):")
    for word, count in sorted_freq[:10]:
        print(f"  {word}: {count}")

# 练习4: 缓存装饰器模拟
def memoize_example():
    """记忆化缓存示例"""
    cache = {}

    def expensive_function(n):
        if n in cache:
            print(f"从缓存获取 {n}")
            return cache[n]

        print(f"计算 {n}")
        # 模拟耗时计算
        result = n * n + n
        cache[n] = result
        return result

    print("\n缓存演示:")
    print(f"结果1: {expensive_function(5)}")
    print(f"结果2: {expensive_function(5)}")  # 应该从缓存获取
    print(f"结果3: {expensive_function(3)}")
    print(f"缓存内容: {cache}")

# 运行练习
print("练习1: 学生成绩管理系统")
student_grade_system()

print("\n练习2: 购物车系统")
shopping_cart()

print("\n练习3: 词频统计器")
word_counter()

print("\n练习4: 缓存示例")
memoize_example()
