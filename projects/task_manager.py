# Python学习项目 - 实际项目：任务管理器
# 学习序号：第8阶段 第2课 - 任务管理器项目
# 建议学习时间：180-240分钟
# 前置知识：第1-7阶段 - 完整Python基础
# 下一课：第8阶段 第3课 - Web应用项目 (simple_web_app.py)
# 本项目展示如何构建一个功能完整的任务管理系统

"""
任务管理器功能特性:
1. 任务的增删改查 (CRUD)
2. 任务分类和优先级管理
3. 任务状态跟踪 (待办/进行中/完成)
4. 截止日期和提醒功能
5. 数据持久化 (JSON文件存储)
6. 统计和报告功能
7. 命令行用户界面
8. 任务搜索和过滤
"""

import json
import os
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Any
from enum import Enum
import uuid

# ===== 数据模型 =====

class TaskStatus(Enum):
    """任务状态枚举"""
    TODO = "待办"
    IN_PROGRESS = "进行中"
    DONE = "完成"
    CANCELLED = "已取消"

class TaskPriority(Enum):
    """任务优先级枚举"""
    LOW = "低"
    MEDIUM = "中"
    HIGH = "高"
    URGENT = "紧急"

class Task:
    """任务类"""

    def __init__(self, title: str, description: str = "",
                 priority: TaskPriority = TaskPriority.MEDIUM,
                 category: str = "默认",
                 due_date: Optional[datetime] = None):
        self.id = str(uuid.uuid4())[:8]  # 简短的UUID
        self.title = title
        self.description = description
        self.priority = priority
        self.category = category
        self.status = TaskStatus.TODO
        self.due_date = due_date
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.completed_at: Optional[datetime] = None

    def to_dict(self) -> Dict[str, Any]:
        """转换为字典格式（用于JSON序列化）"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'priority': self.priority.value,
            'category': self.category,
            'status': self.status.value,
            'due_date': self.due_date.isoformat() if self.due_date else None,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'completed_at': self.completed_at.isoformat() if self.completed_at else None,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Task':
        """从字典创建任务实例"""
        task = cls(
            title=data['title'],
            description=data.get('description', ''),
            priority=TaskPriority(data.get('priority', '中')),
            category=data.get('category', '默认'),
        )
        task.id = data['id']
        task.status = TaskStatus(data.get('status', '待办'))

        if data.get('due_date'):
            task.due_date = datetime.fromisoformat(data['due_date'])
        if data.get('created_at'):
            task.created_at = datetime.fromisoformat(data['created_at'])
        if data.get('updated_at'):
            task.updated_at = datetime.fromisoformat(data['updated_at'])
        if data.get('completed_at'):
            task.completed_at = datetime.fromisoformat(data['completed_at'])

        return task

    def update(self, **kwargs) -> None:
        """更新任务属性"""
        for key, value in kwargs.items():
            if hasattr(self, key):
                if key == 'priority':
                    value = TaskPriority(value)
                elif key == 'status':
                    value = TaskStatus(value)
                elif key == 'due_date' and value:
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)

        self.updated_at = datetime.now()

        # 如果状态变为完成，设置完成时间
        if kwargs.get('status') == TaskStatus.DONE and not self.completed_at:
            self.completed_at = datetime.now()

    def is_overdue(self) -> bool:
        """检查任务是否过期"""
        if self.due_date and self.status != TaskStatus.DONE:
            return datetime.now() > self.due_date
        return False

    def days_until_due(self) -> Optional[int]:
        """计算距离截止日期的天数"""
        if not self.due_date:
            return None
        delta = self.due_date - datetime.now()
        return delta.days

    def __str__(self) -> str:
        """字符串表示"""
        status_icon = {
            TaskStatus.TODO: "⏳",
            TaskStatus.IN_PROGRESS: "🔄",
            TaskStatus.DONE: "✅",
            TaskStatus.CANCELLED: "❌"
        }

        priority_color = {
            TaskPriority.LOW: "🟢",
            TaskPriority.MEDIUM: "🟡",
            TaskPriority.HIGH: "🟠",
            TaskPriority.URGENT: "🔴"
        }

        due_info = ""
        if self.due_date:
            days = self.days_until_due()
            if days is not None:
                if days < 0:
                    due_info = f" 过期{-days}天"
                elif days == 0:
                    due_info = " 今天截止"
                else:
                    due_info = f" {days}天后截止"

        return (f"{status_icon[self.status]} {priority_color[self.priority]} "
                f"[{self.id}] {self.title} ({self.category}){due_info}")

# ===== 任务管理器类 =====

class TaskManager:
    """任务管理器类"""

    def __init__(self, data_file: str = "tasks.json"):
        self.data_file = data_file
        self.tasks: List[Task] = []
        self.load_tasks()

    def load_tasks(self) -> None:
        """从文件加载任务"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.tasks = [Task.from_dict(task_data) for task_data in data]
        except (json.JSONDecodeError, IOError) as e:
            print(f"加载任务数据失败: {e}")
            self.tasks = []

    def save_tasks(self) -> None:
        """保存任务到文件"""
        try:
            data = [task.to_dict() for task in self.tasks]
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except IOError as e:
            print(f"保存任务数据失败: {e}")

    def add_task(self, title: str, description: str = "",
                 priority: str = "中", category: str = "默认",
                 due_date_str: Optional[str] = None) -> Task:
        """添加新任务"""
        try:
            priority_enum = TaskPriority(priority)
        except ValueError:
            print(f"无效的优先级: {priority}，使用默认优先级'中'")
            priority_enum = TaskPriority.MEDIUM

        due_date = None
        if due_date_str:
            try:
                due_date = datetime.fromisoformat(due_date_str)
            except ValueError:
                print(f"无效的日期格式: {due_date_str}，忽略截止日期")

        task = Task(title, description, priority_enum, category, due_date)
        self.tasks.append(task)
        self.save_tasks()
        print(f"任务已添加: {task}")
        return task

    def get_task(self, task_id: str) -> Optional[Task]:
        """根据ID获取任务"""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: str, **kwargs) -> bool:
        """更新任务"""
        task = self.get_task(task_id)
        if not task:
            print(f"任务不存在: {task_id}")
            return False

        try:
            task.update(**kwargs)
            self.save_tasks()
            print(f"任务已更新: {task}")
            return True
        except ValueError as e:
            print(f"更新失败: {e}")
            return False

    def delete_task(self, task_id: str) -> bool:
        """删除任务"""
        task = self.get_task(task_id)
        if not task:
            print(f"任务不存在: {task_id}")
            return False

        self.tasks.remove(task)
        self.save_tasks()
        print(f"任务已删除: {task.title}")
        return True

    def list_tasks(self, status_filter: Optional[str] = None,
                   category_filter: Optional[str] = None,
                   priority_filter: Optional[str] = None,
                   show_overdue: bool = False) -> List[Task]:
        """列出任务（支持过滤）"""
        filtered_tasks = self.tasks.copy()

        if status_filter:
            try:
                status_enum = TaskStatus(status_filter)
                filtered_tasks = [t for t in filtered_tasks if t.status == status_enum]
            except ValueError:
                print(f"无效的状态过滤: {status_filter}")

        if category_filter:
            filtered_tasks = [t for t in filtered_tasks if t.category == category_filter]

        if priority_filter:
            try:
                priority_enum = TaskPriority(priority_filter)
                filtered_tasks = [t for t in filtered_tasks if t.priority == priority_enum]
            except ValueError:
                print(f"无效的优先级过滤: {priority_filter}")

        if show_overdue:
            filtered_tasks = [t for t in filtered_tasks if t.is_overdue()]

        return filtered_tasks

    def search_tasks(self, keyword: str) -> List[Task]:
        """搜索任务"""
        keyword_lower = keyword.lower()
        return [task for task in self.tasks
                if keyword_lower in task.title.lower()
                or keyword_lower in task.description.lower()
                or keyword_lower in task.category.lower()]

    def get_statistics(self) -> Dict[str, Any]:
        """获取统计信息"""
        total = len(self.tasks)
        status_counts = {}
        priority_counts = {}
        category_counts = {}
        overdue_count = 0

        for task in self.tasks:
            status_counts[task.status.value] = status_counts.get(task.status.value, 0) + 1
            priority_counts[task.priority.value] = priority_counts.get(task.priority.value, 0) + 1
            category_counts[task.category] = category_counts.get(task.category, 0) + 1

            if task.is_overdue():
                overdue_count += 1

        return {
            'total_tasks': total,
            'status_distribution': status_counts,
            'priority_distribution': priority_counts,
            'category_distribution': category_counts,
            'overdue_tasks': overdue_count,
            'completion_rate': (status_counts.get(TaskStatus.DONE.value, 0) / total * 100) if total > 0 else 0
        }

    def get_upcoming_tasks(self, days: int = 7) -> List[Task]:
        """获取即将到期的任务"""
        now = datetime.now()
        future_date = now + timedelta(days=days)

        upcoming = []
        for task in self.tasks:
            if (task.due_date and now <= task.due_date <= future_date
                and task.status != TaskStatus.DONE):
                upcoming.append(task)

        return sorted(upcoming, key=lambda t: t.due_date)

