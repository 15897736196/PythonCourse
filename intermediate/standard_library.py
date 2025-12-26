# Python学习项目 - 中级内容：标准库精选
# 学习序号：第6阶段 第2课 - 标准库精选
# 建议学习时间：90-120分钟
# 前置知识：第6阶段 第1课 - 文件操作
# 下一课：第7阶段 第1课 - 装饰器 (advanced/decorators.py)
# 本模块介绍Python标准库中最重要的模块和实用功能

"""
Python标准库提供了丰富的基础功能，无需额外安装即可使用。
本模块涵盖最常用的标准库模块：

系统和环境:
- sys: 系统相关功能
- os: 操作系统接口

时间和日期:
- datetime: 日期时间处理
- time: 时间函数

数学和随机:
- math: 数学函数
- random: 随机数生成
- statistics: 统计函数

数据处理:
- json: JSON数据处理
- csv: CSV文件处理
- pickle: 对象序列化

数据结构:
- collections: 高级数据结构

文本处理:
- re: 正则表达式
- string: 字符串操作

实用工具:
- itertools: 迭代器工具
- functools: 函数工具
- operator: 操作符函数
"""

import sys
import os
import datetime
import time
import math
import random
import statistics
import json
import csv
import pickle
import re
import string
import collections
import itertools
import functools
import operator
from urllib.parse import urlparse, urljoin, quote, unquote
from urllib.request import urlopen
import argparse

# ===== 1. 系统相关模块 =====

print("=== 系统相关模块 ===")

# sys模块
print("sys模块:")
print(f"  Python版本: {sys.version}")
print(f"  平台: {sys.platform}")
print(f"  可执行文件路径: {sys.executable}")
print(f"  命令行参数: {sys.argv}")
print(f"  Python路径: {sys.path[:3]}...")  # 只显示前3个

# 获取系统信息
print(f"  递归深度限制: {sys.getrecursionlimit()}")

# os模块
print("\nOS模块:")
print(f"  当前工作目录: {os.getcwd()}")
print(f"  环境变量PATH: {os.environ.get('PATH', 'N/A')[:50]}...")
print(f"  操作系统: {os.name}")

# 路径操作
current_file = os.path.abspath(__file__)
print(f"  当前文件路径: {current_file}")
print(f"  文件名: {os.path.basename(current_file)}")
print(f"  目录名: {os.path.dirname(current_file)}")

# ===== 2. 时间和日期处理 =====

print("\n=== 时间和日期处理 ===")

# datetime模块
print("datetime模块:")

# 当前时间
now = datetime.datetime.now()
print(f"  当前时间: {now}")
print(f"  日期: {now.date()}")
print(f"  时间: {now.time()}")

# 格式化时间
formatted = now.strftime("%Y年%m月%d日 %H:%M:%S")
print(f"  格式化时间: {formatted}")

# 解析时间字符串
date_string = "2024-12-26 18:30:00"
parsed = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(f"  解析时间: {parsed}")

# 时间运算
tomorrow = now + datetime.timedelta(days=1)
next_week = now + datetime.timedelta(weeks=1)
print(f"  明天: {tomorrow.date()}")
print(f"  下周: {next_week.date()}")

# time模块
print("\ntime模块:")
start_time = time.time()
time.sleep(0.1)  # 暂停0.1秒
end_time = time.time()

print(".4f")
print(f"  CPU时间: {time.process_time():.4f}秒")

# 时间戳转换
timestamp = time.time()
local_time = time.localtime(timestamp)
print(f"  时间戳: {timestamp}")
print(f"  本地时间: {time.strftime('%Y-%m-%d %H:%M:%S', local_time)}")

# ===== 3. 数学和随机数 =====

print("\n=== 数学和随机数 ===")

# math模块
print("math模块:")
print(f"  π: {math.pi:.6f}")
print(f"  e: {math.e:.6f}")
print(f"  平方根(16): {math.sqrt(16)}")
print(f"  2的3次方: {math.pow(2, 3)}")
print(f"  sin(π/2): {math.sin(math.pi/2):.6f}")
print(f"  向上取整(3.2): {math.ceil(3.2)}")
print(f"  向下取整(3.8): {math.floor(3.8)}")
print(f"  四舍五入(3.5): {round(3.5)}")

# random模块
print("\nrandom模块:")

# 设置种子保证结果可重现
random.seed(42)

