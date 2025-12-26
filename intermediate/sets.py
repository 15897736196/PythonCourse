# Python学习项目 - 中级内容：集合
# 学习序号：第2阶段 第3课 - 集合
# 建议学习时间：45-60分钟
# 前置知识：第2阶段 第1-2课 - 列表、元组和字典
# 下一课：第2阶段 第4课 - 字符串操作 (strings.py)
# 本模块介绍Python中的集合数据结构

# ===== 1. 集合基础 =====

print("=== 集合(Set)基础 ===")

# 创建集合
empty_set = set()
fruits = {"苹果", "香蕉", "橙子"}
numbers = set([1, 2, 3, 4, 5])  # 从列表创建
mixed = {1, "hello", 3.14, True}

print(f"空集合: {empty_set}")
print(f"水果集合: {fruits}")
print(f"数字集合: {numbers}")
print(f"混合集合: {mixed}")

# 注意：集合是无序的，True和1被认为是相同的
print(f"注意True和1: {{1, True}} = { {1, True} }")

# ===== 2. 集合操作 =====

print("\n=== 集合操作 ===")

# 添加元素
fruits = {"苹果", "香蕉"}
fruits.add("橙子")
print(f"添加元素后: {fruits}")

# 添加多个元素
fruits.update(["葡萄", "西瓜"])
print(f"更新多个元素后: {fruits}")

# 删除元素
fruits.remove("香蕉")  # 如果元素不存在会报错
print(f"删除'香蕉'后: {fruits}")

fruits.discard("樱桃")  # 如果元素不存在不会报错
print(f"尝试删除不存在的元素: {fruits}")

# 随机删除一个元素
if fruits:
    removed = fruits.pop()
    print(f"随机弹出: {removed}, 剩余: {fruits}")

# 清空集合
temp_set = {1, 2, 3}
temp_set.clear()
print(f"清空集合: {temp_set}")

# ===== 3. 集合运算 =====

print("\n=== 集合运算 ===")

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"集合A: {set_a}")
print(f"集合B: {set_b}")

# 并集
print(f"A ∪ B (并集): {set_a | set_b}")
print(f"A.union(B): {set_a.union(set_b)}")

# 交集
print(f"A ∩ B (交集): {set_a & set_b}")
print(f"A.intersection(B): {set_a.intersection(set_b)}")

# 差集
print(f"A - B (差集): {set_a - set_b}")
print(f"A.difference(B): {set_a.difference(set_b)}")

print(f"B - A (差集): {set_b - set_a}")

# 对称差集（异或）
print(f"A △ B (对称差集): {set_a ^ set_b}")
print(f"A.symmetric_difference(B): {set_a.symmetric_difference(set_b)}")

# ===== 4. 集合关系判断 =====

print("\n=== 集合关系判断 ===")

set_x = {1, 2, 3}
set_y = {1, 2, 3, 4, 5}
set_z = {3, 4, 5}

print(f"X: {set_x}")
print(f"Y: {set_y}")
print(f"Z: {set_z}")

# 子集判断
print(f"X ⊆ Y (X是Y的子集): {set_x.issubset(set_y)}")
print(f"Y ⊆ X (Y是X的子集): {set_y.issubset(set_x)}")

# 超集判断
print(f"Y ⊇ X (Y是X的超集): {set_y.issuperset(set_x)}")
print(f"X ⊇ Y (X是Y的超集): {set_x.issuperset(set_y)}")

# 相等判断
print(f"X == Y: {set_x == set_y}")

# 不相交判断
print(f"X和Z不相交: {set_x.isdisjoint(set_z)}")

# ===== 5. 集合推导式 =====

print("\n=== 集合推导式 ===")

# 基本集合推导式
squares = {x**2 for x in range(1, 6)}
print(f"平方数集合: {squares}")

# 条件集合推导式
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(f"偶数平方集合: {even_squares}")

# 从字符串创建集合
vowels = {char for char in "hello world" if char in "aeiou"}
print(f"元音字母集合: {vowels}")

