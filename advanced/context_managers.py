# Python学习项目 - 高级特性：上下文管理器
# 学习序号：第7阶段 第3课 - 上下文管理器
# 建议学习时间：60-90分钟
# 前置知识：第7阶段 第1-2课 - 装饰器和生成器
# 下一课：第8阶段 第1课 - 计算器项目 (projects/calculator.py)
# 本模块介绍Python上下文管理器的概念、使用方法和实际应用

"""
上下文管理器(Context Managers)是Python中用于资源管理的高级特性，
主要通过with语句使用。上下文管理器确保资源在使用完毕后得到正确清理。

主要用途：
1. 文件操作 - 自动关闭文件
2. 数据库连接 - 自动关闭连接
3. 锁管理 - 自动释放锁
4. 临时文件 - 自动清理临时文件
5. 网络连接 - 自动关闭连接
6. 事务管理 - 自动提交或回滚

上下文管理器协议：
- __enter__(): 进入上下文时调用，返回资源对象
- __exit__(exc_type, exc_val, exc_tb): 退出上下文时调用，处理清理逻辑
"""

import time
import threading
import tempfile
import os
import sqlite3
from typing import Any, Optional, Type
from contextlib import contextmanager, ContextDecorator

# ===== 1. 上下文管理器基础 =====

print("=== 上下文管理器基础 ===")