print(f"  随机整数(1-10): {random.randint(1, 10)}")
print(f"  随机浮点数(0-1): {random.random():.4f}")
print(f"  随机选择: {random.choice(['苹果', '香蕉', '橙子'])}")
print(f"  随机样本: {random.sample(range(1, 11), 3)}")

# 生成随机列表并打乱
numbers = list(range(1, 11))
random.shuffle(numbers)
print(f"  打乱顺序: {numbers}")

# statistics模块
print("\nstatistics模块:")
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"  数据: {data}")
print(f"  平均值: {statistics.mean(data):.2f}")
print(f"  中位数: {statistics.median(data)}")
print(f"  众数: {statistics.mode([1, 2, 2, 3, 3, 3])}")
print(f"  方差: {statistics.variance(data):.2f}")
print(f"  标准差: {statistics.stdev(data):.2f}")

# ===== 4. 数据序列化 =====

print("\n=== 数据序列化 ===")

# 准备测试数据
test_data = {
    "user": {
        "name": "张三",
        "age": 25,
        "city": "北京"
    },
    "items": ["苹果", "香蕉", "橙子"],
    "timestamp": datetime.datetime.now().isoformat()
}

# JSON序列化
print("JSON序列化:")
json_string = json.dumps(test_data, ensure_ascii=False, indent=2)
print(f"  JSON字符串:\n{json_string}")

# JSON反序列化
parsed_data = json.loads(json_string)
print(f"  解析后数据: user={parsed_data['user']['name']}, items={len(parsed_data['items'])}个")

# pickle序列化
print("\npickle序列化:")
pickled_data = pickle.dumps(test_data)
print(f"  pickle数据长度: {len(pickled_data)} bytes")

# pickle反序列化
unpickled_data = pickle.loads(pickled_data)
print(f"  反序列化后: {unpickled_data['user']['name']}")

# ===== 5. CSV文件处理 =====

print("\n=== CSV文件处理 ===")

# 创建CSV数据
csv_data = [
    ["姓名", "年龄", "城市"],
    ["张三", 25, "北京"],
    ["李四", 30, "上海"],
    ["王五", 28, "广州"]
]

# 写入CSV字符串
csv_output = []
for row in csv_data:
    csv_output.append(','.join(str(item) for item in row))

print("CSV数据:")
for line in csv_output:
    print(f"  {line}")

# 使用csv模块
import io
csv_string = io.StringIO()
writer = csv.writer(csv_string)
writer.writerows(csv_data)

print(f"\ncsv模块输出:\n{csv_string.getvalue()}")

# ===== 6. 正则表达式 =====

print("\n=== 正则表达式 ===")

text = """
联系我们：
邮箱：user@example.com 或 support@company.com
电话：138-1234-5678 或 (010) 8888-9999
网址：https://www.example.com/page?q=test
日期：2024-12-26 或 2024/12/26
"""

print("正则表达式匹配:")

# 邮箱匹配
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
emails = re.findall(email_pattern, text)
print(f"  邮箱: {emails}")

# 电话号码匹配
phone_pattern = r'\(?\d{3,4}\)?[-]?\d{3,4}[-]?\d{4}'
phones = re.findall(phone_pattern, text)
print(f"  电话: {phones}")

# URL匹配
url_pattern = r'https?://[^\s]+'
urls = re.findall(url_pattern, text)
print(f"  网址: {urls}")

# 日期匹配
date_pattern = r'\d{4}[-/]\d{1,2}[-/]\d{1,2}'
dates = re.findall(date_pattern, text)
print(f"  日期: {dates}")

# 字符串替换
censored = re.sub(email_pattern, "[邮箱隐藏]", text)
print(f"\n隐藏邮箱:\n{censored[:100]}...")

# ===== 7. 字符串操作增强 =====

print("\n=== 字符串操作增强 ===")

# string模块
print("string模块:")

# 预定义字符串常量
print(f"  字母: {string.ascii_letters[:20]}...")
print(f"  数字: {string.digits}")
print(f"  标点: {string.punctuation[:10]}...")

# 字符串模板
template = string.Template("Hello, $name! Welcome to $place.")
result = template.substitute(name="张三", place="Python世界")
print(f"  字符串模板: {result}")

# 高级格式化
data = {"name": "李四", "score": 95.5}
formatted = string.Formatter().format("学生{name}的分数是{score:.1f}", **data)
print(f"  高级格式化: {formatted}")