# ===== 6. 冻结集合(frozenset) =====

print("\n=== 冻结集合(frozenset) ===")

# 创建冻结集合
normal_set = {1, 2, 3}
frozen_set = frozenset([1, 2, 3])

print(f"普通集合: {normal_set}, 类型: {type(normal_set)}")
print(f"冻结集合: {frozen_set}, 类型: {type(frozen_set)}")

# 冻结集合是不可变的
# frozen_set.add(4)  # 这会报错

# 但是可以进行集合运算
another_frozen = frozenset([3, 4, 5])
print(f"冻结集合并集: {frozen_set | another_frozen}")

# 冻结集合可以作为字典的键
my_dict = {frozen_set: "这是一个冻结集合"}
print(f"使用冻结集合作为键: {my_dict}")

# ===== 7. 集合的应用场景 =====

print("\n=== 集合的应用场景 ===")

# 场景1: 去重
print("去重应用:")
original_list = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique_list = list(set(original_list))
print(f"原列表: {original_list}")
print(f"去重后: {unique_list}")

# 场景2: 查找共同元素
print("\n查找共同爱好:")
person1_hobbies = {"阅读", "编程", "旅行", "音乐"}
person2_hobbies = {"阅读", "摄影", "音乐", "烹饪"}
person3_hobbies = {"阅读", "音乐", "运动"}

common_hobbies = person1_hobbies & person2_hobbies & person3_hobbies
print(f"共同爱好: {common_hobbies}")

# 场景3: 检查成员资格
print("\n权限检查:")
user_permissions = {"read", "write"}
required_permissions = {"read", "admin"}

has_permission = required_permissions.issubset(user_permissions)
print(f"用户权限: {user_permissions}")
print(f"需要权限: {required_permissions}")
print(f"是否有权限: {has_permission}")

# 场景4: 数据筛选
print("\n数据筛选:")
all_students = {"Alice", "Bob", "Charlie", "David", "Eve"}
passed_students = {"Alice", "Charlie", "Eve"}
failed_students = all_students - passed_students

print(f"所有学生: {all_students}")
print(f"及格学生: {passed_students}")
print(f"不及格学生: {failed_students}")

# ===== 8. 集合的高级操作 =====

print("\n=== 集合的高级操作 ===")

# update操作（原地修改）
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(f"原set1: {set1}")
set1.update(set2)  # 等价于 set1 |= set2
print(f"update后: {set1}")

# 其他原地操作
set_a = {1, 2, 3}
set_b = {2, 3, 4}

set_a.intersection_update(set_b)  # 保留交集
print(f"intersection_update: {set_a}")

set_a = {1, 2, 3}
set_a.difference_update(set_b)  # 删除交集部分
print(f"difference_update: {set_a}")

set_a = {1, 2, 3}
set_a.symmetric_difference_update(set_b)  # 对称差集更新
print(f"symmetric_difference_update: {set_a}")

# ===== 9. 集合与列表的转换 =====

print("\n=== 集合与列表的转换 ===")

# 列表去重并保持顺序（Python 3.7+）
def remove_duplicates_keep_order(items):
    """去重并保持顺序"""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

original = [1, 3, 2, 1, 4, 2, 3, 5]
deduplicated = remove_duplicates_keep_order(original)
print(f"原列表: {original}")
print(f"去重保持顺序: {deduplicated}")

# ===== 10. 集合的性能特点 =====

print("\n=== 集合的性能特点 ===")

import time

# 测试成员资格检查性能
large_list = list(range(10000))
large_set = set(range(10000))

# 列表查找
start = time.time()
for _ in range(1000):
    9999 in large_list
list_time = time.time() - start

# 集合查找
start = time.time()
for _ in range(1000):
    9999 in large_set
set_time = time.time() - start

print(".4f")
print(".4f")
print(".1f")

# ===== 练习 =====

print("\n=== 练习时间 ===")

