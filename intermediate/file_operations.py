# Python学习项目 - 中级内容：文件操作
# 学习序号：第6阶段 第1课 - 文件操作
# 建议学习时间：90-120分钟
# 前置知识：第1-5阶段 - 基础语法到异常处理
# 下一课：第6阶段 第2课 - 标准库精选 (standard_library.py)
# 本模块介绍Python文件操作的核心概念和实际应用

"""
文件操作是Python编程中的重要内容，涉及：
1. 文件的打开、读取、写入和关闭
2. 文本文件和二进制文件
3. 目录操作和文件管理
4. 路径处理
5. CSV和JSON文件处理
6. 文件权限和属性
7. 临时文件
8. 高级文件操作技巧
"""

import os
import shutil
import tempfile
import csv
import json
import pathlib
from datetime import datetime
from typing import List, Dict, Any, Optional, Union

# ===== 1. 文件基础操作 =====

print("=== 文件基础操作 ===")

# 文件打开模式
print("文件打开模式:")
print("  'r'  - 读取（默认）")
print("  'w'  - 写入（覆盖）")
print("  'a'  - 追加")
print("  'x'  - 独占创建")
print("  'b'  - 二进制模式")
print("  't'  - 文本模式（默认）")
print("  '+'  - 读写模式")

# ===== 2. 文本文件操作 =====

print("\n=== 文本文件操作 ===")

# 创建示例文本文件
sample_text = """Python文件操作示例

这是第一段文本。
包含多行内容。

第二段：
- 项目1
- 项目2
- 项目3

结束语：文件操作很重要！
"""

# 写入文件
print("写入文本文件:")
with open('python_learning/utils/sample.txt', 'w', encoding='utf-8') as file:
    file.write(sample_text)
    print("  文件已创建并写入内容")

# 读取文件 - 多种方式
print("\n读取文本文件:")