# 基本的上下文管理器类
class Timer:
    """计时器上下文管理器"""

    def __init__(self, name="操作"):
        self.name = name
        self.start_time = None

    def __enter__(self):
        """进入上下文"""
        self.start_time = time.time()
        print(f"开始{self.name}...")
        return self  # 可以返回任何对象，这里返回self以便访问方法

    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出上下文"""
        end_time = time.time()
        duration = end_time - self.start_time
        print(".4f")

        # 返回False表示不处理异常，让异常继续传播
        return False

# 使用上下文管理器
with Timer("数据处理"):
    time.sleep(0.5)  # 模拟耗时操作
    data = [x**2 for x in range(1000)]

# ===== 2. 资源管理示例 =====

print("\n=== 资源管理示例 ===")

class FileManager:
    """文件管理器上下文管理器"""

    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        """打开文件"""
        try:
            self.file = open(self.filename, self.mode, encoding='utf-8')
            return self.file
        except FileNotFoundError:
            raise FileNotFoundError(f"文件 '{self.filename}' 不存在")
        except PermissionError:
            raise PermissionError(f"没有权限访问文件 '{self.filename}'")

    def __exit__(self, exc_type, exc_val, exc_tb):
        """关闭文件"""
        if self.file:
            self.file.close()
            print(f"文件 '{self.filename}' 已关闭")

        # 如果有异常，记录但不处理
        if exc_type:
            print(f"在处理文件时发生异常: {exc_type.__name__}")

        return False  # 不处理异常

# 创建测试文件
with open('test_file.txt', 'w', encoding='utf-8') as f:
    f.write("这是一行测试文本\n")
    f.write("这是第二行\n")

# 使用文件管理器
try:
    with FileManager('test_file.txt', 'r') as file:
        content = file.read()
        print(f"文件内容:\n{content}")
except FileNotFoundError as e:
    print(f"错误: {e}")

# ===== 3. 数据库连接管理器 =====

print("\n=== 数据库连接管理器 ===")

class DatabaseConnection:
    """数据库连接上下文管理器"""

    def __init__(self, db_name="test.db"):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        """建立数据库连接"""
        self.connection = sqlite3.connect(self.db_name)
        print(f"数据库 '{self.db_name}' 连接已建立")
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        """关闭数据库连接"""
        if self.connection:
            if exc_type:
                # 如果有异常，回滚事务
                self.connection.rollback()
                print("事务已回滚")
            else:
                # 如果没有异常，提交事务
                self.connection.commit()
                print("事务已提交")

            self.connection.close()
            print(f"数据库 '{self.db_name}' 连接已关闭")

        return False

# 使用数据库连接管理器
with DatabaseConnection() as conn:
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER
        )
    ''')

    # 插入数据
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("张三", 25))
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("李四", 30))

    # 查询数据
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    print("用户数据:")
    for user in users:
        print(f"  ID: {user[0]}, 姓名: {user[1]}, 年龄: {user[2]}")

# ===== 4. contextlib模块 =====

print("\n=== contextlib模块 ===")

import contextlib

# 使用@contextmanager装饰器
@contextmanager
def timer_context(name="操作"):
    """基于生成器的上下文管理器"""
    start_time = time.time()
    print(f"开始{name}...")
    try:
        yield  # 这里可以返回资源对象
    finally:
        end_time = time.time()
        duration = end_time - start_time
        print(".4f")

# 使用基于生成器的上下文管理器
with timer_context("数学计算"):
    result = sum(x**2 for x in range(10000))

# 文件操作的contextmanager版本
@contextmanager
def safe_open(filename, mode='r'):
    """安全的文件打开器"""
    try:
        file = open(filename, mode, encoding='utf-8')
        yield file
    finally:
        file.close()
        print(f"文件 '{filename}' 已自动关闭")

# 使用安全的文件打开器
with safe_open('test_file.txt', 'r') as f:
    content = f.read()
    print(f"读取的内容: {content[:30]}...")

# ===== 5. 嵌套上下文管理器 =====

print("\n=== 嵌套上下文管理器 ===")

@contextmanager
def indent_log(level=0):
    """缩进日志上下文管理器"""
    indent = "  " * level
    print(f"{indent}进入上下文 (级别 {level})")
    try:
        yield level
    finally:
        print(f"{indent}退出上下文 (级别 {level})")

# 嵌套使用
with indent_log(0):
    print("在级别0中")
    with indent_log(1):
        print("在级别1中")
        with indent_log(2):
            print("在级别2中")
    print("回到级别0")

# ===== 6. 锁管理 =====

print("\n=== 锁管理 ===")

class LockManager:
    """线程锁管理器"""

    def __init__(self):
        self.lock = threading.Lock()

    def __enter__(self):
        """获取锁"""
        self.lock.acquire()
        print("锁已获取")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """释放锁"""
        self.lock.release()
        print("锁已释放")
        return False

# 模拟多线程资源访问
shared_resource = []

def worker_thread(thread_id, lock_manager):
    """工作线程"""
    with lock_manager:
        # 模拟一些工作
        time.sleep(0.1)
        shared_resource.append(f"线程{thread_id}的工作结果")
        print(f"线程{thread_id} 完成了工作")

lock_manager = LockManager()
threads = []

# 创建多个线程
for i in range(3):
    thread = threading.Thread(target=worker_thread, args=(i+1, lock_manager))
    threads.append(thread)
    thread.start()

# 等待所有线程完成
for thread in threads:
    thread.join()

print(f"所有线程完成，最终结果: {shared_resource}")

# ===== 7. ContextDecorator =====

print("\n=== ContextDecorator ===")

class MyContextDecorator(ContextDecorator):
    """可作为装饰器和上下文管理器使用的类"""

    def __enter__(self):
        print("进入上下文")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("退出上下文")
        return False

# 作为上下文管理器使用
with MyContextDecorator():
    print("在上下文中执行")

# 作为装饰器使用
@MyContextDecorator()
def decorated_function():
    print("函数执行中")

decorated_function()

# ===== 8. 临时文件和目录管理 =====

print("\n=== 临时文件和目录管理 ===")

@contextmanager
def temporary_file(suffix='', prefix='tmp', dir=None):
    """临时文件上下文管理器"""
    fd, path = tempfile.mkstemp(suffix=suffix, prefix=prefix, dir=dir)
    try:
        # 关闭文件描述符，让path可以被其他程序使用
        os.close(fd)
        yield path
    finally:
        # 清理临时文件
        if os.path.exists(path):
            os.unlink(path)
            print(f"临时文件 {path} 已删除")

@contextmanager
def temporary_directory(suffix='', prefix='tmp', dir=None):
    """临时目录上下文管理器"""
    temp_dir = tempfile.mkdtemp(suffix=suffix, prefix=prefix, dir=dir)
    try:
        yield temp_dir
    finally:
        # 递归删除临时目录
        import shutil
        shutil.rmtree(temp_dir)
        print(f"临时目录 {temp_dir} 已删除")

# 使用临时文件
with temporary_file(suffix='.txt') as temp_path:
    print(f"临时文件路径: {temp_path}")
    with open(temp_path, 'w', encoding='utf-8') as f:
        f.write("这是临时文件内容\n")
        f.write("它会在上下文结束后被删除\n")

    # 读取验证
    with open(temp_path, 'r', encoding='utf-8') as f:
        content = f.read()
        print(f"临时文件内容: {content[:30]}...")

# 使用临时目录
with temporary_directory(prefix='myapp_') as temp_dir:
    print(f"临时目录路径: {temp_dir}")

    # 在临时目录中创建文件
    test_file = os.path.join(temp_dir, 'test.txt')
    with open(test_file, 'w', encoding='utf-8') as f:
        f.write("临时目录中的文件")

    # 列出目录内容
    contents = os.listdir(temp_dir)
    print(f"临时目录内容: {contents}")

# ===== 9. 自定义异常处理上下文 =====

print("\n=== 自定义异常处理上下文 ===")

class ExceptionHandler:
    """异常处理上下文管理器"""

    def __init__(self, exceptions_to_handle=None, default_value=None):
        self.exceptions_to_handle = exceptions_to_handle or (Exception,)
        self.default_value = default_value
        self.exception_occurred = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type and issubclass(exc_type, self.exceptions_to_handle):
            print(f"捕获到异常: {exc_type.__name__}: {exc_val}")
            self.exception_occurred = exc_val
            return True  # 处理异常，不让它传播

        return False  # 不处理异常

# 使用异常处理上下文
def risky_operation(x):
    """有风险的操作"""
    if x < 0:
        raise ValueError("输入不能为负数")
    if x == 0:
        raise ZeroDivisionError("除零错误")
    return 10 / x

operations = [5, 0, -1, 2]

for x in operations:
    with ExceptionHandler((ValueError, ZeroDivisionError), default_value=0) as handler:
        result = risky_operation(x)
        print(f"操作 {x} 结果: {result}")

    if handler.exception_occurred:
        print(f"  使用默认值继续: {handler.default_value}")

# ===== 10. 上下文管理器的实际应用场景 =====

print("\n=== 上下文管理器的实际应用场景 ===")

# 场景1: 配置管理
class ConfigManager:
    """配置管理器"""

    def __init__(self, config_file):
        self.config_file = config_file
        self.original_config = {}

    def __enter__(self):
        """备份原始配置"""
        # 这里简化，假设配置存储在字典中
        self.original_config = {"debug": False, "max_connections": 10}
        print("配置备份完成")
        return self.original_config

    def __exit__(self, exc_type, exc_val, exc_tb):
        """恢复原始配置"""
        print("配置已恢复到原始状态")
        return False

# 场景2: 性能监控
@contextmanager
def performance_monitor(operation_name):
    """性能监控上下文管理器"""
    start_time = time.time()
    start_memory = 0  # 简化版，实际应该使用psutil等库

    print(f"开始监控: {operation_name}")

    try:
        yield
    finally:
        end_time = time.time()
        end_memory = 0  # 简化版

        duration = end_time - start_time
        memory_used = end_memory - start_memory

        print(".4f")
        if memory_used != 0:
            print(f"内存使用: {memory_used} MB")

# 使用性能监控
with performance_monitor("数据处理"):
    # 模拟数据处理
    data = []
    for i in range(10000):
        data.append(i ** 2)
    processed_data = [x for x in data if x % 2 == 0]

print(f"处理了 {len(processed_data)} 个偶数平方")

# ===== 练习 =====

print("\n=== 练习时间 ===")

# 练习1: 创建一个网络连接管理器
class NetworkConnection:
    """网络连接管理器"""

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connected = False

    def __enter__(self):
        """建立连接"""
        # 模拟网络连接
        time.sleep(0.1)  # 模拟连接时间
        self.connected = True
        print(f"连接到 {self.host}:{self.port}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """关闭连接"""
        if self.connected:
            # 模拟关闭连接
            time.sleep(0.05)
            self.connected = False
            print(f"连接 {self.host}:{self.port} 已关闭")
        return False

    def send_data(self, data):
        """发送数据"""
        if not self.connected:
            raise ConnectionError("连接未建立")
        print(f"发送数据: {data}")
        return f"响应: {data.upper()}"

# 测试网络连接管理器
with NetworkConnection("example.com", 80) as conn:
    response1 = conn.send_data("Hello")
    response2 = conn.send_data("World")
    print(f"响应: {response1}, {response2}")

# 练习2: 使用contextmanager创建HTML标签生成器
@contextmanager
def html_tag(tag_name, **attributes):
    """HTML标签生成器"""
    # 构建属性字符串
    attr_str = ""
    if attributes:
        attr_list = [f'{key}="{value}"' for key, value in attributes.items()]
        attr_str = " " + " ".join(attr_list)

    # 输出开始标签
    print(f"<{tag_name}{attr_str}>", end="")

    try:
        yield
    finally:
        # 输出结束标签
        print(f"</{tag_name}>", end="")

# 测试HTML标签生成器
print("\nHTML生成测试:")
with html_tag("div", class_="container", id="main"):
    with html_tag("h1", style="color: blue"):
        print("欢迎来到Python学习网站", end="")
    with html_tag("p"):
        print("这是一个使用上下文管理器生成的HTML页面", end="")

print()  # 换行

# 练习3: 创建一个事务管理器
class TransactionManager:
    """事务管理器"""

    def __init__(self):
        self.operations = []
        self.rollback_operations = []

    def __enter__(self):
        """开始事务"""
        print("事务开始")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """结束事务"""
        if exc_type:
            # 有异常，回滚
            print("事务失败，正在回滚...")
            for rollback_op in reversed(self.rollback_operations):
                try:
                    rollback_op()
                except Exception as e:
                    print(f"回滚操作失败: {e}")
            print("事务已回滚")
        else:
            # 没有异常，提交
            print("事务成功，正在提交...")
            for op in self.operations:
                try:
                    op()
                except Exception as e:
                    print(f"提交操作失败: {e}")
            print("事务已提交")

        return False  # 不处理异常

    def add_operation(self, operation, rollback_operation=None):
        """添加操作"""
        self.operations.append(operation)
        if rollback_operation:
            self.rollback_operations.append(rollback_operation)

# 测试事务管理器
def create_file(filename, content):
    """创建文件操作"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"文件 {filename} 已创建")