# 练习1: 集合运算演示
def set_operations_demo():
    """集合运算综合演示"""
    programmers = {"Alice", "Bob", "Charlie", "David"}
    designers = {"Eve", "Frank", "Charlie", "Grace"}
    managers = {"Henry", "Alice", "Grace"}

    print("团队成员:")
    print(f"程序员: {programmers}")
    print(f"设计师: {designers}")
    print(f"经理: {managers}")

    # 所有员工
    all_employees = programmers | designers | managers
    print(f"\n所有员工: {all_employees}")

    # 全能员工（三种角色都有）
    versatile = programmers & designers & managers
    print(f"全能员工: {versatile}")

    # 只做程序员的
    only_programmers = programmers - designers - managers
    print(f"专职程序员: {only_programmers}")

    # 设计师或经理，但不是程序员
    design_or_manage_not_dev = (designers | managers) - programmers
    print(f"设计师或经理（非程序员）: {design_or_manage_not_dev}")

# 练习2: 文本分析
def text_analysis():
    """文本分析示例"""
    text1 = "Python is a programming language"
    text2 = "Java is also a programming language"

    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())

    print(f"文本1单词: {words1}")
    print(f"文本2单词: {words2}")

    # 共同单词
    common_words = words1 & words2
    print(f"共同单词: {common_words}")

    # 独特单词
    unique_to_text1 = words1 - words2
    unique_to_text2 = words2 - words1
    print(f"文本1独特单词: {unique_to_text1}")
    print(f"文本2独特单词: {unique_to_text2}")

    # 所有单词
    all_words = words1 | words2
    print(f"所有单词: {all_words}")

# 练习3: 权限管理系统
def permission_system():
    """权限管理系统"""
    users_permissions = {
        "admin": {"read", "write", "delete", "admin"},
        "editor": {"read", "write"},
        "viewer": {"read"}
    }

    def check_permission(user_role, required_permission):
        """检查用户是否有指定权限"""
        user_perms = users_permissions.get(user_role, set())
        return required_permission in user_perms

    def get_user_roles_with_permission(permission):
        """获取拥有指定权限的所有角色"""
        return [role for role, perms in users_permissions.items()
                if permission in perms]

    # 测试权限检查
    print("权限检查:")
    print(f"admin有write权限: {check_permission('admin', 'write')}")
    print(f"viewer有delete权限: {check_permission('viewer', 'delete')}")

    # 获取有write权限的角色
    write_roles = get_user_roles_with_permission("write")
    print(f"有write权限的角色: {write_roles}")

# 练习4: 数据去重和统计
def data_processing():
    """数据处理示例"""
    # 模拟销售记录
    sales_records = [
        {"customer": "A", "product": "苹果"},
        {"customer": "B", "product": "香蕉"},
        {"customer": "A", "product": "苹果"},  # 重复记录
        {"customer": "C", "product": "橙子"},
        {"customer": "B", "product": "苹果"},
        {"customer": "A", "product": "香蕉"},
    ]

    # 去重
    unique_records = []
    seen = set()
    for record in sales_records:
        key = (record["customer"], record["product"])
        if key not in seen:
            seen.add(key)
            unique_records.append(record)

    print("去重后的销售记录:")
    for record in unique_records:
        print(f"  {record['customer']} 购买了 {record['product']}")

    # 统计每个顾客购买的产品种类数
    customer_products = {}
    for record in unique_records:
        customer = record["customer"]
        product = record["product"]
        if customer not in customer_products:
            customer_products[customer] = set()
        customer_products[customer].add(product)

    print("\n顾客购买的产品统计:")
    for customer, products in customer_products.items():
        print(f"  {customer}: {len(products)}种产品 {products}")

# 运行练习
print("练习1: 集合运算演示")
set_operations_demo()

print("\n练习2: 文本分析")
text_analysis()

print("\n练习3: 权限管理系统")
permission_system()

print("\n练习4: 数据处理")
data_processing()
