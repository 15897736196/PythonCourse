# Python学习项目 - 中级内容：异常处理
# 学习序号：第5阶段 第1课 - 异常处理
# 建议学习时间：60-90分钟
# 前置知识：第1-4阶段 - 基础知识和面向对象
# 下一课：第6阶段 第1课 - 文件操作 (file_operations.py)
# 本模块介绍Python异常处理机制和自定义异常

# ===== 1. 异常基础 =====

print("=== 异常基础 ===")

# 常见的异常类型
def demonstrate_exceptions():
    """演示常见的异常"""

    examples = [
        ("除零错误", lambda: 5 / 0),
        ("索引越界", lambda: [1, 2, 3][5]),
        ("键不存在", lambda: {"a": 1}["b"]),
        ("类型错误", lambda: "hello" + 5),
        ("值错误", lambda: int("not_a_number")),
        ("文件不存在", lambda: open("nonexistent_file.txt")),
    ]

    for description, func in examples:
        try:
            result = func()
            print(f"{description}: {result}")
        except Exception as e:
            print(f"{description}: {type(e).__name__}: {e}")

demonstrate_exceptions()

# ===== 2. try-except语句 =====

print("\n=== try-except语句 ===")

# 基本try-except
def safe_division(a, b):
    """安全的除法运算"""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "错误：除数不能为0"
    except TypeError:
        return "错误：输入类型不正确"

print(f"正常除法: {safe_division(10, 2)}")
print(f"除零: {safe_division(10, 0)}")
print(f"类型错误: {safe_division(10, 'a')}")

# 捕获多种异常
def multiple_exceptions():
    """捕获多种异常"""

    test_cases = [
        (10, 2, "正常情况"),
        (10, 0, "除零错误"),
        ("10", "2", "类型错误"),
    ]

    for a, b, description in test_cases:
        try:
            result = a / b
            print(f"{description}: {result}")
        except (ZeroDivisionError, TypeError) as e:
            print(f"{description}: {type(e).__name__}: {e}")
        except Exception as e:
            print(f"{description}: 意外错误: {type(e).__name__}: {e}")

multiple_exceptions()

# ===== 3. else和finally语句 =====

print("\n=== else和finally语句 ===")

def file_operations_demo():
    """文件操作演示"""

    def read_file_safely(filename):
        """安全地读取文件"""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
        except FileNotFoundError:
            print(f"文件 '{filename}' 不存在")
            return None
        except PermissionError:
            print(f"没有权限读取文件 '{filename}'")
            return None
        else:
            # 只有在没有异常时才执行
            print(f"成功读取文件，共{len(content)}个字符")
            return content
        finally:
            # 总是执行，不管是否有异常
            print("文件操作完成")

    # 测试文件操作
    result1 = read_file_safely("existing_file.txt")
    result2 = read_file_safely("nonexistent_file.txt")

    return result1, result2

file_operations_demo()

# ===== 4. raise语句 =====

print("\n=== raise语句 ===")

def validate_age(age):
    """验证年龄"""
    if not isinstance(age, (int, float)):
        raise TypeError("年龄必须是数字")

    if age < 0:
        raise ValueError("年龄不能为负数")

    if age > 150:
        raise ValueError("年龄不能超过150岁")

    return True

# 测试年龄验证
test_ages = [25, -5, 200, "25", 80]

for age in test_ages:
    try:
        validate_age(age)
        print(f"年龄 {age} 验证通过")
    except (TypeError, ValueError) as e:
        print(f"年龄 {age} 验证失败: {e}")

# ===== 5. 自定义异常 =====

print("\n=== 自定义异常 ===")

class ValidationError(Exception):
    """验证错误基类"""
    pass

class AgeValidationError(ValidationError):
    """年龄验证错误"""
    def __init__(self, age, message="年龄验证失败"):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: {self.age}"

class InsufficientFundsError(Exception):
    """余额不足错误"""

    def __init__(self, balance, amount, message="余额不足"):
        self.balance = balance
        self.amount = amount
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: 需要{self.amount}, 当前余额{self.balance}"

def validate_user_age(age):
    """验证用户年龄（使用自定义异常）"""
    if not isinstance(age, (int, float)):
        raise ValidationError(f"年龄必须是数字，得到的是 {type(age)}")

    if age < 0:
        raise AgeValidationError(age, "年龄不能为负数")

    if age < 18:
        raise AgeValidationError(age, "年龄必须满18岁")

    if age > 120:
        raise AgeValidationError(age, "年龄不能超过120岁")

    return True

def withdraw_money(balance, amount):
    """取款（使用自定义异常）"""
    if amount > balance:
        raise InsufficientFundsError(balance, amount)

    return balance - amount

