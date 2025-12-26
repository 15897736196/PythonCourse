# Python学习项目 - 环境设置指南

本文档介绍如何设置Python学习环境。

## 📋 系统要求

### 基本要求
- **操作系统**: Windows 10+, macOS 10.14+, Ubuntu 18.04+
- **Python版本**: 3.6 或更高版本
- **内存**: 至少4GB RAM
- **磁盘空间**: 至少1GB可用空间

### 推荐配置
- **Python版本**: 3.8+
- **IDE**: VS Code, PyCharm, 或其他支持Python的编辑器
- **内存**: 8GB+ RAM

## 🐍 Python安装

### Windows
1. 访问 [python.org](https://python.org)
2. 下载最新Python 3.x版本
3. 运行安装程序，**务必勾选 "Add Python to PATH"**
4. 验证安装: 打开命令提示符，输入 `python --version`

### macOS
```bash
# 使用Homebrew (推荐)
brew install python

# 或从官网下载安装包
# 访问 https://python.org 下载并安装
```

### Linux (Ubuntu/Debian)
```bash
# 更新包管理器
sudo apt update

# 安装Python 3
sudo apt install python3 python3-pip

# 验证安装
python3 --version
pip3 --version
```

## 🛠️ 开发环境设置

### 1. 虚拟环境 (推荐)

虚拟环境可以隔离不同项目的依赖，避免冲突。

#### Windows
```bash
# 安装virtualenv (如果还没安装)
pip install virtualenv

# 创建虚拟环境
python -m venv python_learning_env

# 激活虚拟环境
python_learning_env\Scripts\activate

# 在虚拟环境中，你的命令提示符会显示 (python_learning_env)
```

#### macOS/Linux
```bash
# 安装virtualenv (如果还没安装)
pip3 install virtualenv

# 创建虚拟环境
python3 -m venv python_learning_env

# 激活虚拟环境
source python_learning_env/bin/activate

# 在虚拟环境中，你的shell提示符会显示 (python_learning_env)
```

#### 在虚拟环境中安装依赖
```bash
# 激活虚拟环境后
pip install -r requirements.txt
```

#### 退出虚拟环境
```bash
deactivate
```

### 2. IDE设置

#### VS Code (推荐)
1. 下载并安装 [VS Code](https://code.visualstudio.com/)
2. 安装Python扩展:
   - 打开VS Code
   - 按 `Ctrl+Shift+P` (Windows/Linux) 或 `Cmd+Shift+P` (macOS)
   - 输入 "Extensions: Install Extensions"
   - 搜索 "Python" 并安装 Microsoft的Python扩展
3. 配置Python解释器:
   - 按 `Ctrl+Shift+P`，输入 "Python: Select Interpreter"
   - 选择虚拟环境中的Python解释器

#### PyCharm
1. 下载并安装 [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/)
2. 打开项目，选择虚拟环境作为项目解释器

## 📁 项目设置

### 1. 下载项目
```bash
# 如果是从Git仓库克隆
git clone <repository-url>
cd python_learning

# 如果是下载ZIP文件，解压到本地目录
```

### 2. 安装项目依赖
```bash
# 激活虚拟环境（如果使用）
# Windows: python_learning_env\Scripts\activate
# macOS/Linux: source python_learning_env/bin/activate

# 安装依赖
pip install -r requirements.txt
```

### 3. 验证安装
```bash
# 运行一个简单的测试
python basics/variables_and_types.py

# 如果能正常运行，说明环境设置成功
```

## 🧪 测试环境

### 运行基础测试
```bash
# 测试Python基本功能
python -c "print('Hello, Python!')"

# 测试导入标准库
python -c "import sys, os, json; print('标准库导入成功')"

# 测试文件操作
python intermediate/exception_handling.py
```

## 🔧 常见问题解决

### 问题1: python命令找不到
**错误**: `'python' is not recognized as an internal or external command`

**解决方法**:
- 重新安装Python，确保勾选 "Add Python to PATH"
- 或使用完整路径: `C:\Python39\python.exe`
- 或使用 `python3` 命令 (Linux/macOS)

### 问题2: pip安装失败
**错误**: 网络连接问题或权限问题

**解决方法**:
```bash
# 使用国内镜像
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple package-name

# 或升级pip
python -m pip install --upgrade pip
```

### 问题3: 虚拟环境激活失败
**Windows**: 确保使用正确的激活脚本路径
```bash
# 正确路径
venv\Scripts\activate

# 错误路径
venv/bin/activate  # 这在Windows上不存在
```

### 问题4: 编码问题
**错误**: UnicodeDecodeError 或编码相关错误

**解决方法**:
- 确保Python文件使用UTF-8编码保存
- 在文件开头添加编码声明:
```python
# -*- coding: utf-8 -*-
```

### 问题5: 模块导入错误
**错误**: ModuleNotFoundError

**解决方法**:
- 确保在正确的虚拟环境中
- 检查当前工作目录
- 验证包是否正确安装: `pip list`

## 📚 学习资源

### 验证Python安装
```bash
# 检查Python版本
python --version

# 检查pip版本
pip --version

# 列出已安装的包
pip list

# 检查Python路径
python -c "import sys; print('\\n'.join(sys.path))"
```

### 有用的命令
```bash
# 更新所有已安装的包
pip list --outdated
pip install --upgrade -r requirements.txt

# 创建requirements.txt的备份
pip freeze > requirements_backup.txt

# 清理缓存
pip cache purge
```

## 🚀 下一步

环境设置完成后，你可以：

1. **开始学习**: 按照 `README.md` 中的学习路径开始
2. **运行示例**: 逐个运行项目中的Python文件
3. **动手实践**: 修改代码，添加自己的实验
4. **寻求帮助**: 如果遇到问题，可以查看错误信息或寻求社区帮助

## 💡 提示

- **保持环境清洁**: 定期更新包，清理不需要的虚拟环境
- **备份工作**: 重要代码要备份
- **版本控制**: 考虑使用Git来管理你的学习进度
- **社区支持**: 遇到问题时，可以在Stack Overflow、Reddit的r/learnpython等社区寻求帮助

**祝学习愉快！** 🎉