# ===== 8. 高级数据结构 =====

print("\n=== 高级数据结构 ===")

# collections模块
print("collections模块:")

# Counter - 计数器
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_count = collections.Counter(words)
print(f"  Counter: {word_count}")
print(f"  最常见的2个: {word_count.most_common(2)}")

# defaultdict - 默认字典
word_dict = collections.defaultdict(list)
for word in words:
    word_dict[word[0]].append(word)  # 按首字母分组
print(f"  defaultdict分组: {dict(word_dict)}")

# namedtuple - 命名元组
Person = collections.namedtuple('Person', ['name', 'age', 'city'])
person = Person(name="张三", age=25, city="北京")
print(f"  namedtuple: {person}")
print(f"  访问属性: {person.name}, {person.age}岁")

# deque - 双端队列
deq = collections.deque([1, 2, 3, 4, 5])
deq.append(6)      # 右端添加
deq.appendleft(0)  # 左端添加
print(f"  deque: {list(deq)}")
print(f"  弹出左端: {deq.popleft()}")
print(f"  弹出右端: {deq.pop()}")

# ===== 9. 迭代器工具 =====

print("\n=== 迭代器工具 ===")

# itertools模块
print("itertools模块:")

# count - 无限计数
print(f"  count: {list(itertools.islice(itertools.count(10), 5))}")

# cycle - 循环
print(f"  cycle: {list(itertools.islice(itertools.cycle('ABC'), 7))}")

# repeat - 重复
print(f"  repeat: {list(itertools.repeat('Python', 3))}")

# chain - 连接
print(f"  chain: {list(itertools.chain([1, 2], [3, 4], [5, 6]))}")

# combinations - 组合
items = ['A', 'B', 'C']
print(f"  combinations: {list(itertools.combinations(items, 2))}")

# permutations - 排列
print(f"  permutations: {list(itertools.permutations(items, 2))}")

# product - 笛卡尔积
print(f"  product: {list(itertools.product([1, 2], ['A', 'B']))}")

# ===== 10. 函数工具 =====

print("\n=== 函数工具 ===")

# functools模块
print("functools模块:")

# partial - 偏函数
def multiply(x, y, z=1):
    return x * y * z

double = functools.partial(multiply, y=2)
triple = functools.partial(multiply, y=3, z=2)

print(f"  partial - double(5): {double(5)}")
print(f"  partial - triple(5): {triple(5)}")

# lru_cache - 缓存装饰器
@functools.lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

start_time = time.time()
fib_30 = fibonacci(30)
cache_time = time.time() - start_time

start_time = time.time()
fib_30_again = fibonacci(30)  # 从缓存获取
cached_time = time.time() - start_time

print(".6f")
print(".6f")

# reduce - 累积操作
numbers = [1, 2, 3, 4, 5]
product = functools.reduce(operator.mul, numbers)
print(f"  reduce - 乘积: {product}")

# ===== 11. 操作符函数 =====

print("\n=== 操作符函数 ===")

# operator模块
print("operator模块:")

# 算术操作符
print(f"  add(5, 3): {operator.add(5, 3)}")
print(f"  mul(5, 3): {operator.mul(5, 3)}")
print(f"  pow(5, 3): {operator.pow(5, 3)}")

# 比较操作符
numbers_list = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_list = sorted(numbers_list, key=operator.neg)  # 按负值排序（降序）
print(f"  降序排序: {sorted_list}")

# 属性和项目获取
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

points = [Point(1, 2), Point(3, 1), Point(2, 3)]
sorted_by_x = sorted(points, key=operator.attrgetter('x'))
print(f"  按x坐标排序: {[(p.x, p.y) for p in sorted_by_x]}")

# ===== 12. URL处理 =====

print("\n=== URL处理 ===")

# urllib.parse模块
print("urllib.parse模块:")

test_urls = [
    "https://www.example.com/path/to/page?q=search&page=1",
    "ftp://ftp.example.com/files/data.zip",
    "/relative/path/file.txt"
]

for url in test_urls:
    parsed = urlparse(url)
    print(f"\n  URL: {url}")
    print(f"  协议: {parsed.scheme}")
    print(f"  主机: {parsed.netloc}")
    print(f"  路径: {parsed.path}")
    print(f"  查询: {parsed.query}")

# URL编码/解码
chinese_text = "你好世界"
encoded = quote(chinese_text)
decoded = unquote(encoded)
print(f"\n  中文: {chinese_text}")
print(f"  编码: {encoded}")
print(f"  解码: {decoded}")