# 方式1: read() - 读取全部内容
with open('python_learning/utils/sample.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(f"  read() - 总字符数: {len(content)}")

# 方式2: readline() - 读取一行
with open('python_learning/utils/sample.txt', 'r', encoding='utf-8') as file:
    first_line = file.readline().strip()
    second_line = file.readline().strip()
    print(f"  readline() - 第一行: '{first_line}'")
    print(f"  readline() - 第二行: '{second_line}'")

# 方式3: readlines() - 读取所有行
with open('python_learning/utils/sample.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    print(f"  readlines() - 总行数: {len(lines)}")
    print(f"  readlines() - 第一行内容: '{lines[0].strip()}'")

# 方式4: 逐行迭代
print("  逐行迭代:")
with open('python_learning/utils/sample.txt', 'r', encoding='utf-8') as file:
    for i, line in enumerate(file, 1):
        print(f"    第{i}行: {line.strip()}")

# ===== 3. 文件指针和定位 =====

print("\n=== 文件指针和定位 ===")

with open('python_learning/utils/sample.txt', 'r', encoding='utf-8') as file:
    # 查看当前位置
    print(f"初始位置: {file.tell()}")

    # 读取一些内容
    content = file.read(10)
    print(f"读取10个字符: '{content}'")
    print(f"当前位置: {file.tell()}")

    # 移动到指定位置
    file.seek(0)  # 移动到文件开头
    print(f"seek(0)后位置: {file.tell()}")

    file.seek(5)  # 移动到第5个字节
    print(f"seek(5)后位置: {file.tell()}")

    content = file.read(10)
    print(f"从位置5读取10个字符: '{content}'")

# ===== 4. 追加和修改文件 =====

print("\n=== 追加和修改文件 ===")

# 追加内容
with open('python_learning/utils/sample.txt', 'a', encoding='utf-8') as file:
    file.write("\n\n追加的内容：\n")
    file.write("这是新添加的行。\n")
    file.write(f"添加时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

print("内容已追加到文件")

# ===== 5. 二进制文件操作 =====

print("\n=== 二进制文件操作 ===")

# 写入二进制数据
binary_data = bytes(range(256))  # 0-255的字节

with open('python_learning/utils/binary_sample.bin', 'wb') as file:
    file.write(binary_data)
    print("二进制文件已创建")

# 读取二进制数据
with open('python_learning/utils/binary_sample.bin', 'rb') as file:
    # 读取前16个字节
    first_16 = file.read(16)
    print(f"前16个字节: {list(first_16)}")

    # 读取剩余内容
    rest = file.read()
    print(f"剩余字节数: {len(rest)}")

# ===== 6. 目录操作 =====

print("\n=== 目录操作 ===")

# 创建目录
test_dir = 'python_learning/utils/test_directory'
sub_dir = os.path.join(test_dir, 'subdir')

try:
    os.makedirs(sub_dir, exist_ok=True)
    print(f"目录已创建: {sub_dir}")
except OSError as e:
    print(f"创建目录失败: {e}")

# 列出目录内容
print(f"\n{test_dir} 目录内容:")
try:
    contents = os.listdir(test_dir)
    for item in contents:
        full_path = os.path.join(test_dir, item)
        if os.path.isdir(full_path):
            print(f"  📁 {item}/")
        else:
            print(f"  📄 {item}")
except OSError as e:
    print(f"读取目录失败: {e}")

# ===== 7. 文件和目录管理 =====

print("\n=== 文件和目录管理 ===")

# 文件重命名
old_name = 'python_learning/utils/sample.txt'
new_name = 'python_learning/utils/renamed_sample.txt'

try:
    os.rename(old_name, new_name)
    print(f"文件已重命名: {old_name} -> {new_name}")
except OSError as e:
    print(f"重命名失败: {e}")

# 文件删除
try:
    os.remove('python_learning/utils/binary_sample.bin')
    print("二进制文件已删除")
except OSError as e:
    print(f"删除失败: {e}")

# 递归删除目录
try:
    shutil.rmtree(test_dir)
    print(f"目录已递归删除: {test_dir}")
except OSError as e:
    print(f"删除目录失败: {e}")

# ===== 8. 路径处理 =====

print("\n=== 路径处理 ===")

# 当前工作目录
current_dir = os.getcwd()
print(f"当前工作目录: {current_dir}")

# 路径拼接
path1 = os.path.join('python_learning', 'utils', 'test.txt')
print(f"路径拼接: {path1}")

# 路径分割
dirname, basename = os.path.split(path1)
print(f"路径分割 - 目录: {dirname}, 文件名: {basename}")

# 文件扩展名
name, ext = os.path.splitext(basename)
print(f"文件名: {name}, 扩展名: {ext}")

# 判断路径类型
test_paths = [
    'python_learning/utils',
    new_name,
    'nonexistent_file.txt'
]

for path in test_paths:
    print(f"路径: {path}")
    print(f"  存在: {os.path.exists(path)}")
    print(f"  是文件: {os.path.isfile(path)}")
    print(f"  是目录: {os.path.isdir(path)}")
    if os.path.exists(path):
        print(f"  大小: {os.path.getsize(path)} bytes")
        print(f"  修改时间: {datetime.fromtimestamp(os.path.getmtime(path))}")

# ===== 9. pathlib模块 =====

print("\n=== pathlib模块（现代路径处理） ===")

from pathlib import Path

# 创建Path对象
project_root = Path('python_learning')
utils_dir = project_root / 'utils'

print(f"项目根目录: {project_root}")
print(f"工具目录: {utils_dir}")

# 路径操作
print(f"工具目录存在: {utils_dir.exists()}")
print(f"工具目录是目录: {utils_dir.is_dir()}")

# 列出目录内容
if utils_dir.exists():
    print("工具目录内容:")
    for item in utils_dir.iterdir():
        if item.is_file():
            print(f"  📄 {item.name} ({item.stat().st_size} bytes)")
        elif item.is_dir():
            print(f"  📁 {item.name}/")

# 文件匹配
txt_files = list(utils_dir.glob('*.txt'))
print(f"找到的文本文件: {[f.name for f in txt_files]}")

# ===== 10. CSV文件处理 =====

print("\n=== CSV文件处理 ===")

# 准备CSV数据
csv_data = [
    ['姓名', '年龄', '城市', '职业'],
    ['张三', 25, '北京', '工程师'],
    ['李四', 30, '上海', '设计师'],
    ['王五', 28, '广州', '教师'],
    ['赵六', 35, '深圳', '经理']
]

# 写入CSV文件
csv_filename = 'python_learning/utils/sample_data.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(csv_data)
    print("CSV文件已创建")

# 读取CSV文件
print("读取CSV文件:")
with open(csv_filename, 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i == 0:
            print(f"表头: {row}")
        else:
            print(f"记录{i}: {row}")

# 使用DictReader进行字典式读取
print("\n字典式读取CSV:")
with open(csv_filename, 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(f"  {row['姓名']}: {row['年龄']}岁, {row['城市']}, {row['职业']}")

# ===== 11. JSON文件处理 =====

print("\n=== JSON文件处理 ===")

# 准备JSON数据
json_data = {
    "company": "Python学习公司",
    "employees": [
        {
            "name": "张三",
            "age": 25,
            "department": "工程部",
            "skills": ["Python", "JavaScript", "SQL"],
            "salary": 8000
        },
        {
            "name": "李四",
            "age": 30,
            "department": "设计部",
            "skills": ["Photoshop", "Illustrator", "Sketch"],
            "salary": 7000
        }
    ],
    "projects": {
        "current": ["网站重构", "移动应用开发"],
        "completed": ["电商平台", "数据可视化工具"]
    },
    "metadata": {
        "created": datetime.now().isoformat(),
        "version": "1.0"
    }
}

# 写入JSON文件
json_filename = 'python_learning/utils/sample_data.json'
with open(json_filename, 'w', encoding='utf-8') as jsonfile:
    json.dump(json_data, jsonfile, ensure_ascii=False, indent=2)
    print("JSON文件已创建")

# 读取JSON文件
print("读取JSON文件:")
with open(json_filename, 'r', encoding='utf-8') as jsonfile:
    loaded_data = json.load(jsonfile)

print(f"公司名称: {loaded_data['company']}")
print(f"员工数量: {len(loaded_data['employees'])}")
print(f"当前项目: {loaded_data['projects']['current']}")

# ===== 12. 临时文件 =====

print("\n=== 临时文件 ===")

# 使用tempfile模块创建临时文件
with tempfile.NamedTemporaryFile(mode='w+', suffix='.txt', delete=False) as temp_file:
    temp_file.write("这是临时文件内容\n")
    temp_file.write("它会在程序结束后被清理\n")
    temp_filename = temp_file.name
    print(f"临时文件已创建: {temp_filename}")

# 读取临时文件内容
with open(temp_filename, 'r') as temp_file:
    content = temp_file.read()
    print(f"临时文件内容:\n{content}")

# 手动删除临时文件
os.unlink(temp_filename)
print("临时文件已手动删除")

# 临时目录
with tempfile.TemporaryDirectory() as temp_dir:
    print(f"临时目录已创建: {temp_dir}")

    # 在临时目录中创建文件
    temp_file_path = os.path.join(temp_dir, 'temp_data.txt')
    with open(temp_file_path, 'w') as f:
        f.write("临时目录中的文件")

    print(f"临时目录内容: {os.listdir(temp_dir)}")

print("临时目录已自动清理")

# ===== 13. 文件权限和属性 =====

print("\n=== 文件权限和属性 ===")

# 检查文件权限
test_file = new_name  # 使用之前重命名的文件
if os.path.exists(test_file):
    # 文件状态信息
    stat_info = os.stat(test_file)
    print(f"文件: {test_file}")
    print(f"  大小: {stat_info.st_size} bytes")
    print(f"  修改时间: {datetime.fromtimestamp(stat_info.st_mtime)}")
    print(f"  访问时间: {datetime.fromtimestamp(stat_info.st_atime)}")
    print(f"  创建时间: {datetime.fromtimestamp(stat_info.st_ctime)}")

    # 权限检查
    print(f"  可读: {os.access(test_file, os.R_OK)}")
    print(f"  可写: {os.access(test_file, os.W_OK)}")
    print(f"  可执行: {os.access(test_file, os.X_OK)}")

# ===== 14. 高级文件操作技巧 =====

print("\n=== 高级文件操作技巧 ===")

# 文件备份
def backup_file(filename):
    """创建文件备份"""
    if not os.path.exists(filename):
        return False

    backup_name = filename + '.backup'
    shutil.copy2(filename, backup_name)
    print(f"备份已创建: {backup_name}")
    return True

# 文件合并
def merge_files(output_file, *input_files):
    """合并多个文件"""
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for input_file in input_files:
            if os.path.exists(input_file):
                with open(input_file, 'r', encoding='utf-8') as infile:
                    outfile.write(f"=== {os.path.basename(input_file)} ===\n")
                    outfile.write(infile.read())
                    outfile.write("\n\n")
                print(f"已合并: {input_file}")

# 文件查找
def find_files(directory, extension=None, name_pattern=None):
    """查找文件"""
    matches = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if extension and not file.endswith(extension):
                continue
            if name_pattern and name_pattern not in file:
                continue
            matches.append(os.path.join(root, file))
    return matches

# ===== 15. 文件操作安全性和最佳实践 =====

print("\n=== 文件操作安全性和最佳实践 ===")

# 安全的文件打开方式
def safe_file_operation(filename, operation):
    """安全的文件操作"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return operation(file)
    except FileNotFoundError:
        print(f"文件不存在: {filename}")
        return None
    except PermissionError:
        print(f"权限不足: {filename}")
        return None
    except UnicodeDecodeError:
        print(f"编码错误，尝试其他编码: {filename}")
        try:
            with open(filename, 'r', encoding='gbk') as file:
                return operation(file)
        except UnicodeDecodeError:
            print(f"无法解码文件: {filename}")
            return None
    except Exception as e:
        print(f"文件操作错误: {e}")
        return None

# 使用安全文件操作
def count_words(file_obj):
    """统计单词数"""
    content = file_obj.read()
    return len(content.split())

word_count = safe_file_operation(new_name, count_words)
if word_count is not None:
    print(f"文件单词数: {word_count}")

# ===== 练习 =====

print("\n=== 练习时间 ===")

# 练习1: 文件内容分析器
def file_analyzer(filename):
    """文件内容分析器"""
    if not os.path.exists(filename):
        return f"文件不存在: {filename}"

    stats = {
        'lines': 0,
        'words': 0,
        'characters': 0,
        'size': os.path.getsize(filename)
    }

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            stats['lines'] += 1
            stats['characters'] += len(line)
            stats['words'] += len(line.split())

    return stats

# 测试文件分析器
analyzer_result = file_analyzer(new_name)
if isinstance(analyzer_result, dict):
    print("文件分析结果:")
    print(f"  行数: {analyzer_result['lines']}")
    print(f"  单词数: {analyzer_result['words']}")
    print(f"  字符数: {analyzer_result['characters']}")
    print(f"  文件大小: {analyzer_result['size']} bytes")
else:
    print(analyzer_result)

# 练习2: 批量文件重命名
def batch_rename(directory, old_pattern, new_pattern):
    """批量重命名文件"""
    if not os.path.exists(directory):
        return f"目录不存在: {directory}"

    renamed_count = 0
    for filename in os.listdir(directory):
        if old_pattern in filename:
            old_path = os.path.join(directory, filename)
            new_filename = filename.replace(old_pattern, new_pattern)
            new_path = os.path.join(directory, new_filename)

            try:
                os.rename(old_path, new_path)
                print(f"已重命名: {filename} -> {new_filename}")
                renamed_count += 1
            except OSError as e:
                print(f"重命名失败 {filename}: {e}")

    return f"共重命名了 {renamed_count} 个文件"

# 练习3: 目录树结构查看器
def print_directory_tree(directory, indent=0):
    """打印目录树结构"""
    if not os.path.exists(directory):
        print(f"目录不存在: {directory}")
        return

    prefix = "  " * indent
    print(f"{prefix}📁 {os.path.basename(directory)}/")

    try:
        items = sorted(os.listdir(directory))
        for item in items:
            item_path = os.path.join(directory, item)
            if os.path.isdir(item_path):
                print_directory_tree(item_path, indent + 1)
            else:
                print(f"{prefix}  📄 {item}")
    except PermissionError:
        print(f"{prefix}  🔒 权限不足")

# 测试目录树查看器
print("\n项目目录结构:")
print_directory_tree('python_learning')

# 练习4: 简单的文件压缩/解压
def create_zip_archive(source_dir, zip_name):
    """创建ZIP压缩文件"""
    try:
        shutil.make_archive(zip_name, 'zip', source_dir)
        zip_path = zip_name + '.zip'
        if os.path.exists(zip_path):
            size = os.path.getsize(zip_path)
            print(f"ZIP文件已创建: {zip_path} ({size} bytes)")
            return True
    except Exception as e:
        print(f"创建ZIP失败: {e}")
    return False

# 测试ZIP创建
if create_zip_archive('python_learning/utils', 'utils_backup'):
    print("备份创建成功")

# ===== 清理临时文件 =====

print("\n清理示例文件...")
cleanup_files = [
    new_name,  # 重命名的文件
    csv_filename,
    json_filename,
    'python_learning/utils/utils_backup.zip'
]

for file_path in cleanup_files:
    try:
        if os.path.exists(file_path):
            if os.path.isdir(file_path):
                shutil.rmtree(file_path)
            else:
                os.remove(file_path)
            print(f"已清理: {file_path}")
    except OSError as e:
        print(f"清理失败 {file_path}: {e}")

print("文件操作学习完成！文件操作是Python编程的基础，掌握这些技巧能让你高效处理各种数据存储需求。")