# 测试自定义异常
print("年龄验证测试:")
test_ages = [25, 15, -5, "25", 130]

for age in test_ages:
    try:
        validate_user_age(age)
        print(f"年龄 {age} 验证通过")
    except AgeValidationError as e:
        print(f"年龄验证错误: {e}")
    except ValidationError as e:
        print(f"验证错误: {e}")

print("\n取款测试:")
balances = [1000, 500, 100]
withdrawals = [500, 800, 200]

for balance, amount in zip(balances, withdrawals):
    try:
        new_balance = withdraw_money(balance, amount)
        print(f"取款成功: 从{balance}提取{amount}, 剩余{new_balance}")
    except InsufficientFundsError as e:
        print(f"取款失败: {e}")

# ===== 6. 异常链和上下文 =====

print("\n=== 异常链和上下文 ===")

def process_data(data):
    """处理数据（演示异常链）"""
    try:
        # 尝试转换为整数
        number = int(data)
    except ValueError as e:
        # 重新引发异常，并保留原始异常信息
        raise ValueError(f"无法将 '{data}' 转换为整数") from e

def calculate_square_root(n):
    """计算平方根（演示异常上下文）"""
    try:
        if n < 0:
            raise ValueError("不能计算负数的平方根")
        import math
        return math.sqrt(n)
    except ValueError as e:
        raise ValueError(f"计算平方根失败: {n}") from e

# 测试异常链
test_data = ["25", "abc", "-4", "3.14"]

for data in test_data:
    try:
        number = int(data)
        sqrt_result = calculate_square_root(number)
        print(f"数据 '{data}' 的平方根: {sqrt_result}")
    except ValueError as e:
        print(f"处理数据 '{data}' 时出错: {e}")
        # 显示异常链
        if e.__cause__:
            print(f"  原始异常: {e.__cause__}")

# ===== 7. assert语句 =====

print("\n=== assert语句 ===")

def divide_numbers(a, b):
    """除法运算（使用断言）"""
    assert isinstance(a, (int, float)), "被除数必须是数字"
    assert isinstance(b, (int, float)), "除数必须是数字"
    assert b != 0, "除数不能为0"

    return a / b

# 测试断言
test_cases = [
    (10, 2, "正常情况"),
    (10, 0, "除零"),
    ("10", 2, "类型错误"),
    (10, "2", "类型错误"),
]

for a, b, description in test_cases:
    try:
        result = divide_numbers(a, b)
        print(f"{description}: {a} / {b} = {result}")
    except AssertionError as e:
        print(f"{description}: 断言失败 - {e}")
    except ZeroDivisionError as e:
        print(f"{description}: 除零错误 - {e}")

# ===== 8. 异常处理的最佳实践 =====

print("\n=== 异常处理的最佳实践 ===")

# 最佳实践1: 只捕获你能处理的异常
def read_config_file(filename):
    """读取配置文件"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            config = {}
            for line in file:
                if '=' in line:
                    key, value = line.strip().split('=', 1)
                    config[key] = value
            return config
    except FileNotFoundError:
        # 我们能处理这个异常
        print(f"配置文件 '{filename}' 不存在，使用默认配置")
        return {"debug": "false", "max_connections": "10"}
    except PermissionError:
        # 我们能处理这个异常
        print(f"没有权限读取配置文件 '{filename}'")
        return {}
    # 其他异常让上层处理

# 最佳实践2: 使用finally清理资源
class DatabaseConnection:
    """数据库连接示例"""

    def __init__(self):
        self.connected = False

    def connect(self):
        """连接数据库"""
        self.connected = True
        print("数据库连接已建立")

    def disconnect(self):
        """断开连接"""
        if self.connected:
            self.connected = False
            print("数据库连接已断开")

    def execute_query(self, query):
        """执行查询"""
        if not self.connected:
            raise RuntimeError("数据库未连接")

        # 模拟查询执行
        if "error" in query:
            raise RuntimeError("查询执行失败")

        return f"查询结果: {query}"

def execute_database_query(query):
    """执行数据库查询（最佳实践）"""
    db = DatabaseConnection()

    try:
        db.connect()
        result = db.execute_query(query)
        return result
    except RuntimeError as e:
        print(f"数据库操作失败: {e}")
        return None
    finally:
        # 确保连接被断开
        db.disconnect()

# 测试数据库操作
print("数据库操作测试:")
print(execute_database_query("SELECT * FROM users"))
print(execute_database_query("SELECT * FROM error_table"))

# 最佳实践3: 创建有意义的异常层次结构
class ApplicationError(Exception):
    """应用错误基类"""
    pass

class ConfigurationError(ApplicationError):
    """配置错误"""
    pass

class DatabaseError(ApplicationError):
    """数据库错误"""
    pass

class ValidationError(ApplicationError):
    """验证错误"""
    pass

def load_configuration():
    """加载配置（使用异常层次结构）"""
    try:
        # 模拟配置加载
        config = read_config_file("app_config.txt")
        if not config:
            raise ConfigurationError("无法加载配置")
        return config
    except FileNotFoundError:
        raise ConfigurationError("配置文件不存在") from FileNotFoundError

def save_to_database(data):
    """保存到数据库（使用异常层次结构）"""
    try:
        # 模拟数据库操作
        if "invalid" in str(data):
            raise DatabaseError("数据验证失败")
        return execute_database_query(f"INSERT {data}")
    except RuntimeError:
        raise DatabaseError("数据库操作失败") from RuntimeError

# 测试异常层次结构
print("\n异常层次结构测试:")
try:
    config = load_configuration()
    print(f"配置加载成功: {config}")
except ConfigurationError as e:
    print(f"配置错误: {e}")

try:
    result = save_to_database("valid_data")
    print(f"数据库保存成功: {result}")
except DatabaseError as e:
    print(f"数据库错误: {e}")

# ===== 9. 上下文管理器和异常处理 =====

print("\n=== 上下文管理器和异常处理 ===")

class FileManager:
    """文件管理器上下文管理器"""

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        """进入上下文"""
        try:
            self.file = open(self.filename, self.mode, encoding='utf-8')
            return self.file
        except FileNotFoundError:
            raise FileNotFoundError(f"文件 '{self.filename}' 不存在")
        except PermissionError:
            raise PermissionError(f"没有权限访问文件 '{self.filename}'")

    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出上下文"""
        if self.file:
            self.file.close()

        # 如果有异常，记录但不处理
        if exc_type:
            print(f"在处理文件 '{self.filename}' 时发生异常: {exc_type.__name__}")

        # 返回False让异常继续传播
        return False

