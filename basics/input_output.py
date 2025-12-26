# Python学习项目 - 基础语法：输入输出
# 学习序号：第1阶段 第4课 - 输入输出
# 建议学习时间：45-60分钟
# 前置知识：第1阶段 第1-3课 - 基础语法
# 下一课：第2阶段 第1课 - 列表和元组 (intermediate/lists_tuples.py)
# 本模块介绍Python中的输入输出操作

# ===== 1. print()函数的基本使用 =====

print("=== print()函数基本使用 ===")

# 基本输出
print("Hello, World!")

# 输出多个值（用空格分隔）
print("Python", "is", "awesome!")

# 指定分隔符
print("Python", "is", "awesome!", sep="-")

# 指定结束符（默认是换行）
print("这行不会换行", end="")
print("，这是续接的内容")

# ===== 2. 格式化输出 =====

print("\n=== 格式化输出 ===")

name = "小明"
age = 25
height = 175.5

# f-string (Python 3.6+推荐)
print(f"姓名: {name}, 年龄: {age}岁, 身高: {height}cm")

# format()方法
print("姓名: {}, 年龄: {}岁, 身高: {}cm".format(name, age, height))

# %格式化（旧式）
print("姓名: %s, 年龄: %d岁, 身高: %.1fcm" % (name, age, height))

# ===== 3. 字符串格式化进阶 =====

print("\n=== 字符串格式化进阶 ===")

# 对齐和宽度控制
products = [
    ("苹果", 5.50),
    ("香蕉", 3.20),
    ("橙子", 4.80)
]

print("商品清单:")
print("-" * 20)
for product, price in products:
    print("<10")  # 左对齐，宽度10
    print(">8.2f")  # 右对齐，宽度8，小数点后2位

# 数字格式化
number = 1234567.89123
print(f"\n原始数字: {number}")
print(f"千分位分隔: {number:,}")
print(f"科学计数: {number:.2e}")
print(f"百分比: {number:.2%}")

# ===== 4. input()函数 =====

print("\n=== input()函数 ===")

# 基本输入
# name = input("请输入你的姓名: ")
# print(f"你好，{name}!")

# 输入数字并转换类型
# age_str = input("请输入你的年龄: ")
# age = int(age_str)
# print(f"明年你将{age + 1}岁")

# ===== 5. 输入验证和错误处理 =====

print("\n=== 输入验证 ===")

