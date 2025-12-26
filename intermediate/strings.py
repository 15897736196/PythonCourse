# Python学习项目 - 中级内容：字符串操作
# 学习序号：第2阶段 第4课 - 字符串操作
# 建议学习时间：60-90分钟
# 前置知识：第2阶段 第1-3课 - 数据结构基础
# 下一课：第3阶段 第1课 - 函数基础 (functions_basics.py)
# 本模块介绍Python中的字符串操作和处理

# ===== 1. 字符串基础回顾 =====

print("=== 字符串基础回顾 ===")

# 字符串创建
single_quote = 'Hello'
double_quote = "World"
triple_quote = """This is a
multi-line string"""

print(f"单引号: {single_quote}")
print(f"双引号: {double_quote}")
print(f"三引号: {triple_quote}")

# 字符串是不可变的
text = "Hello"
print(f"原字符串: {text}, id: {id(text)}")

text = text + " World"  # 创建新字符串
print(f"修改后: {text}, id: {id(text)}")

# ===== 2. 字符串索引和切片 =====

print("\n=== 字符串索引和切片 ===")

text = "Python编程"

# 索引访问
print(f"字符串: {text}")
print(f"正向索引: text[0] = '{text[0]}'")
print(f"反向索引: text[-1] = '{text[-1]}'")

# 切片操作
print(f"text[0:6] = '{text[0:6]}'")
print(f"text[6:] = '{text[6:]}'")
print(f"text[:6] = '{text[:6]}'")
print(f"text[::-1] = '{text[::-1]}'")  # 反转字符串
print(f"text[::2] = '{text[::2]}'")    # 每隔一个字符

# ===== 3. 字符串方法 =====

print("\n=== 字符串方法 ===")

text = "  Hello, Python World!  "

# 大小写转换
print(f"原字符串: '{text}'")
print(f"upper(): '{text.upper()}'")
print(f"lower(): '{text.lower()}'")
print(f"title(): '{text.title()}'")
print(f"capitalize(): '{text.capitalize()}'")

# 空白处理
print(f"strip(): '{text.strip()}'")
print(f"lstrip(): '{text.lstrip()}'")
print(f"rstrip(): '{text.rstrip()}'")

# 查找和替换
text2 = "Python is great, Python is easy"
print(f"\n原字符串: '{text2}'")
print(f"find('Python'): {text2.find('Python')}")
print(f"rfind('Python'): {text2.rfind('Python')}")
print(f"count('Python'): {text2.count('Python')}")
print(f"replace('Python', 'Java'): '{text2.replace('Python', 'Java')}'")

# 分割和连接
sentence = "Python,Java,C++,JavaScript"
languages = sentence.split(",")
print(f"\n原字符串: '{sentence}'")
print(f"split(','): {languages}")
print(f"join(): '{', '.join(languages)}'")

# ===== 4. 字符串格式化进阶 =====

print("\n=== 字符串格式化进阶 ===")

# format()方法详解
name, age, salary = "张三", 25, 5000.50

# 位置参数
print("姓名: {}, 年龄: {}".format(name, age))

# 关键字参数
print("姓名: {name}, 年龄: {age}".format(name=name, age=age))

# 格式化数字
print("薪水: {:.2f}".format(salary))
print("年龄: {:03d}".format(age))  # 补零

# f-string高级用法
pi = 3.14159265359
print(f"圆周率: {pi:.2f}")      # 小数点后2位
print(f"圆周率: {pi:10.3f}")    # 宽度10，右对齐
print(f"圆周率: {pi:<10.3f}")   # 左对齐
print(f"圆周率: {pi:^10.3f}")   # 居中对齐

# 表达式计算
x, y = 10, 20
print(f"计算: {x} + {y} = {x + y}")

# ===== 5. 字符串判断方法 =====

print("\n=== 字符串判断方法 ===")

test_strings = [
    "Hello123",
    "hello",
    "HELLO",
    "Hello World",
    "123",
    "   ",
    "",
    "Hello-World_123"
]

for s in test_strings:
    print(f"字符串: '{s}'")
    print(f"  isalpha(): {s.isalpha()}")
    print(f"  isdigit(): {s.isdigit()}")
    print(f"  isalnum(): {s.isalnum()}")
    print(f"  isspace(): {s.isspace()}")
    print(f"  isupper(): {s.isupper()}")
    print(f"  islower(): {s.islower()}")
    print(f"  istitle(): {s.istitle()}")
    print(f"  startswith('H'): {s.startswith('H')}")
    print(f"  endswith('3'): {s.endswith('3')}")
    print()

