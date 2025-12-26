# Python学习项目 - 中级内容：面向对象基础
# 学习序号：第4阶段 第1课 - 面向对象基础
# 建议学习时间：120-150分钟
# 前置知识：第1-3阶段 - 基础语法、数据结构、函数和模块
# 下一课：第5阶段 第1课 - 异常处理 (exception_handling.py)
# 本模块介绍Python面向对象的类和对象概念

# ===== 1. 类和对象的概念 =====

print("=== 类和对象的概念 ===")

# 定义一个简单的类
class Person:
    """人这个类"""

    # 类变量（所有实例共享）
    species = "人类"

    def __init__(self, name, age):
        """初始化方法（构造函数）"""
        # 实例变量（每个实例独有）
        self.name = name
        self.age = age

    def introduce(self):
        """实例方法"""
        return f"我叫{self.name}，今年{self.age}岁。"

    def celebrate_birthday(self):
        """庆祝生日"""
        self.age += 1
        return f"{self.name}生日快乐！现在{self.age}岁了。"

    @classmethod
    def get_species(cls):
        """类方法"""
        return f"我们都是{cls.species}"

    @staticmethod
    def is_adult(age):
        """静态方法"""
        return age >= 18

# 创建对象（实例化）
person1 = Person("张三", 25)
person2 = Person("李四", 30)

print(f"person1介绍: {person1.introduce()}")
print(f"person2介绍: {person2.introduce()}")

# 调用实例方法
print(person1.celebrate_birthday())

# 调用类方法
print(Person.get_species())

# 调用静态方法
print(f"张三是成年人: {Person.is_adult(25)}")
print(f"小孩是成年人: {Person.is_adult(10)}")

# ===== 2. 实例变量和类变量 =====

print("\n=== 实例变量和类变量 ===")

class Student:
    """学生类"""

    # 类变量
    school_name = "Python大学"
    total_students = 0

    def __init__(self, name, student_id):
        # 实例变量
        self.name = name
        self.student_id = student_id
        self.grades = []

        # 修改类变量
        Student.total_students += 1

    def add_grade(self, grade):
        """添加成绩"""
        self.grades.append(grade)

    def get_average(self):
        """计算平均分"""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

# 创建学生实例
student1 = Student("王五", "2021001")
student2 = Student("赵六", "2021002")

student1.add_grade(85)
student1.add_grade(92)
student1.add_grade(78)

student2.add_grade(88)
student2.add_grade(95)

print(f"学校名称: {Student.school_name}")
print(f"总学生数: {Student.total_students}")
print(f"{student1.name}的平均分: {student1.get_average():.1f}")
print(f"{student2.name}的平均分: {student2.get_average():.1f}")

# 修改类变量
Student.school_name = "Python精英大学"
print(f"修改后的学校名称: {Student.school_name}")

# ===== 3. 方法的类型 =====

print("\n=== 方法的类型 ===")

class Calculator:
    """计算器类"""

    # 类变量
    operations_count = 0

    def __init__(self):
        # 实例变量
        self.history = []

    def add(self, a, b):
        """实例方法：加法"""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        Calculator.operations_count += 1
        return result

    @classmethod
    def get_operations_count(cls):
        """类方法：获取操作次数"""
        return f"总共进行了{cls.operations_count}次操作"

    @staticmethod
    def is_number(value):
        """静态方法：检查是否为数字"""
        return isinstance(value, (int, float))

# 使用不同类型的方法
calc = Calculator()

print(f"加法结果: {calc.add(5, 3)}")
print(f"加法结果: {calc.add(10, 7)}")
print(f"操作历史: {calc.history}")

print(Calculator.get_operations_count())
print(f"5是数字: {Calculator.is_number(5)}")
print(f"'hello'是数字: {Calculator.is_number('hello')}")

# ===== 4. 封装和私有属性 =====

print("\n=== 封装和私有属性 ===")