# ===== 13. 命令行参数解析 =====

print("\n=== 命令行参数解析 ===")

# argparse模块 (模拟命令行参数)
print("argparse模块示例:")

# 创建参数解析器
parser = argparse.ArgumentParser(description="示例命令行工具")
parser.add_argument('--name', default='World', help='问候对象')
parser.add_argument('--count', type=int, default=1, help='问候次数')
parser.add_argument('--verbose', action='store_true', help='详细输出')

# 模拟命令行参数
test_args = ['--name', 'Python', '--count', '3', '--verbose']
args = parser.parse_args(test_args)

print(f"  解析结果: name={args.name}, count={args.count}, verbose={args.verbose}")

# 执行逻辑
for i in range(args.count):
    if args.verbose:
        print(f"  [INFO] 这是第{i+1}次问候")
    print(f"  Hello, {args.name}!")

# ===== 练习 =====

print("\n=== 练习时间 ===")

# 练习1: 使用标准库实现数据分析
def data_analysis_demo():
    """数据分析演示"""
    # 生成随机数据
    random.seed(42)
    data = [random.normalvariate(100, 15) for _ in range(1000)]  # 正态分布数据

    print("数据分析演示:")
    print(".2f")
    print(".2f")
    print(".2f")

    # 分位数
    sorted_data = sorted(data)
    q1 = statistics.quantiles(sorted_data, n=4)[0]
    q3 = statistics.quantiles(sorted_data, n=4)[2]
    iqr = q3 - q1
    print(".2f")

    # 频率分布
    bins = [50, 70, 90, 110, 130, 150]
    freq = collections.Counter()
    for value in data:
        for i, bin_edge in enumerate(bins):
            if value <= bin_edge:
                freq[f"≤{bin_edge}"] += 1
                break
        else:
            freq[f">{bins[-1]}"] += 1

    print(f"  频率分布: {dict(freq)}")

# 练习2: 使用标准库实现文本处理
def text_processing_demo():
    """文本处理演示"""
    text = """
    Python是一门强大的编程语言。Python的设计哲学强调代码的可读性和简洁性。
    Python广泛应用于Web开发、数据科学、人工智能等领域。
    """

    # 分词
    words = re.findall(r'\b\w+\b', text.lower())

    # 词频统计
    word_freq = collections.Counter(words)

    # 去除停用词
    stop_words = {'是', '一', '门', '的', '和', '性', '于', '等', '在'}
    filtered_words = [word for word in words if word not in stop_words and len(word) > 1]

    print("文本处理演示:")
    print(f"  总词数: {len(words)}")
    print(f"  唯一词数: {len(set(words))}")
    print(f"  最常见单词: {word_freq.most_common(5)}")
    print(f"  过滤后单词: {filtered_words[:10]}...")

    # 句子分割
    sentences = re.split(r'[。！？]', text.strip())
    sentences = [s.strip() for s in sentences if s.strip()]
    print(f"  句子数: {len(sentences)}")

# 练习3: 使用标准库实现配置文件解析
def config_parser_demo():
    """配置文件解析演示"""
    import configparser

    # 创建配置
    config = configparser.ConfigParser()
    config.add_section('database')
    config.set('database', 'host', 'localhost')
    config.set('database', 'port', '5432')
    config.set('database', 'name', 'mydb')

    config.add_section('app')
    config.set('app', 'debug', 'true')
    config.set('app', 'max_connections', '100')

    # 写入字符串
    import io
    config_string = io.StringIO()
    config.write(config_string)
    config_content = config_string.getvalue()

    print("配置文件解析演示:")
    print("生成的配置内容:")
    print(config_content)

    # 解析配置
    config_string.seek(0)
    parsed_config = configparser.ConfigParser()
    parsed_config.read_string(config_content)

    print("解析结果:")
    for section in parsed_config.sections():
        print(f"  [{section}]")
        for key, value in parsed_config.items(section):
            print(f"    {key} = {value}")

# 运行练习
print("练习1: 数据分析演示")
data_analysis_demo()

print("\n练习2: 文本处理演示")
text_processing_demo()

print("\n练习3: 配置文件解析演示")
config_parser_demo()

print("\n标准库精选学习完成！Python标准库提供了丰富的基础功能，掌握这些模块能大大提高开发效率。")
