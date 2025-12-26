# Python学习项目 - 基础语法：变量和数据类型
# 学习序号：第1阶段 第1课 - 变量和数据类型
# 建议学习时间：30-45分钟
# 前置知识：无
# 下一课：第1阶段 第2课 - 运算符 (operators.py)
# 本模块介绍Python中最基本的数据类型和变量使用

"""
Python变量命名规则：
1. 变量名只能包含字母、数字、下划线
2. 变量名不能以数字开头
3. 不能使用Python关键字作为变量名
4. 建议使用小写字母和下划线组合（snake_case）
5. 变量名要有意义，便于理解
"""

# ===== 1. 基本数据类型 =====

# 整数 (int)
age = 25
print(f"年龄: {age}, 类型: {type(age)}")

# 浮点数 (float)
height = 175.5
weight = 70.0
print(f"身高: {height}cm, 体重: {weight}kg")
print(f"类型: height是{type(height)}, weight是{type(weight)}")

# 字符串 (str)
name = "张三"
city = '北京'
message = """这是一个多行字符串
可以包含换行符
非常方便"""
print(f"姓名: {name}, 城市: {city}")
print(f"多行消息: {message}")

# 布尔值 (bool)
is_student = True
has_license = False
print(f"是否学生: {is_student}, 有驾照: {has_license}")

# ===== 2. 类型转换 =====

# 数字转字符串
score = 95
score_str = str(score)
print(f"分数字符串: {score_str}, 类型: {type(score_str)}")

# 字符串转数字
price_str = "29.99"
price = float(price_str)
quantity = int("10")
print(f"价格: {price}, 数量: {quantity}")

# 布尔值转换
print(f"空字符串转布尔: {bool('')}")
print(f"非空字符串转布尔: {bool('hello')}")
print(f"0转布尔: {bool(0)}")
print(f"非0数字转布尔: {bool(5)}")

# ===== 3. 变量赋值和操作 =====

# 同时赋值多个变量
x, y, z = 1, 2, 3
print(f"x={x}, y={y}, z={z}")

# 交换变量值（Python特色）
a, b = 10, 20
print(f"交换前: a={a}, b={b}")
a, b = b, a
print(f"交换后: a={a}, b={b}")

# ===== 4. None类型 =====
result = None
print(f"None值: {result}, 类型: {type(result)}")

# ===== 5. 动态类型特性 =====
# Python是动态类型语言，变量类型可以改变
variable = "我是字符串"
print(f"variable: {variable}, 类型: {type(variable)}")

variable = 42
print(f"variable: {variable}, 类型: {type(variable)}")

variable = [1, 2, 3]
print(f"variable: {variable}, 类型: {type(variable)}")

# ===== 6. 常量约定 =====
# Python没有真正的常量，但约定使用大写表示常量
PI = 3.14159
MAX_CONNECTIONS = 100
CONFIG_FILE = "config.ini"

print(f"圆周率: {PI}, 最大连接数: {MAX_CONNECTIONS}")

# ===== 练习 =====
print("\n=== 练习时间 ===")

# 练习1: 创建不同类型的变量
your_name = "你的名字"
your_age = 0  # 填入你的年龄
your_height = 0.0  # 填入你的身高（米）

print(f"姓名: {your_name}, 年龄: {your_age}, 身高: {your_height}米")

# 练习2: 类型转换
birth_year = "1990"
current_year = 2024
age_calculated = current_year - int(birth_year)
print(f"计算出的年龄: {age_calculated}")

# 练习3: 布尔值判断
is_adult = age_calculated >= 18
print(f"是否成年: {is_adult}")