# 使用自定义上下文管理器
def safe_file_operation():
    """安全的文件操作"""
    try:
        with FileManager("example.txt", "w") as file:
            file.write("Hello, World!\n")
            file.write("This is a test file.\n")

        with FileManager("example.txt", "r") as file:
            content = file.read()
            print(f"文件内容: {content}")

    except (FileNotFoundError, PermissionError) as e:
        print(f"文件操作失败: {e}")

safe_file_operation()

# ===== 练习 =====

print("\n=== 练习时间 ===")

# 练习1: 健壮的计算器
class CalculatorError(Exception):
    """计算器错误基类"""
    pass

class DivisionByZeroError(CalculatorError):
    """除零错误"""
    pass

class InvalidOperationError(CalculatorError):
    """无效操作错误"""
    pass

class Calculator:
    """健壮的计算器"""

    def __init__(self):
        self.history = []

    def add(self, a, b):
        """加法"""
        self._validate_numbers(a, b)
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        """减法"""
        self._validate_numbers(a, b)
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        """乘法"""
        self._validate_numbers(a, b)
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        """除法"""
        self._validate_numbers(a, b)
        if b == 0:
            raise DivisionByZeroError("除数不能为0")

        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def _validate_numbers(self, *numbers):
        """验证输入是否为数字"""
        for num in numbers:
            if not isinstance(num, (int, float)):
                raise InvalidOperationError(f"操作数必须是数字，得到的是 {type(num)}")

    def get_history(self):
        """获取计算历史"""
        return self.history.copy()

# 测试计算器
calc = Calculator()

operations = [
    ("add", 10, 5),
    ("subtract", 10, 3),
    ("multiply", 6, 7),
    ("divide", 15, 3),
    ("divide", 10, 0),  # 除零错误
    ("add", 5, "3"),    # 类型错误
]

print("计算器测试:")
for op, a, b in operations:
    try:
        method = getattr(calc, op)
        result = method(a, b)
        print(f"{op}({a}, {b}) = {result}")
    except CalculatorError as e:
        print(f"{op}({a}, {b}) 失败: {e}")
    except AttributeError:
        print(f"未知操作: {op}")

print(f"\n计算历史: {calc.get_history()}")

# 练习2: 用户注册系统
class RegistrationError(Exception):
    """注册错误基类"""
    pass

class UsernameError(RegistrationError):
    """用户名错误"""
    pass

class PasswordError(RegistrationError):
    """密码错误"""
    pass

class EmailError(RegistrationError):
    """邮箱错误"""
    pass