# ===== 6. 字符串编码和解码 =====

print("=== 字符串编码和解码 ===")

text = "Hello, 世界!"

# 编码为字节
utf8_bytes = text.encode('utf-8')
print(f"UTF-8编码: {utf8_bytes}")
print(f"类型: {type(utf8_bytes)}")

# 解码回字符串
decoded_text = utf8_bytes.decode('utf-8')
print(f"解码回字符串: {decoded_text}")

# 其他编码
try:
    gbk_bytes = text.encode('gbk')
    print(f"GBK编码: {gbk_bytes}")
except UnicodeEncodeError as e:
    print(f"GBK编码错误: {e}")

# ===== 7. 正则表达式基础 =====

print("\n=== 正则表达式基础 ===")

import re

text = "我的邮箱是user@example.com，另一个是test123@gmail.com"
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# 查找所有匹配
emails = re.findall(email_pattern, text)
print(f"找到的邮箱: {emails}")

# 匹配电话号码
phone_text = "联系电话: 138-1234-5678 或 (010)8888-9999"
phone_pattern = r'\(?\d{3,4}\)?[-]?\d{3,4}[-]?\d{4}'

phones = re.findall(phone_pattern, phone_text)
print(f"找到的电话: {phones}")

# 替换
censored = re.sub(email_pattern, "[邮箱已隐藏]", text)
print(f"隐藏邮箱: {censored}")

# 分组匹配
date_text = "今天是2024年12月26日"
date_pattern = r'(\d{4})年(\d{1,2})月(\d{1,2})日'

match = re.search(date_pattern, date_text)
if match:
    year, month, day = match.groups()
    print(f"解析日期: {year}年{month}月{day}日")

# ===== 8. 字符串模板 =====

print("\n=== 字符串模板 ===")

from string import Template

# 创建模板
template = Template("Hello, $name! Welcome to $place.")
result = template.substitute(name="张三", place="Python世界")
print(f"模板替换: {result}")

# 使用字典
data = {"name": "李四", "place": "编程世界"}
result2 = template.substitute(data)
print(f"字典替换: {result2}")

# 安全替换（避免KeyError）
safe_template = Template("Hello, $name! Welcome to ${place}.")
try:
    result3 = safe_template.safe_substitute(name="王五")  # 缺少place
    print(f"安全替换: {result3}")
except Exception as e:
    print(f"错误: {e}")

# ===== 9. 多语言字符串处理 =====

print("\n=== 多语言字符串处理 ===")

# Unicode字符串
chinese = "你好世界"
japanese = "こんにちは世界"
korean = "안녕하세요 세계"

print(f"中文: {chinese}")
print(f"日文: {japanese}")
print(f"韩文: {korean}")

# 字符串长度（Unicode字符数）
print(f"中文长度: {len(chinese)}")
print(f"日文长度: {len(japanese)}")
print(f"韩文长度: {len(korean)}")

# 字符串反转（考虑Unicode）
def reverse_unicode(text):
    """正确反转Unicode字符串"""
    return ''.join(reversed(text))

print(f"中文反转: {reverse_unicode(chinese)}")
print(f"日文反转: {reverse_unicode(japanese)}")

# ===== 10. 字符串性能优化 =====

print("\n=== 字符串性能优化 ===")

import time

# 字符串拼接性能对比
n = 10000

# 方法1: 使用+运算符（低效）
start = time.time()
result1 = ""
for i in range(n):
    result1 += str(i)
time1 = time.time() - start

# 方法2: 使用join()方法（高效）
start = time.time()
result2 = ''.join(str(i) for i in range(n))
time2 = time.time() - start

print(".4f")
print(".4f")
print(".1f")

# ===== 练习 =====

print("\n=== 练习时间 ===")

# 练习1: 文本分析器
def text_analyzer():
    """文本分析器"""
    text = """
    Python是一种高级编程语言，由Guido van Rossum于1991年创建。
    Python的设计哲学强调代码的可读性和简洁性。
    它的语法简洁明了，易于学习和使用。
    """

    print("文本分析结果:")
    print(f"字符数: {len(text)}")
    print(f"单词数: {len(text.split())}")
    print(f"行数: {len(text.strip().split('\n'))}")

    # 统计字母频率
    letters = [c.lower() for c in text if c.isalpha()]
    letter_freq = {}
    for letter in letters:
        letter_freq[letter] = letter_freq.get(letter, 0) + 1

    print("字母频率 (前5个):")
    sorted_freq = sorted(letter_freq.items(), key=lambda x: x[1], reverse=True)
    for letter, count in sorted_freq[:5]:
        print(f"  {letter}: {count}")

