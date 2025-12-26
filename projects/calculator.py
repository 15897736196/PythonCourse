# Python学习项目 - 实际项目：高级计算器
# 学习序号：第8阶段 第1课 - 计算器项目
# 建议学习时间：120-180分钟
# 前置知识：第1-7阶段 - 完整Python基础
# 下一课：第8阶段 第2课 - 任务管理器项目 (task_manager.py)
# 本项目展示如何综合运用所学知识构建一个功能完整的计算器应用

"""
高级计算器功能特性:
1. 基础算术运算 (+, -, *, /)
2. 高级数学运算 (幂、平方根、阶乘、对数等)
3. 内存功能 (存储/调用计算结果)
4. 计算历史记录
5. 错误处理和输入验证
6. 用户友好的命令行界面
7. 数据持久化 (保存历史记录)
"""

import math
import json
import os
from datetime import datetime
from typing import Optional, List, Dict, Any

# ===== 自定义异常类 =====

class CalculatorError(Exception):
    """计算器错误基类"""
    pass

class InvalidOperationError(CalculatorError):
    """无效操作错误"""
    pass

class DivisionByZeroError(CalculatorError):
    """除零错误"""
    pass

class InvalidInputError(CalculatorError):
    """无效输入错误"""
    pass

# ===== 计算器类 =====