class BankAccount:
    """银行账户类"""

    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.__balance = initial_balance  # 私有属性
        self.__transaction_history = []  # 私有属性

    def deposit(self, amount):
        """存款"""
        if amount > 0:
            self.__balance += amount
            self.__transaction_history.append(f"存款: +{amount}")
            return True
        return False

    def withdraw(self, amount):
        """取款"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__transaction_history.append(f"取款: -{amount}")
            return True
        return False

    def get_balance(self):
        """获取余额"""
        return self.__balance

    def get_transaction_history(self):
        """获取交易历史"""
        return self.__transaction_history.copy()  # 返回副本，保护原始数据

# 使用银行账户
account = BankAccount("张三", 1000)

account.deposit(500)
account.withdraw(200)
account.deposit(100)

print(f"账户持有人: {account.account_holder}")
print(f"当前余额: {account.get_balance()}")
print(f"交易历史: {account.get_transaction_history()}")

# 尝试直接访问私有属性（不推荐）
# print(account.__balance)  # 这会报错
# 但可以通过特殊方式访问（不推荐）
print(f"通过特殊方式访问余额: {account._BankAccount__balance}")

# ===== 5. 属性装饰器 =====

print("\n=== 属性装饰器 ===")

class Temperature:
    """温度类"""

    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        """摄氏度属性"""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """设置摄氏度"""
        if value < -273.15:
            raise ValueError("温度不能低于绝对零度")
        self._celsius = value

    @property
    def fahrenheit(self):
        """华氏度属性（只读）"""
        return self._celsius * 9/5 + 32

    @property
    def kelvin(self):
        """开尔文属性（只读）"""
        return self._celsius + 273.15

# 使用温度类
temp = Temperature(25)

print(f"摄氏度: {temp.celsius}°C")
print(f"华氏度: {temp.fahrenheit}°F")
print(f"开尔文: {temp.kelvin}K")

# 修改温度
temp.celsius = 30
print(f"修改后摄氏度: {temp.celsius}°C")
print(f"对应的华氏度: {temp.fahrenheit}°F")

# 尝试设置无效温度
try:
    temp.celsius = -300
except ValueError as e:
    print(f"错误: {e}")

# ===== 6. 特殊方法（魔术方法） =====

print("\n=== 特殊方法（魔术方法） ===")

class Vector:
    """二维向量类"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """字符串表示"""
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        """官方字符串表示"""
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        """向量加法"""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __mul__(self, scalar):
        """向量乘法"""
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented

    def __eq__(self, other):
        """相等比较"""
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False

    def __len__(self):
        """长度（这里指向量维度）"""
        return 2

    def __getitem__(self, index):
        """索引访问"""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("向量只有x和y两个分量")

# 使用向量类
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"向量1: {v1}")
print(f"向量2: {v2}")
print(f"向量相加: {v1 + v2}")
print(f"向量乘以2: {v1 * 2}")
print(f"向量相等: {v1 == v2}")
print(f"向量长度: {len(v1)}")
print(f"向量x分量: {v1[0]}, y分量: {v1[1]}")

# ===== 7. 类继承 =====

print("\n=== 类继承 ===")

class Animal:
    """动物基类"""

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        """发出声音"""
        return "一些声音"

    def eat(self, food):
        """进食"""
        return f"{self.name}正在吃{food}"

    def sleep(self):
        """睡觉"""
        return f"{self.name}正在睡觉"

class Dog(Animal):
    """狗类"""

    def __init__(self, name, breed):
        super().__init__(name, "狗")
        self.breed = breed

    def make_sound(self):
        """狗叫"""
        return "汪汪!"

    def fetch(self, item):
        """捡东西"""
        return f"{self.name}捡回了{item}"

class Cat(Animal):
    """猫类"""

    def __init__(self, name, color):
        super().__init__(name, "猫")
        self.color = color

    def make_sound(self):
        """猫叫"""
        return "喵喵!"

    def climb(self, place):
        """爬高"""
        return f"{self.name}爬上了{place}"

# 使用继承的类
dog = Dog("旺财", "金毛")
cat = Cat("咪咪", "橘色")

print(f"狗: {dog.name} ({dog.species}, {dog.breed})")
print(f"狗叫: {dog.make_sound()}")
print(f"狗捡东西: {dog.fetch('球')}")
print(f"狗睡觉: {dog.sleep()}")

print(f"\n猫: {cat.name} ({cat.species}, {cat.color})")
print(f"猫叫: {cat.make_sound()}")
print(f"猫爬高: {cat.climb('树')}")
print(f"猫吃饭: {cat.eat('鱼')}")

# ===== 8. 多态 =====

print("\n=== 多态 ===")

def animal_sounds(animals):
    """让所有动物发出声音"""
    for animal in animals:
        print(f"{animal.name}: {animal.make_sound()}")

# 创建不同类型的动物
animals = [
    Dog("旺财", "金毛"),
    Cat("咪咪", "橘色"),
    Dog("小白", "哈士奇"),
    Cat("小黑", "黑色")
]

animal_sounds(animals)

# ===== 9. 方法重载和运算符重载 =====

print("\n=== 方法重载和运算符重载 ===")

class Point:
    """点类"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        """点加法"""
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        """点减法"""
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __eq__(self, other):
        """相等比较"""
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def distance_from_origin(self):
        """计算到原点的距离"""
        return (self.x ** 2 + self.y ** 2) ** 0.5

# 使用点类
p1 = Point(3, 4)
p2 = Point(1, 2)

print(f"点1: {p1}")
print(f"点2: {p2}")
print(f"点相加: {p1 + p2}")
print(f"点相减: {p1 - p2}")
print(f"点相等: {p1 == p2}")
print(f"点到原点距离: {p1.distance_from_origin():.2f}")

# ===== 练习 =====

print("\n=== 练习时间 ===")

# 练习1: 创建一个简单的银行系统
class BankAccount:
    """银行账户"""

    # 类变量
    bank_name = "Python银行"
    total_accounts = 0
    total_balance = 0

    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.__balance = initial_balance
        self.__transactions = []

        BankAccount.total_accounts += 1
        BankAccount.total_balance += initial_balance

    def deposit(self, amount):
        """存款"""
        if amount > 0:
            self.__balance += amount
            self.__transactions.append(f"存款: +{amount}")
            BankAccount.total_balance += amount
            return True
        return False

    def withdraw(self, amount):
        """取款"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__transactions.append(f"取款: -{amount}")
            BankAccount.total_balance -= amount
            return True
        return False

    def get_balance(self):
        """获取余额"""
        return self.__balance

    def get_transaction_history(self):
        """获取交易历史"""
        return self.__transactions.copy()

    @classmethod
    def get_bank_info(cls):
        """获取银行信息"""
        return f"{cls.bank_name}: {cls.total_accounts}个账户, 总余额{cls.total_balance}"

    @staticmethod
    def validate_amount(amount):
        """验证金额"""
        return isinstance(amount, (int, float)) and amount > 0