# 练习2: 密码强度检查器
def password_strength_checker():
    """密码强度检查器"""

    def check_password(password):
        """检查密码强度"""
        strength = 0
        feedback = []

        if len(password) >= 8:
            strength += 1
        else:
            feedback.append("密码长度应至少8位")

        if re.search(r'[A-Z]', password):
            strength += 1
        else:
            feedback.append("应包含大写字母")

        if re.search(r'[a-z]', password):
            strength += 1
        else:
            feedback.append("应包含小写字母")

        if re.search(r'\d', password):
            strength += 1
        else:
            feedback.append("应包含数字")

        if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            strength += 1
        else:
            feedback.append("应包含特殊字符")

        strength_levels = ["非常弱", "弱", "中等", "强", "非常强"]
        level = strength_levels[min(strength, 4)]

        return level, feedback

    # 测试密码
    test_passwords = [
        "123",
        "password",
        "Password123",
        "P@ssw0rd123",
        "Str0ng!P@ssw0rd#2024"
    ]

    print("密码强度检查:")
    for pwd in test_passwords:
        level, feedback = check_password(pwd)
        print(f"\n密码: {pwd}")
        print(f"强度: {level}")
        if feedback:
            print("建议改进:")
            for item in feedback:
                print(f"  - {item}")

# 练习3: 文本格式化工具
def text_formatter():
    """文本格式化工具"""

    def format_text(text, width=50, alignment='left'):
        """格式化文本"""
        words = text.split()
        lines = []
        current_line = []

        for word in words:
            if len(' '.join(current_line + [word])) <= width:
                current_line.append(word)
            else:
                lines.append(' '.join(current_line))
                current_line = [word]

        if current_line:
            lines.append(' '.join(current_line))

        # 对齐处理
        formatted_lines = []
        for line in lines:
            if alignment == 'left':
                formatted_lines.append(line.ljust(width))
            elif alignment == 'right':
                formatted_lines.append(line.rjust(width))
            elif alignment == 'center':
                formatted_lines.append(line.center(width))

        return '\n'.join(formatted_lines)

    sample_text = "Python是一种解释型、高级编程语言，以其简洁、易读的语法而闻名。它支持多种编程范式，包括面向对象、函数式和过程式编程。"

    print("文本格式化示例:")
    print("\n左对齐 (宽度50):")
    print(format_text(sample_text, 50, 'left'))

    print("\n居中对齐 (宽度40):")
    print(format_text(sample_text, 40, 'center'))

# 练习4: 字符串压缩和解压
def string_compression():
    """简单的字符串压缩"""

    def compress_string(text):
        """压缩重复字符"""
        if not text:
            return ""

        compressed = []
        count = 1
        current = text[0]

        for char in text[1:]:
            if char == current:
                count += 1
            else:
                compressed.append(f"{current}{count}" if count > 1 else current)
                current = char
                count = 1

        compressed.append(f"{current}{count}" if count > 1 else current)
        return ''.join(compressed)

    def decompress_string(compressed):
        """解压字符串"""
        import re
        # 分离字母和数字
        parts = re.findall(r'([A-Za-z])(\d*)', compressed)

        result = []
        for char, count in parts:
            count = int(count) if count else 1
            result.append(char * count)

        return ''.join(result)

    # 测试压缩
    test_strings = [
        "aaabbbccc",
        "abc",
        "aabbccddd",
        "aaaaaabbbbbccccc"
    ]

    print("字符串压缩示例:")
    for original in test_strings:
        compressed = compress_string(original)
        decompressed = decompress_string(compressed)
        print(f"原字符串: {original}")
        print(f"压缩后: {compressed}")
        print(f"解压后: {decompressed}")
        print(f"压缩正确: {original == decompressed}")
        print()

# 运行练习
print("练习1: 文本分析器")
text_analyzer()

print("\n练习2: 密码强度检查器")
password_strength_checker()

print("\n练习3: 文本格式化工具")
text_formatter()

print("\n练习4: 字符串压缩")
string_compression()