def delete_file(filename):
    """删除文件操作"""
    if os.path.exists(filename):
        os.unlink(filename)
        print(f"文件 {filename} 已删除")

with TransactionManager() as tm:
    # 添加创建文件的操作
    tm.add_operation(
        lambda: create_file("file1.txt", "内容1"),
        lambda: delete_file("file1.txt")
    )

    tm.add_operation(
        lambda: create_file("file2.txt", "内容2"),
        lambda: delete_file("file2.txt")
    )

    # 模拟一个会失败的操作
    # raise Exception("模拟错误")

# 检查文件是否存在
print(f"file1.txt 存在: {os.path.exists('file1.txt')}")
print(f"file2.txt 存在: {os.path.exists('file2.txt')}")

# 清理测试文件
for filename in ["file1.txt", "file2.txt"]:
    if os.path.exists(filename):
        os.unlink(filename)

# 练习4: 创建一个CD上下文管理器
@contextmanager
def change_directory(new_dir):
    """改变当前工作目录的上下文管理器"""
    original_dir = os.getcwd()
    try:
        os.chdir(new_dir)
        print(f"切换到目录: {new_dir}")
        yield
    finally:
        os.chdir(original_dir)
        print(f"回到原目录: {original_dir}")

# 测试目录切换
print(f"\n当前目录: {os.getcwd()}")

