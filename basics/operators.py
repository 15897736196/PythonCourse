# Python学习项目 - 基础语法：运算符
# 学习序号：第1阶段 第2课 - 运算符
# 建议学习时间：45-60分钟
# 前置知识：第1阶段 第1课 - 变量和数据类型
# 下一课：第1阶段 第3课 - 控制流 (control_flow.py)
# 本模块介绍Python中的各种运算符及其使用

# ===== 1. 算术运算符 =====

# 基本算术运算
a = 10
b = 3

print("=== 算术运算符 ===")
print(f"a = {a}, b = {b}")
print(f"加法: a + b = {a + b}")
print(f"减法: a - b = {a - b}")
print(f"乘法: a * b = {a * b}")
print(f"除法: a / b = {a / b}")
print(f"整除: a // b = {a // b}")
print(f"取余: a % b = {a % b}")
print(f"幂运算: a ** b = {a ** b}")

# 浮点数运算
x = 7.5
y = 2.0
print(f"\n浮点数运算: x = {x}, y = {y}")
print(f"x / y = {x / y}")
print(f"x // y = {x // y}")

# ===== 2. 比较运算符 =====

print("\n=== 比较运算符 ===")
print(f"a == b: {a == b}")  # 等于
print(f"a != b: {a != b}")  # 不等于
print(f"a > b: {a > b}")    # 大于
print(f"a < b: {a < b}")    # 小于
print(f"a >= b: {a >= b}")  # 大于等于
print(f"a <= b: {a <= b}")  # 小于等于

# 字符串比较
str1 = "apple"
str2 = "banana"
print(f"\n字符串比较:")
print(f"'{str1}' < '{str2}': {str1 < str2}")  # 按字典序比较

# ===== 3. 逻辑运算符 =====

print("\n=== 逻辑运算符 ===")
p = True
q = False

print(f"p = {p}, q = {q}")
print(f"p and q: {p and q}")  # 逻辑与
print(f"p or q: {p or q}")    # 逻辑或
print(f"not p: {not p}")      # 逻辑非

# 逻辑运算符的短路特性
def check_first():
    print("检查第一个条件")
    return True

def check_second():
    print("检查第二个条件")
    return False

print("\n短路特性演示:")
# and运算：第一个为False时，第二个不执行
result = check_second() and check_first()
print(f"结果: {result}")

# or运算：第一个为True时，第二个不执行
result = check_first() or check_second()
print(f"结果: {result}")

# ===== 4. 赋值运算符 =====

print("\n=== 赋值运算符 ===")
x = 5
print(f"初始值: x = {x}")

x += 3  # x = x + 3
print(f"x += 3: {x}")

x -= 2  # x = x - 2
print(f"x -= 2: {x}")

x *= 4  # x = x * 4
print(f"x *= 4: {x}")

x /= 2  # x = x / 2
print(f"x /= 2: {x}")

x //= 2  # x = x // 2
print(f"x //= 2: {x}")

x %= 3  # x = x % 3
print(f"x %= 3: {x}")

x **= 2  # x = x ** 2
print(f"x **= 2: {x}")

# ===== 5. 位运算符 =====

print("\n=== 位运算符 ===")
m = 10  # 二进制: 1010
n = 6   # 二进制: 0110

print(f"m = {m} (二进制: {bin(m)}), n = {n} (二进制: {bin(n)})")
print(f"m & n (按位与): {m & n} (二进制: {bin(m & n)})")
print(f"m | n (按位或): {m | n} (二进制: {bin(m | n)})")
print(f"m ^ n (按位异或): {m ^ n} (二进制: {bin(m ^ n)})")
print(f"~m (按位取反): {~m}")
print(f"m << 1 (左移): {m << 1} (二进制: {bin(m << 1)})")
print(f"m >> 1 (右移): {m >> 1} (二进制: {bin(m >> 1)})")

# ===== 6. 成员运算符 =====

print("\n=== 成员运算符 ===")
fruits = ["apple", "banana", "orange"]
print(f"fruits = {fruits}")
print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'grape' in fruits: {'grape' in fruits}")
print(f"'apple' not in fruits: {'apple' not in fruits}")

# ===== 7. 身份运算符 =====

print("\n=== 身份运算符 ===")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"list1 = {list1}")
print(f"list2 = {list2}")
print(f"list3 = list1")

print(f"list1 is list2: {list1 is list2}")  # False，不同对象
print(f"list1 is list3: {list1 is list3}")  # True，同一个对象
print(f"list1 == list2: {list1 == list2}")  # True，值相等

# ===== 8. 运算符优先级 =====

print("\n=== 运算符优先级示例 ===")
result = 2 + 3 * 4 ** 2 / 2
print(f"2 + 3 * 4 ** 2 / 2 = {result}")

# 使用括号改变优先级
result2 = (2 + 3) * 4 ** (2 / 2)
print(f"(2 + 3) * 4 ** (2 / 2) = {result2}")

# ===== 练习 =====

print("\n=== 练习时间 ===")

# 练习1: 计算BMI
weight = 70  # kg
height = 1.75  # m
bmi = weight / (height ** 2)
print(f"BMI计算: 体重{weight}kg, 身高{height}m, BMI = {bmi:.2f}")

# 练习2: 判断闰年条件
year = 2024
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(f"{year}年是否为闰年: {is_leap}")

# 练习3: 权限检查
age = 25
has_id = True
is_member = False

can_enter = age >= 18 and has_id and (is_member or age < 65)
print(f"年龄{age}, 有身份证{has_id}, 是会员{is_member}")
print(f"是否可以进入: {can_enter}")

# 练习4: 位运算应用 - 检查奇偶数
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"检查奇偶数:")
for num in numbers:
    is_even = (num & 1) == 0
    print(f"{num} 是偶数: {is_even}")