class AdvancedCalculator:
    """
    高级计算器类

    提供基础和高级数学运算功能，包含历史记录和内存功能
    """

    def __init__(self):
        self.memory: float = 0.0  # 内存存储的值
        self.history: List[Dict[str, Any]] = []  # 计算历史
        self.history_file = "calculator_history.json"  # 历史记录文件

        # 加载历史记录
        self._load_history()

    def _load_history(self) -> None:
        """加载历史记录"""
        try:
            if os.path.exists(self.history_file):
                with open(self.history_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.history = data.get('history', [])
                    self.memory = data.get('memory', 0.0)
        except (json.JSONDecodeError, IOError) as e:
            print(f"加载历史记录失败: {e}")
            self.history = []
            self.memory = 0.0

    def _save_history(self) -> None:
        """保存历史记录"""
        try:
            data = {
                'history': self.history[-100:],  # 只保存最近100条记录
                'memory': self.memory,
                'last_saved': datetime.now().isoformat()
            }
            with open(self.history_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except IOError as e:
            print(f"保存历史记录失败: {e}")

    def _add_to_history(self, operation: str, inputs: List[float],
                       result: float, description: str = "") -> None:
        """添加计算到历史记录"""
        entry = {
            'timestamp': datetime.now().isoformat(),
            'operation': operation,
            'inputs': inputs,
            'result': result,
            'description': description
        }
        self.history.append(entry)
        self._save_history()

    def _validate_number(self, value: Any) -> float:
        """验证并转换输入为数字"""
        try:
            if isinstance(value, str):
                # 处理特殊输入
                if value.lower() in ['pi', 'π']:
                    return math.pi
                elif value.lower() in ['e']:
                    return math.e
                elif value.lower() in ['mem', 'memory']:
                    return self.memory

            return float(value)
        except (ValueError, TypeError):
            raise InvalidInputError(f"无效的数字输入: {value}")

    # ===== 基础运算 =====

    def add(self, a: Any, b: Any) -> float:
        """加法运算"""
        a, b = self._validate_number(a), self._validate_number(b)
        result = a + b
        self._add_to_history('add', [a, b], result, f"{a} + {b}")
        return result

    def subtract(self, a: Any, b: Any) -> float:
        """减法运算"""
        a, b = self._validate_number(a), self._validate_number(b)
        result = a - b
        self._add_to_history('subtract', [a, b], result, f"{a} - {b}")
        return result

    def multiply(self, a: Any, b: Any) -> float:
        """乘法运算"""
        a, b = self._validate_number(a), self._validate_number(b)
        result = a * b
        self._add_to_history('multiply', [a, b], result, f"{a} × {b}")
        return result

    def divide(self, a: Any, b: Any) -> float:
        """除法运算"""
        a, b = self._validate_number(a), self._validate_number(b)
        if b == 0:
            raise DivisionByZeroError("除数不能为0")
        result = a / b
        self._add_to_history('divide', [a, b], result, f"{a} ÷ {b}")
        return result

    # ===== 高级运算 =====

    def power(self, base: Any, exponent: Any) -> float:
        """幂运算"""
        base, exponent = self._validate_number(base), self._validate_number(exponent)
        result = math.pow(base, exponent)
        self._add_to_history('power', [base, exponent], result, f"{base}^{exponent}")
        return result

    def square_root(self, x: Any) -> float:
        """平方根"""
        x = self._validate_number(x)
        if x < 0:
            raise InvalidOperationError("不能计算负数的平方根")
        result = math.sqrt(x)
        self._add_to_history('sqrt', [x], result, f"√{x}")
        return result

    def factorial(self, n: Any) -> int:
        """阶乘"""
        n = self._validate_number(n)
        if not n.is_integer() or n < 0:
            raise InvalidOperationError("阶乘只能计算非负整数")
        if n > 100:  # 防止过大的计算
            raise InvalidOperationError("阶乘计算的数字不能超过100")

        result = math.factorial(int(n))
        self._add_to_history('factorial', [n], result, f"{int(n)}!")
        return result

    def logarithm(self, x: Any, base: Any = 10) -> float:
        """对数运算"""
        x, base = self._validate_number(x), self._validate_number(base)
        if x <= 0:
            raise InvalidOperationError("对数真数必须为正数")
        if base <= 0 or base == 1:
            raise InvalidOperationError("对数底数必须为正数且不等于1")

        result = math.log(x, base)
        base_str = "e" if base == math.e else str(base)
        self._add_to_history('log', [x, base], result, f"log_{base_str}({x})")
        return result

    def sine(self, angle: Any, degrees: bool = False) -> float:
        """正弦函数"""
        angle = self._validate_number(angle)
        if degrees:
            angle = math.radians(angle)

        result = math.sin(angle)
        unit = "°" if degrees else "rad"
        self._add_to_history('sin', [angle, 1 if degrees else 0], result,
                           f"sin({angle}{unit})")
        return result

    def cosine(self, angle: Any, degrees: bool = False) -> float:
        """余弦函数"""
        angle = self._validate_number(angle)
        if degrees:
            angle = math.radians(angle)

        result = math.cos(angle)
        unit = "°" if degrees else "rad"
        self._add_to_history('cos', [angle, 1 if degrees else 0], result,
                           f"cos({angle}{unit})")
        return result

    def tangent(self, angle: Any, degrees: bool = False) -> float:
        """正切函数"""
        angle = self._validate_number(angle)
        if degrees:
            angle = math.radians(angle)

        result = math.tan(angle)
        unit = "°" if degrees else "rad"
        self._add_to_history('tan', [angle, 1 if degrees else 0], result,
                           f"tan({angle}{unit})")
        return result

    # ===== 内存功能 =====

    def store_memory(self, value: Any) -> None:
        """存储值到内存"""
        value = self._validate_number(value)
        self.memory = value
        self._save_history()
        print(f"已存储 {value} 到内存")

    def recall_memory(self) -> float:
        """调用内存中的值"""
        return self.memory

    def clear_memory(self) -> None:
        """清除内存"""
        self.memory = 0.0
        self._save_history()
        print("内存已清除")

    # ===== 历史记录功能 =====

    def get_history(self, limit: int = 10) -> List[Dict[str, Any]]:
        """获取计算历史"""
        return self.history[-limit:] if limit > 0 else self.history

    def clear_history(self) -> None:
        """清除历史记录"""
        self.history.clear()
        self._save_history()
        print("历史记录已清除")

    def show_history(self, limit: int = 10) -> None:
        """显示计算历史"""
        history = self.get_history(limit)
        if not history:
            print("暂无计算历史")
            return

        print(f"\n最近 {len(history)} 次计算:")
        print("-" * 60)

        for i, entry in enumerate(history, 1):
            timestamp = datetime.fromisoformat(entry['timestamp'])
            time_str = timestamp.strftime("%H:%M:%S")

            print("2d")
            if entry.get('description'):
                print(f"         描述: {entry['description']}")

        print("-" * 60)

    # ===== 批量计算功能 =====

    def calculate_expression(self, expression: str) -> float:
        """
        计算数学表达式
        支持: +, -, *, /, **, sqrt(), sin(), cos(), tan(), log(), ln()
        """
        try:
            # 安全评估表达式（限制可用函数）
            allowed_names = {
                k: v for k, v in math.__dict__.items()
                if not k.startswith("__")
            }
            allowed_names.update({
                "sqrt": math.sqrt,
                "sin": math.sin,
                "cos": math.cos,
                "tan": math.tan,
                "log": math.log,
                "ln": lambda x: math.log(x, math.e),
                "pi": math.pi,
                "e": math.e,
                "mem": self.memory
            })

            # 替换常用函数名
            expression = expression.replace("ln(", "log(math.e, ")

            result = eval(expression, {"__builtins__": {}}, allowed_names)
            result = float(result)

            self._add_to_history('expression', [expression], result,
                               f"表达式: {expression}")
            return result

        except Exception as e:
            raise InvalidOperationError(f"表达式计算失败: {e}")

# ===== 用户界面 =====

class CalculatorUI:
    """计算器用户界面"""

    def __init__(self):
        self.calculator = AdvancedCalculator()
        self.commands = {
            'help': self.show_help,
            'quit': self.quit_calculator,
            'exit': self.quit_calculator,
            'history': self.show_calculation_history,
            'memory': self.show_memory,
            'clear': self.clear_history,
            'memstore': self.store_to_memory,
            'memrecall': self.recall_memory,
            'memclear': self.clear_memory,
        }

    def show_help(self) -> None:
        """显示帮助信息"""
        help_text = """
高级计算器使用帮助
==================

基础运算:
  add a b        加法运算
  sub a b        减法运算
  mul a b        乘法运算
  div a b        除法运算

高级运算:
  pow a b        幂运算 (a^b)
  sqrt x         平方根
  fact n         阶乘
  log x [base]   对数运算 (默认10为底)
  sin x [deg]    正弦函数 (deg=1表示角度制)
  cos x [deg]    余弦函数
  tan x [deg]    正切函数

内存功能:
  memstore x     存储x到内存
  memrecall      调用内存值
  memclear       清除内存

历史记录:
  history [n]    显示最近n次计算 (默认10次)
  clear          清除历史记录

表达式计算:
  calc <expr>    计算数学表达式
                 支持: + - * / ** () sqrt() sin() cos() tan()
                 log() ln() pi e mem

特殊输入:
  pi 或 π        圆周率
  e              自然对数
  mem 或 memory  内存值

其他命令:
  help           显示此帮助
  quit/exit      退出计算器

示例:
  add 5 3
  pow 2 8
  sqrt 16
  calc sin(pi/2) + cos(0)
  memstore 42
  calc mem * 2
        """
        print(help_text)

    def show_calculation_history(self, args: List[str] = None) -> None:
        """显示计算历史"""
        limit = 10
        if args and len(args) > 0:
            try:
                limit = int(args[0])
            except ValueError:
                print("无效的显示数量，使用默认值10")
        self.calculator.show_history(limit)

    def show_memory(self) -> None:
        """显示内存值"""
        print(f"内存值: {self.calculator.memory}")

    def clear_history(self) -> None:
        """清除历史记录"""
        self.calculator.clear_history()

    def store_to_memory(self, args: List[str]) -> None:
        """存储值到内存"""
        if not args:
            print("请提供要存储的值")
            return
        try:
            value = float(args[0])
            self.calculator.store_memory(value)
        except ValueError:
            print("无效的数值")

    def recall_memory(self) -> None:
        """调用内存值"""
        value = self.calculator.recall_memory()
        print(f"内存值: {value}")

    def clear_memory(self) -> None:
        """清除内存"""
        self.calculator.clear_memory()

    def quit_calculator(self) -> None:
        """退出计算器"""
        print("感谢使用高级计算器！再见！")
        exit(0)

    def execute_command(self, command: str, args: List[str]) -> None:
        """执行命令"""
        if command in self.commands:
            try:
                self.commands[command](args)
            except Exception as e:
                print(f"命令执行失败: {e}")
        else:
            print(f"未知命令: {command}")
            print("输入 'help' 查看可用命令")

    def calculate(self, operation: str, args: List[str]) -> None:
        """执行计算"""
        try:
            if operation == 'add':
                result = self.calculator.add(args[0], args[1])
            elif operation == 'sub':
                result = self.calculator.subtract(args[0], args[1])
            elif operation == 'mul':
                result = self.calculator.multiply(args[0], args[1])
            elif operation == 'div':
                result = self.calculator.divide(args[0], args[1])
            elif operation == 'pow':
                result = self.calculator.power(args[0], args[1])
            elif operation == 'sqrt':
                result = self.calculator.square_root(args[0])
            elif operation == 'fact':
                result = self.calculator.factorial(args[0])
            elif operation == 'log':
                if len(args) > 1:
                    result = self.calculator.logarithm(args[0], args[1])
                else:
                    result = self.calculator.logarithm(args[0])
            elif operation == 'sin':
                degrees = len(args) > 1 and args[1] == 'deg'
                result = self.calculator.sine(args[0], degrees)
            elif operation == 'cos':
                degrees = len(args) > 1 and args[1] == 'deg'
                result = self.calculator.cosine(args[0], degrees)
            elif operation == 'tan':
                degrees = len(args) > 1 and args[1] == 'deg'
                result = self.calculator.tangent(args[0], degrees)
            else:
                print(f"未知运算: {operation}")
                return

            print(f"结果: {result}")

        except CalculatorError as e:
            print(f"计算错误: {e}")
        except Exception as e:
            print(f"意外错误: {e}")

    def calculate_expression(self, expression: str) -> None:
        """计算表达式"""
        try:
            result = self.calculator.calculate_expression(expression)
            print(f"结果: {result}")
        except CalculatorError as e:
            print(f"表达式计算错误: {e}")
        except Exception as e:
            print(f"表达式错误: {e}")

    def run(self) -> None:
        """运行计算器界面"""
        print("=" * 50)
        print("    欢迎使用高级计算器 v2.0")
        print("=" * 50)
        print("输入 'help' 查看使用说明")
        print("输入 'quit' 或 'exit' 退出")
        print()

        while True:
            try:
                user_input = input("计算器> ").strip()

                if not user_input:
                    continue

                parts = user_input.split()
                command = parts[0].lower()
                args = parts[1:]

                # 检查是否是命令
                if command in self.commands:
                    self.execute_command(command, args)
                # 检查是否是计算表达式
                elif command == 'calc' and args:
                    expression = ' '.join(args)
                    self.calculate_expression(expression)
                # 检查是否是直接计算
                else:
                    if len(args) < 1:
                        print("请提供足够的参数")
                        continue
                    self.calculate(command, args)

            except KeyboardInterrupt:
                print("\n\n感谢使用高级计算器！再见！")
                break
            except EOFError:
                print("\n\n感谢使用高级计算器！再见！")
                break
            except Exception as e:
                print(f"输入错误: {e}")
                print("输入 'help' 查看正确用法")

# ===== 主程序 =====

def main():
    """主程序入口"""
    ui = CalculatorUI()
    ui.run()

if __name__ == "__main__":
    main()