# 创建测试目录
test_dir = "test_directory"
os.makedirs(test_dir, exist_ok=True)

with change_directory(test_dir):
    print(f"在新目录中: {os.getcwd()}")
    # 在这里可以进行目录相关的操作

print(f"回到原目录: {os.getcwd()}")

# 清理测试目录
os.rmdir(test_dir)

# 练习5: 多重资源管理器
@contextmanager
def multi_resource_manager(*managers):
    """多重资源管理器"""
    resources = []
    try:
        for manager in managers:
            resource = manager.__enter__()
            resources.append((manager, resource))
        yield [resource for _, resource in resources]
    finally:
        # 反向退出
        for manager, _ in reversed(resources):
            try:
                manager.__exit__(None, None, None)
            except Exception as e:
                print(f"资源清理出错: {e}")

# 定义简单的资源管理器
class SimpleResource:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"获取资源: {self.name}")
        return self.name

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"释放资源: {self.name}")
        return False

# 测试多重资源管理器
resource1 = SimpleResource("数据库连接")
resource2 = SimpleResource("文件句柄")
resource3 = SimpleResource("网络连接")

with multi_resource_manager(resource1, resource2, resource3) as resources:
    print(f"同时管理 {len(resources)} 个资源: {resources}")
    # 在这里使用资源
    time.sleep(0.1)

print("\n上下文管理器学习完成！上下文管理器是Python资源管理的重要工具，掌握它能让你写出更加健壮和优雅的代码。")

# 清理剩余的测试文件
if os.path.exists('test_file.txt'):
    os.remove('test_file.txt')
