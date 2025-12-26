# Python学习项目 - 基础语法：控制流
# 学习序号：第1阶段 第3课 - 控制流
# 建议学习时间：60-90分钟
# 前置知识：第1阶段 第1-2课 - 变量、数据类型和运算符
# 下一课：第1阶段 第4课 - 输入输出 (input_output.py)
# 本模块介绍Python中的条件语句和循环结构

# ===== 1. 条件语句 (if-elif-else) =====

print("=== 条件语句示例 ===")

# 基本if语句
age = 18
if age >= 18:
    print("你已成年，可以观看此内容")

# if-else语句
temperature = 25
if temperature > 30:
    print("今天很热，记得多喝水")
else:
    print("天气凉爽，适合外出")

# if-elif-else语句
score = 85
if score >= 90:
    grade = "优秀"
elif score >= 80:
    grade = "良好"
elif score >= 70:
    grade = "中等"
elif score >= 60:
    grade = "及格"
else:
    grade = "不及格"

print(f"分数{score}对应的等级是: {grade}")

# ===== 2. 嵌套条件语句 =====

print("\n=== 嵌套条件语句 ===")

has_ticket = True
age = 16
with_parent = True

if has_ticket:
    if age >= 18:
        print("欢迎成人观众入场")
    elif age >= 12:
        print("欢迎青少年观众入场")
    else:
        if with_parent:
            print("儿童需家长陪同入场")
        else:
            print("儿童必须家长陪同才能入场")
else:
    print("请先购买门票")

# ===== 3. 条件表达式 (三元运算符) =====

print("\n=== 条件表达式 ===")

# 传统写法
x = 5
if x > 0:
    result = "正数"
else:
    result = "非正数"
print(f"x = {x}, 结果: {result}")

# 条件表达式写法
result = "正数" if x > 0 else "非正数"
print(f"使用条件表达式: x = {x}, 结果: {result}")

# 更复杂的条件表达式
y = -3
result = "正数" if y > 0 else "零" if y == 0 else "负数"
print(f"y = {y}, 结果: {result}")

# ===== 4. for循环 =====

print("\n=== for循环 ===")

# 遍历列表
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
print("水果列表:")
for fruit in fruits:
    print(f"  - {fruit}")

# 使用range()函数
print("\n0到4的数字:")
for i in range(5):
    print(f"  - {i}")

print("\n1到10的偶数:")
for i in range(2, 11, 2):  # 从2开始，到11结束（不包含），步长为2
    print(f"  - {i}")

# 遍历字符串
word = "Python"
print(f"\n单词 '{word}' 的每个字母:")
for letter in word:
    print(f"  - {letter}")

# ===== 5. while循环 =====

print("\n=== while循环 ===")

# 基本while循环
count = 1
print("倒计时:")
while count <= 5:
    print(f"  - {count}")
    count += 1

# 使用break跳出循环
print("\n寻找第一个大于10的数:")
numbers = [3, 7, 12, 5, 8, 15, 2]
for num in numbers:
    if num > 10:
        print(f"找到: {num}")
        break
    print(f"检查: {num}")

# 使用continue跳过本次循环
print("\n跳过偶数:")
for num in range(1, 11):
    if num % 2 == 0:
        continue
    print(f"  - {num}")

# ===== 6. 循环中的else语句 =====

print("\n=== 循环中的else ===")

# for循环的else - 循环正常结束时执行
print("寻找质数:")
for num in range(2, 10):
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} = {i} * {num//i}")
            break
    else:
        print(f"{num} 是质数")

# while循环的else
count = 0
while count < 3:
    print(f"计数: {count}")
    count += 1
else:
    print("循环正常结束")

# ===== 7. 循环控制语句详解 =====

print("\n=== 循环控制详解 ===")

# break示例 - 找到目标后停止
target = 7
found = False
attempts = 0

while attempts < 10:
    attempts += 1
    if attempts == target:
        found = True
        print(f"在第{attempts}次尝试中找到目标!")
        break
    print(f"第{attempts}次尝试...")
else:
    print("没有找到目标")

# continue示例 - 跳过不符合条件的项
print("\n处理成绩 (跳过无效成绩):")
scores = [85, -5, 92, 78, 101, 88, 76]
valid_scores = []

for score in scores:
    if score < 0 or score > 100:
        print(f"跳过无效成绩: {score}")
        continue
    valid_scores.append(score)
    print(f"添加有效成绩: {score}")

print(f"有效成绩: {valid_scores}")

# ===== 8. 无限循环和循环控制 =====

print("\n=== 无限循环控制 ===")

# 模拟用户输入验证
attempts = 0
max_attempts = 3

while True:
    # 模拟用户输入
    user_input = input("请输入一个1-10之间的数字 (输入'quit'退出): ")

    if user_input.lower() == 'quit':
        print("退出程序")
        break

    try:
        number = int(user_input)
        if 1 <= number <= 10:
            print(f"输入有效: {number}")
            break
        else:
            print("数字必须在1-10之间")
    except ValueError:
        print("请输入有效的数字")

    attempts += 1
    if attempts >= max_attempts:
        print("尝试次数过多，程序退出")
        break

# ===== 9. 嵌套循环 =====

print("\n=== 嵌套循环 ===")

# 九九乘法表
print("九九乘法表:")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}×{i}={i*j:2}", end=" ")
    print()  # 换行

# ===== 练习 =====

print("\n=== 练习时间 ===")

# 练习1: 判断成绩等级
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

test_scores = [95, 87, 72, 68, 45]
for score in test_scores:
    grade = get_grade(score)
    print(f"分数{score}: 等级{grade}")

# 练习2: 计算1-100的和
total = 0
for i in range(1, 101):
    total += i
print(f"\n1-100的和: {total}")

# 练习3: 猜数字游戏
import random
target_number = random.randint(1, 100)
guesses = 0

print("\n猜数字游戏 (1-100):")
while True:
    try:
        guess = int(input("请输入你的猜测: "))
        guesses += 1

        if guess == target_number:
            print(f"恭喜! 你猜对了，答案是{target_number}")
            print(f"你总共猜了{guesses}次")
            break
        elif guess < target_number:
            print("太小了!")
        else:
            print("太大了!")
    except ValueError:
        print("请输入有效的数字!")

# 练习4: 找出列表中的最大值
numbers = [23, 45, 12, 67, 89, 34, 56, 78, 90, 11]
max_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num

print(f"\n列表 {numbers} 中的最大值是: {max_num}")