# 测试银行系统
account1 = BankAccount("张三", 1000)
account2 = BankAccount("李四", 2000)

account1.deposit(500)
account2.withdraw(300)
account1.deposit(200)

print("银行系统测试:")
print(BankAccount.get_bank_info())
print(f"张三余额: {account1.get_balance()}")
print(f"李四余额: {account2.get_balance()}")
print(f"张三交易记录: {account1.get_transaction_history()}")

# 练习2: 几何形状层次结构
class Shape:
    """形状基类"""

    def area(self):
        """计算面积"""
        raise NotImplementedError("子类必须实现area方法")

    def perimeter(self):
        """计算周长"""
        raise NotImplementedError("子类必须实现perimeter方法")

class Rectangle(Shape):
    """矩形"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle({self.width} x {self.height})"

class Circle(Shape):
    """圆形"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Circle(radius={self.radius})"

# 测试形状类
shapes = [
    Rectangle(5, 3),
    Circle(4),
    Rectangle(10, 8),
    Circle(2.5)
]

print("\n几何形状测试:")
for shape in shapes:
    print(f"{shape}: 面积={shape.area():.2f}, 周长={shape.perimeter():.2f}")

# 练习3: 员工管理系统
class Employee:
    """员工基类"""

    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def get_info(self):
        """获取员工信息"""
        return f"员工ID: {self.employee_id}, 姓名: {self.name}, 薪资: {self.salary}"

    def calculate_bonus(self):
        """计算奖金（基类方法）"""
        return self.salary * 0.1

class Manager(Employee):
    """经理"""

    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id, salary)
        self.department = department

    def calculate_bonus(self):
        """经理奖金计算（更高的奖金）"""
        return self.salary * 0.2

    def get_info(self):
        """获取经理信息"""
        base_info = super().get_info()
        return f"{base_info}, 部门: {self.department}"

class Developer(Employee):
    """开发人员"""

    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id, salary)
        self.programming_language = programming_language

    def get_info(self):
        """获取开发人员信息"""
        base_info = super().get_info()
        return f"{base_info}, 编程语言: {self.programming_language}"

# 测试员工系统
employees = [
    Manager("张三", "M001", 10000, "技术部"),
    Developer("李四", "D001", 8000, "Python"),
    Manager("王五", "M002", 12000, "销售部"),
    Developer("赵六", "D002", 7500, "JavaScript")
]

print("\n员工管理系统:")
total_bonus = 0
for employee in employees:
    print(employee.get_info())
    bonus = employee.calculate_bonus()
    total_bonus += bonus
    print(f"  奖金: {bonus}")

print(f"\n总奖金支出: {total_bonus}")

# 练习4: 图书管理系统
class Book:
    """图书类"""

    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def __str__(self):
        status = "可借" if self.available else "已借出"
        return f"'{self.title}' by {self.author} [{status}]"

class Library:
    """图书馆类"""

    def __init__(self, name):
        self.name = name
        self.books = {}

    def add_book(self, book):
        """添加图书"""
        self.books[book.isbn] = book

    def borrow_book(self, isbn):
        """借书"""
        if isbn in self.books and self.books[isbn].available:
            self.books[isbn].available = False
            return f"成功借出: {self.books[isbn].title}"
        return "图书不可借"

    def return_book(self, isbn):
        """还书"""
        if isbn in self.books and not self.books[isbn].available:
            self.books[isbn].available = True
            return f"成功归还: {self.books[isbn].title}"
        return "归还失败"

    def list_books(self):
        """列出所有图书"""
        return list(self.books.values())

# 测试图书馆系统
library = Library("Python图书馆")

# 添加图书
books = [
    Book("Python编程", "张三", "ISBN001"),
    Book("数据结构", "李四", "ISBN002"),
    Book("算法导论", "王五", "ISBN003")
]

for book in books:
    library.add_book(book)

print("\n图书馆系统:")
print("所有图书:")
for book in library.list_books():
    print(f"  {book}")

print(f"\n借书: {library.borrow_book('ISBN001')}")
print(f"借书: {library.borrow_book('ISBN001')}")  # 再次借同一本书

print(f"还书: {library.return_book('ISBN001')}")

print("\n更新后的图书状态:")
for book in library.list_books():
    print(f"  {book}")