def get_valid_number(prompt, min_val=None, max_val=None):
    """获取有效的数字输入"""
    while True:
        try:
            value = float(input(prompt))
            if min_val is not None and value < min_val:
                print(f"输入值不能小于{min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"输入值不能大于{max_val}")
                continue
            return value
        except ValueError:
            print("请输入有效的数字!")

# 演示输入验证（注释掉以避免阻塞）
# score = get_valid_number("请输入成绩 (0-100): ", 0, 100)
# print(f"输入的成绩是: {score}")

# ===== 6. 文件输入输出基础 =====

print("\n=== 文件输入输出基础 ===")

# 写入文件
print("写入文件示例:")
with open("example.txt", "w", encoding="utf-8") as file:
    file.write("这是第一行\n")
    file.write("这是第二行\n")
    file.write("这是第三行\n")

print("文件写入完成")

# 读取文件
print("\n读取文件内容:")
try:
    with open("example.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print("文件全部内容:")
        print(content)
except FileNotFoundError:
    print("文件不存在")

# 逐行读取
print("\n逐行读取:")
try:
    with open("example.txt", "r", encoding="utf-8") as file:
        for line_num, line in enumerate(file, 1):
            print("2")
except FileNotFoundError:
    print("文件不存在")

# ===== 7. 字符串输入输出进阶 =====

print("\n=== 字符串IO ===")

import io

# StringIO - 在内存中进行字符串IO操作
output = io.StringIO()
output.write("Hello, ")
output.write("World!")
content = output.getvalue()
print(f"StringIO内容: {content}")

# 关闭StringIO
output.close()

# ===== 8. 格式化表格输出 =====

print("\n=== 表格输出 ===")

# 创建简单的表格
data = [
    ["姓名", "年龄", "城市"],
    ["张三", "25", "北京"],
    ["李四", "30", "上海"],
    ["王五", "28", "广州"]
]

# 计算每列的最大宽度
col_widths = []
for col in range(len(data[0])):
    max_width = max(len(row[col]) for row in data)
    col_widths.append(max_width)

# 输出表格
print("+" + "+".join("-" * (width + 2) for width in col_widths) + "+")

for i, row in enumerate(data):
    print("|" + "|".join(f" {cell:<{col_widths[j]}} " for j, cell in enumerate(row)) + "|")
    if i == 0:  # 在标题行后添加分隔线
        print("+" + "+".join("-" * (width + 2) for width in col_widths) + "+")

print("+" + "+".join("-" * (width + 2) for width in col_widths) + "+")

# ===== 9. 进度条模拟 =====

print("\n=== 进度条模拟 ===")

import time

def show_progress(current, total, width=50):
    """显示进度条"""
    percentage = current / total
    filled = int(width * percentage)
    bar = "█" * filled + "░" * (width - filled)
    print("2d", end="", flush=True)

# 模拟进度
total_steps = 20
for step in range(total_steps + 1):
    show_progress(step, total_steps)
    time.sleep(0.1)  # 模拟工作时间

print("\n完成!")

# ===== 练习 =====

print("\n=== 练习时间 ===")

# 练习1: 简单的问答程序
def quiz_game():
    questions = [
        ("Python的创造者是谁?", "Guido van Rossum"),
        ("Python的吉祥物是什么?", "蛇"),
        ("Python发布的第一年是?", "1991")
    ]

    score = 0
    for question, answer in questions:
        user_answer = input(question + " ")
        if user_answer.lower() == answer.lower():
            print("✓ 正确!")
            score += 1
        else:
            print(f"✗ 错误。正确答案是: {answer}")

    print(f"\n你的得分: {score}/{len(questions)}")

# 练习2: 格式化输出个人信息
def format_person_info():
    people = [
        {"name": "Alice", "age": 25, "city": "New York", "salary": 50000},
        {"name": "Bob", "age": 30, "city": "London", "salary": 60000},
        {"name": "Charlie", "age": 35, "city": "Tokyo", "salary": 70000}
    ]

    print("个人信息表:")
    print("-" * 50)
    print("5")
    print("-" * 50)

    for person in people:
        print("<8")

# 练习3: 文件操作 - 保存和加载设置
def save_settings(filename="settings.txt"):
    """保存设置到文件"""
    settings = {
        "theme": "dark",
        "language": "zh-CN",
        "font_size": "14",
        "auto_save": "true"
    }

    with open(filename, "w", encoding="utf-8") as f:
        for key, value in settings.items():
            f.write(f"{key}={value}\n")
    print(f"设置已保存到 {filename}")

def load_settings(filename="settings.txt"):
    """从文件加载设置"""
    settings = {}
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                if "=" in line:
                    key, value = line.strip().split("=", 1)
                    settings[key] = value
        print(f"从 {filename} 加载的设置: {settings}")
        return settings
    except FileNotFoundError:
        print(f"设置文件 {filename} 不存在")
        return {}

# 运行练习
print("练习1: 问答游戏")
# quiz_game()  # 注释掉以避免阻塞

print("\n练习2: 格式化个人信息")
format_person_info()

print("\n练习3: 设置文件操作")
save_settings()
load_settings()

# ===== 清理示例文件 =====
import os
if os.path.exists("example.txt"):
    os.remove("example.txt")
    print("\n清理了示例文件")

if os.path.exists("settings.txt"):
    os.remove("settings.txt")
    print("清理了设置文件")