class UserRegistration:
    """用户注册系统"""

    def __init__(self):
        self.users = {}

    def register_user(self, username, password, email):
        """注册用户"""
        try:
            self._validate_username(username)
            self._validate_password(password)
            self._validate_email(email)

            if username in self.users:
                raise UsernameError("用户名已存在")

            self.users[username] = {
                "password": password,
                "email": email
            }

            return f"用户 '{username}' 注册成功"

        except RegistrationError:
            raise  # 重新引发注册相关的异常

    def _validate_username(self, username):
        """验证用户名"""
        if not username:
            raise UsernameError("用户名不能为空")

        if len(username) < 3:
            raise UsernameError("用户名长度不能少于3个字符")

        if not username.replace('_', '').isalnum():
            raise UsernameError("用户名只能包含字母、数字和下划线")

    def _validate_password(self, password):
        """验证密码"""
        if len(password) < 6:
            raise PasswordError("密码长度不能少于6个字符")

        if not any(c.isupper() for c in password):
            raise PasswordError("密码必须包含至少一个大写字母")

        if not any(c.islower() for c in password):
            raise PasswordError("密码必须包含至少一个小写字母")

        if not any(c.isdigit() for c in password):
            raise PasswordError("密码必须包含至少一个数字")

    def _validate_email(self, email):
        """验证邮箱"""
        import re
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if not re.match(email_pattern, email):
            raise EmailError("邮箱格式不正确")

    def login_user(self, username, password):
        """用户登录"""
        try:
            if username not in self.users:
                raise UsernameError("用户名不存在")

            if self.users[username]["password"] != password:
                raise PasswordError("密码错误")

            return f"用户 '{username}' 登录成功"

        except RegistrationError:
            raise

# 测试用户注册系统
registration = UserRegistration()

test_users = [
    ("user1", "Password123", "user1@example.com"),
    ("us", "pass", "invalid-email"),  # 多个错误
    ("user2", "password", "user2@example.com"),  # 密码不符合要求
    ("user_3", "ValidPass123", "user3@example.com"),  # 正常
]

print("\n用户注册测试:")
for username, password, email in test_users:
    try:
        result = registration.register_user(username, password, email)
        print(f"注册成功: {result}")
    except RegistrationError as e:
        print(f"注册失败: {e}")

# 测试登录
print("\n用户登录测试:")
try:
    result = registration.login_user("user_3", "ValidPass123")
    print(f"登录成功: {result}")
except RegistrationError as e:
    print(f"登录失败: {e}")

try:
    result = registration.login_user("user_3", "wrongpassword")
    print(f"登录成功: {result}")
except RegistrationError as e:
    print(f"登录失败: {e}")

# 练习3: 安全的JSON文件操作
import json
import os

class JSONFileError(Exception):
    """JSON文件错误基类"""
    pass

class JSONFileManager:
    """安全的JSON文件管理器"""

    def __init__(self, filename):
        self.filename = filename

    def save_data(self, data):
        """保存数据到JSON文件"""
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=2)
            return True
        except (IOError, OSError) as e:
            raise JSONFileError(f"保存文件失败: {e}") from e
        except (TypeError, ValueError) as e:
            raise JSONFileError(f"数据序列化失败: {e}") from e

    def load_data(self):
        """从JSON文件加载数据"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            raise JSONFileError(f"文件 '{self.filename}' 不存在") from FileNotFoundError
        except (IOError, OSError) as e:
            raise JSONFileError(f"读取文件失败: {e}") from e
        except (json.JSONDecodeError, ValueError) as e:
            raise JSONFileError(f"JSON解析失败: {e}") from e

    def update_data(self, new_data):
        """更新数据（读取-修改-保存）"""
        try:
            # 读取现有数据
            current_data = self.load_data()

            # 更新数据
            if isinstance(current_data, dict) and isinstance(new_data, dict):
                current_data.update(new_data)
            elif isinstance(current_data, list) and isinstance(new_data, list):
                current_data.extend(new_data)
            else:
                current_data = new_data

            # 保存更新后的数据
            self.save_data(current_data)
            return current_data

        except JSONFileError:
            raise

# 测试JSON文件管理器
json_manager = JSONFileManager("test_data.json")

# 测试保存和加载
test_data = {
    "users": [
        {"name": "张三", "age": 25},
        {"name": "李四", "age": 30}
    ],
    "settings": {
        "theme": "dark",
        "language": "zh-CN"
    }
}

print("\nJSON文件管理器测试:")
try:
    json_manager.save_data(test_data)
    print("数据保存成功")

    loaded_data = json_manager.load_data()
    print("数据加载成功")
    print(f"加载的用户数量: {len(loaded_data['users'])}")

    # 更新数据
    new_user = {"name": "王五", "age": 28}
    updated_data = json_manager.update_data({"users": [new_user]})
    print(f"数据更新成功，当前用户数量: {len(updated_data['users'])}")

except JSONFileError as e:
    print(f"JSON文件操作失败: {e}")

# 清理测试文件
try:
    if os.path.exists("test_data.json"):
        os.remove("test_data.json")
        print("清理了测试文件")
except OSError:
    pass