# ===== 用户界面 =====

class TaskManagerUI:
    """任务管理器用户界面"""

    def __init__(self):
        self.manager = TaskManager()

    def show_help(self) -> None:
        """显示帮助信息"""
        help_text = """
任务管理器使用帮助
================

任务管理:
  add <标题> [描述] [优先级] [分类] [截止日期]
     添加新任务
     优先级: 低/中/高/紧急 (默认: 中)
     日期格式: YYYY-MM-DD 或 YYYY-MM-DD HH:MM:SS

  list [状态] [分类] [优先级] [--overdue]
     列出任务
     状态: 待办/进行中/完成/已取消

  show <任务ID>
     显示任务详情

  update <任务ID> <属性> <值>
     更新任务属性
     属性: title, description, priority, category, status, due_date

  delete <任务ID>
     删除任务

  search <关键词>
     搜索任务

统计和报告:
  stats          显示统计信息
  upcoming [天数] 显示即将到期的任务 (默认7天)

其他命令:
  help           显示此帮助
  quit/exit      退出程序

示例:
  add "完成Python项目" "实现计算器功能" 高 工作 2024-12-31
  list 待办
  update abc12345 status 完成
  search 项目
  upcoming 3
        """
        print(help_text)

    def add_task_interactive(self, args: List[str]) -> None:
        """交互式添加任务"""
        if not args:
            # 交互式输入
            title = input("任务标题: ").strip()
            if not title:
                print("任务标题不能为空")
                return

            description = input("任务描述 (可选): ").strip()
            priority = input("优先级 (低/中/高/紧急, 默认: 中): ").strip() or "中"
            category = input("分类 (默认: 默认): ").strip() or "默认"
            due_date_str = input("截止日期 (YYYY-MM-DD, 可选): ").strip()

        else:
            # 命令行参数
            title = args[0]
            description = args[1] if len(args) > 1 else ""
            priority = args[2] if len(args) > 2 else "中"
            category = args[3] if len(args) > 3 else "默认"
            due_date_str = args[4] if len(args) > 4 else None

        if not title:
            print("任务标题不能为空")
            return

        self.manager.add_task(title, description, priority, category, due_date_str)

    def list_tasks_interactive(self, args: List[str]) -> None:
        """列出任务"""
        status_filter = None
        category_filter = None
        priority_filter = None
        show_overdue = False

        # 解析参数
        for arg in args:
            if arg in ['待办', '进行中', '完成', '已取消']:
                status_filter = arg
            elif arg in ['低', '中', '高', '紧急']:
                priority_filter = arg
            elif arg == '--overdue':
                show_overdue = True
            else:
                category_filter = arg

        tasks = self.manager.list_tasks(status_filter, category_filter,
                                      priority_filter, show_overdue)

        if not tasks:
            print("没有找到匹配的任务")
            return

        print(f"\n找到 {len(tasks)} 个任务:")
        print("-" * 80)
        for task in tasks:
            print(task)
        print("-" * 80)

    def show_task_detail(self, args: List[str]) -> None:
        """显示任务详情"""
        if not args:
            print("请提供任务ID")
            return

        task_id = args[0]
        task = self.manager.get_task(task_id)

        if not task:
            print(f"任务不存在: {task_id}")
            return

        print(f"\n任务详情:")
        print(f"ID: {task.id}")
        print(f"标题: {task.title}")
        print(f"描述: {task.description}")
        print(f"状态: {task.status.value}")
        print(f"优先级: {task.priority.value}")
        print(f"分类: {task.category}")
        print(f"截止日期: {task.due_date.strftime('%Y-%m-%d %H:%M') if task.due_date else '无'}")
        print(f"创建时间: {task.created_at.strftime('%Y-%m-%d %H:%M')}")
        print(f"更新时间: {task.updated_at.strftime('%Y-%m-%d %H:%M')}")
        print(f"完成时间: {task.completed_at.strftime('%Y-%m-%d %H:%M') if task.completed_at else '未完成'}")

        if task.is_overdue():
            print("⚠️  此任务已过期!")

    def update_task_interactive(self, args: List[str]) -> None:
        """更新任务"""
        if len(args) < 3:
            print("用法: update <任务ID> <属性> <值>")
            return

        task_id = args[0]
        attribute = args[1]
        value = ' '.join(args[2:])

        # 属性映射
        attr_mapping = {
            'title': 'title',
            'description': 'description',
            'priority': 'priority',
            'category': 'category',
            'status': 'status',
            'due_date': 'due_date'
        }

        if attribute not in attr_mapping:
            print(f"无效的属性: {attribute}")
            print("可用属性: title, description, priority, category, status, due_date")
            return

        self.manager.update_task(task_id, **{attr_mapping[attribute]: value})

    def delete_task_interactive(self, args: List[str]) -> None:
        """删除任务"""
        if not args:
            print("请提供任务ID")
            return

        task_id = args[0]

        # 确认删除
        confirm = input(f"确定要删除任务 {task_id} 吗? (y/N): ").strip().lower()
        if confirm == 'y':
            self.manager.delete_task(task_id)
        else:
            print("删除已取消")

    def search_tasks_interactive(self, args: List[str]) -> None:
        """搜索任务"""
        if not args:
            print("请提供搜索关键词")
            return

        keyword = ' '.join(args)
        tasks = self.manager.search_tasks(keyword)

        if not tasks:
            print(f"没有找到包含 '{keyword}' 的任务")
            return

        print(f"\n搜索 '{keyword}' 找到 {len(tasks)} 个任务:")
        print("-" * 80)
        for task in tasks:
            print(task)
        print("-" * 80)

    def show_statistics(self) -> None:
        """显示统计信息"""
        stats = self.manager.get_statistics()

        print(f"\n📊 任务统计信息")
        print(f"=" * 40)
        print(f"总任务数: {stats['total_tasks']}")
        print(f"完成率: {stats['completion_rate']:.1f}%")
        print(f"过期任务: {stats['overdue_tasks']}")

        print(f"\n状态分布:")
        for status, count in stats['status_distribution'].items():
            print(f"  {status}: {count}")

        print(f"\n优先级分布:")
        for priority, count in stats['priority_distribution'].items():
            print(f"  {priority}: {count}")

        print(f"\n分类分布:")
        for category, count in stats['category_distribution'].items():
            print(f"  {category}: {count}")

    def show_upcoming_tasks(self, args: List[str]) -> None:
        """显示即将到期的任务"""
        days = 7
        if args:
            try:
                days = int(args[0])
            except ValueError:
                print("无效的天数，使用默认值7")

        tasks = self.manager.get_upcoming_tasks(days)

        if not tasks:
            print(f"未来 {days} 天内没有即将到期的任务")
            return

        print(f"\n⏰ 未来 {days} 天内即将到期的任务:")
        print("-" * 80)
        for task in tasks:
            days_left = task.days_until_due()
            urgency = "⚠️ 今天到期" if days_left == 0 else f"{days_left}天后到期"
            print(f"{task} - {urgency}")
        print("-" * 80)

    def run(self) -> None:
        """运行任务管理器界面"""
        print("=" * 50)
        print("    欢迎使用任务管理器 v1.0")
        print("=" * 50)
        print("输入 'help' 查看使用说明")
        print("输入 'quit' 或 'exit' 退出")
        print()

        while True:
            try:
                user_input = input("任务管理器> ").strip()

                if not user_input:
                    continue

                parts = user_input.split()
                command = parts[0].lower()
                args = parts[1:]

                if command == 'help':
                    self.show_help()
                elif command in ['quit', 'exit']:
                    print("感谢使用任务管理器！再见！")
                    break
                elif command == 'add':
                    self.add_task_interactive(args)
                elif command == 'list':
                    self.list_tasks_interactive(args)
                elif command == 'show':
                    self.show_task_detail(args)
                elif command == 'update':
                    self.update_task_interactive(args)
                elif command == 'delete':
                    self.delete_task_interactive(args)
                elif command == 'search':
                    self.search_tasks_interactive(args)
                elif command == 'stats':
                    self.show_statistics()
                elif command == 'upcoming':
                    self.show_upcoming_tasks(args)
                else:
                    print(f"未知命令: {command}")
                    print("输入 'help' 查看可用命令")

            except KeyboardInterrupt:
                print("\n\n感谢使用任务管理器！再见！")
                break
            except EOFError:
                print("\n\n感谢使用任务管理器！再见！")
                break
            except Exception as e:
                print(f"命令执行出错: {e}")

# ===== 主程序 =====

def main():
    """主程序入口"""
    ui = TaskManagerUI()
    ui.run()

if __name__ == "__main__":
    main()
