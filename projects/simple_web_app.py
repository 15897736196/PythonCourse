# Python学习项目 - 实际项目：简易Web应用
# 学习序号：第8阶段 第3课 - Web应用项目
# 建议学习时间：180-240分钟
# 前置知识：第1-7阶段 - 完整Python基础
# 下一课：🎉 恭喜完成Python学习项目！可以开始自己的项目开发了
# 本项目展示如何使用Flask构建一个简单的Web应用

"""
简易Web应用功能特性:
1. 基本的Web路由和视图函数
2. HTML模板渲染
3. 表单处理和数据提交
4. 会话管理和用户状态
5. 简单的留言板功能
6. RESTful API接口
7. 错误处理和日志记录
8. 静态文件服务
"""

from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash
import json
import os
from datetime import datetime
from typing import List, Dict, Any
import secrets

# ===== 数据模型 =====

class Message:
    """留言类"""

    def __init__(self, author: str, content: str, category: str = "general"):
        self.id = secrets.token_hex(8)  # 生成唯一ID
        self.author = author
        self.content = content
        self.category = category
        self.timestamp = datetime.now()
        self.likes = 0

    def to_dict(self) -> Dict[str, Any]:
        """转换为字典"""
        return {
            'id': self.id,
            'author': self.author,
            'content': self.content,
            'category': self.category,
            'timestamp': self.timestamp.isoformat(),
            'likes': self.likes
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Message':
        """从字典创建实例"""
        message = cls(data['author'], data['content'], data['category'])
        message.id = data['id']
        message.timestamp = datetime.fromisoformat(data['timestamp'])
        message.likes = data.get('likes', 0)
        return message

class MessageBoard:
    """留言板类"""

    def __init__(self, data_file: str = "messages.json"):
        self.data_file = data_file
        self.messages: List[Message] = []
        self.load_messages()

    def load_messages(self) -> None:
        """加载留言"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.messages = [Message.from_dict(msg_data) for msg_data in data]
        except (json.JSONDecodeError, IOError) as e:
            print(f"加载留言失败: {e}")
            self.messages = []

    def save_messages(self) -> None:
        """保存留言"""
        try:
            data = [msg.to_dict() for msg in self.messages]
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except IOError as e:
            print(f"保存留言失败: {e}")

    def add_message(self, author: str, content: str, category: str = "general") -> Message:
        """添加留言"""
        message = Message(author, content, category)
        self.messages.append(message)
        self.save_messages()
        return message

    def get_message(self, message_id: str) -> Message:
        """获取留言"""
        for message in self.messages:
            if message.id == message_id:
                return message
        raise ValueError(f"留言不存在: {message_id}")

    def delete_message(self, message_id: str) -> bool:
        """删除留言"""
        for i, message in enumerate(self.messages):
            if message.id == message_id:
                del self.messages[i]
                self.save_messages()
                return True
        return False

    def like_message(self, message_id: str) -> bool:
        """点赞留言"""
        message = self.get_message(message_id)
        message.likes += 1
        self.save_messages()
        return True

    def get_messages_by_category(self, category: str) -> List[Message]:
        """按分类获取留言"""
        return [msg for msg in self.messages if msg.category == category]

    def search_messages(self, keyword: str) -> List[Message]:
        """搜索留言"""
        keyword_lower = keyword.lower()
        return [msg for msg in self.messages
                if keyword_lower in msg.content.lower()
                or keyword_lower in msg.author.lower()]

# ===== Flask应用设置 =====

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # 随机生成密钥

# 创建模板文件夹和静态文件夹
os.makedirs('templates', exist_ok=True)
os.makedirs('static', exist_ok=True)
os.makedirs('static/css', exist_ok=True)
os.makedirs('static/js', exist_ok=True)

# 初始化留言板
message_board = MessageBoard()

# ===== HTML模板 =====

# 基础模板
base_template = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Python留言板{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="{{ url_for('static', filename='css/style.css') }}" rel="stylesheet">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container">
            <a class="navbar-brand" href="{{ url_for('home') }}">🐍 Python留言板</a>
            <div class="navbar-nav ms-auto">
                {% if session.get('username') %}
                    <span class="navbar-text me-3">欢迎，{{ session.username }}！</span>
                    <a class="nav-link" href="{{ url_for('logout') }}">登出</a>
                {% else %}
                    <a class="nav-link" href="{{ url_for('login') }}">登录</a>
                {% endif %}
            </div>
        </div>
    </nav>

    <div class="container mt-4">
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ 'danger' if category == 'error' else 'success' }} alert-dismissible fade show">
                        {{ message }}
                        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                    </div>
                {% endfor %}
            {% endif %}
        {% endwith %}

        {% block content %}{% endblock %}
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    <script src="{{ url_for('static', filename='js/app.js') }}"></script>
</body>
</html>
"""

# 首页模板
home_template = """
{% extends "base.html" %}

{% block title %}首页 - Python留言板{% endblock %}

{% block content %}
<div class="row">
    <div class="col-md-8">
        <div class="card">
            <div class="card-header">
                <h5>📝 最新留言</h5>
            </div>
            <div class="card-body">
                {% for message in messages %}
                <div class="message-card mb-3 p-3 border rounded">
                    <div class="d-flex justify-content-between align-items-start">
                        <div>
                            <h6 class="mb-1">
                                <span class="badge bg-secondary">{{ message.category }}</span>
                                {{ message.author }}
                            </h6>
                            <p class="mb-2">{{ message.content }}</p>
                            <small class="text-muted">
                                {{ message.timestamp.strftime('%Y-%m-%d %H:%M') }}
                            </small>
                        </div>
                        <div class="text-end">
                            <button class="btn btn-sm btn-outline-primary like-btn"
                                    data-message-id="{{ message.id }}">
                                👍 {{ message.likes }}
                            </button>
                        </div>
                    </div>
                </div>
                {% endfor %}

                {% if not messages %}
                <p class="text-muted">暂无留言，快来发表第一条留言吧！</p>
                {% endif %}
            </div>
        </div>
    </div>

    <div class="col-md-4">
        <div class="card">
            <div class="card-header">
                <h5>✍️ 发表留言</h5>
            </div>
            <div class="card-body">
                {% if session.get('username') %}
                <form method="POST" action="{{ url_for('add_message') }}">
                    <div class="mb-3">
                        <label for="category" class="form-label">分类</label>
                        <select class="form-select" id="category" name="category" required>
                            <option value="general">一般</option>
                            <option value="question">问题</option>
                            <option value="share">分享</option>
                            <option value="discussion">讨论</option>
                        </select>
                    </div>
                    <div class="mb-3">
                        <label for="content" class="form-label">内容</label>
                        <textarea class="form-control" id="content" name="content"
                                rows="4" required></textarea>
                    </div>
                    <button type="submit" class="btn btn-primary">发表留言</button>
                </form>
                {% else %}
                <p>请先 <a href="{{ url_for('login') }}">登录</a> 后再发表留言</p>
                {% endif %}
            </div>
        </div>

        <div class="card mt-3">
            <div class="card-header">
                <h5>📊 统计信息</h5>
            </div>
            <div class="card-body">
                <p>总留言数: {{ stats.total_messages }}</p>
                <p>今日留言: {{ stats.today_messages }}</p>
                <p>活跃用户: {{ stats.active_users }}</p>
            </div>
        </div>
    </div>
</div>
{% endblock %}
"""

# 登录模板
login_template = """
{% extends "base.html" %}

{% block title %}登录 - Python留言板{% endblock %}

{% block content %}
<div class="row justify-content-center">
    <div class="col-md-6">
        <div class="card">
            <div class="card-header">
                <h5>🔐 用户登录</h5>
            </div>
            <div class="card-body">
                <form method="POST">
                    <div class="mb-3">
                        <label for="username" class="form-label">用户名</label>
                        <input type="text" class="form-control" id="username"
                               name="username" required>
                    </div>
                    <div class="mb-3">
                        <label for="password" class="form-label">密码</label>
                        <input type="password" class="form-control" id="password"
                               name="password" required>
                    </div>
                    <button type="submit" class="btn btn-primary">登录</button>
                    <a href="{{ url_for('register') }}" class="btn btn-link">注册新用户</a>
                </form>
            </div>
        </div>
    </div>
</div>
{% endblock %}
"""

# ===== 路由函数 =====

@app.route('/')
def home():
    """首页"""
    messages = message_board.messages[-10:]  # 显示最新10条留言

    # 计算统计信息
    total_messages = len(message_board.messages)
    today = datetime.now().date()
    today_messages = sum(1 for msg in message_board.messages
                        if msg.timestamp.date() == today)
    active_users = len(set(msg.author for msg in message_board.messages))

    stats = {
        'total_messages': total_messages,
        'today_messages': today_messages,
        'active_users': active_users
    }

    return render_template('home.html', messages=messages, stats=stats)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """登录页面"""
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        # 简单的用户验证（实际应用中应该使用数据库）
        if username and password == 'password':  # 简化版验证
            session['username'] = username
            flash('登录成功！', 'success')
            return redirect(url_for('home'))
        else:
            flash('用户名或密码错误', 'error')

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """注册页面（简化版）"""
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        if username and password:
            session['username'] = username
            flash('注册成功并已登录！', 'success')
            return redirect(url_for('home'))
        else:
            flash('请输入有效的用户名和密码', 'error')

    return render_template('login.html')  # 复用登录模板

@app.route('/logout')
def logout():
    """登出"""
    session.pop('username', None)
    flash('已成功登出', 'success')
    return redirect(url_for('home'))

@app.route('/add_message', methods=['POST'])
def add_message():
    """添加留言"""
    if 'username' not in session:
        flash('请先登录', 'error')
        return redirect(url_for('login'))

    category = request.form.get('category', 'general')
    content = request.form.get('content', '').strip()

    if not content:
        flash('留言内容不能为空', 'error')
        return redirect(url_for('home'))

    try:
        message_board.add_message(session['username'], content, category)
        flash('留言发表成功！', 'success')
    except Exception as e:
        flash(f'发表留言失败: {str(e)}', 'error')

    return redirect(url_for('home'))

# ===== API路由 =====

@app.route('/api/messages', methods=['GET'])
def get_messages_api():
    """获取留言API"""
    category = request.args.get('category')
    search = request.args.get('search')

    messages = message_board.messages

    if category:
        messages = message_board.get_messages_by_category(category)

    if search:
        messages = message_board.search_messages(search)

    # 转换为字典格式
    messages_data = [msg.to_dict() for msg in messages[-20:]]  # 最新20条

    return jsonify({
        'success': True,
        'messages': messages_data,
        'count': len(messages_data)
    })

@app.route('/api/messages/<message_id>/like', methods=['POST'])
def like_message_api(message_id):
    """点赞留言API"""
    try:
        message_board.like_message(message_id)
        return jsonify({'success': True})
    except ValueError as e:
        return jsonify({'success': False, 'error': str(e)}), 404

@app.route('/api/stats')
def get_stats_api():
    """获取统计信息API"""
    total_messages = len(message_board.messages)
    today = datetime.now().date()
    today_messages = sum(1 for msg in message_board.messages
                        if msg.timestamp.date() == today)
    active_users = len(set(msg.author for msg in message_board.messages))

    # 分类统计
    categories = {}
    for msg in message_board.messages:
        categories[msg.category] = categories.get(msg.category, 0) + 1

    return jsonify({
        'total_messages': total_messages,
        'today_messages': today_messages,
        'active_users': active_users,
        'categories': categories
    })

# ===== 错误处理 =====

@app.errorhandler(404)
def page_not_found(e):
    """404错误处理"""
    return render_template('error.html', error_code=404, error_message="页面未找到"), 404

@app.errorhandler(500)
def internal_error(e):
    """500错误处理"""
    return render_template('error.html', error_code=500, error_message="服务器内部错误"), 500

# ===== 工具函数 =====

@app.context_processor
def utility_processor():
    """模板工具函数"""
    def format_datetime(dt):
        """格式化日期时间"""
        return dt.strftime('%Y-%m-%d %H:%M')

    return {'format_datetime': format_datetime}

# ===== 启动应用 =====

def create_templates():
    """创建HTML模板文件"""
    templates = {
        'base.html': base_template,
        'home.html': home_template,
        'login.html': login_template,
        'error.html': """
{% extends "base.html" %}

{% block title %}错误 {{ error_code }}{% endblock %}

{% block content %}
<div class="row justify-content-center">
    <div class="col-md-6">
        <div class="card">
            <div class="card-body text-center">
                <h1 class="display-1">{{ error_code }}</h1>
                <p class="lead">{{ error_message }}</p>
                <a href="{{ url_for('home') }}" class="btn btn-primary">返回首页</a>
            </div>
        </div>
    </div>
</div>
{% endblock %}
        """
    }

    for filename, content in templates.items():
        with open(f'templates/{filename}', 'w', encoding='utf-8') as f:
            f.write(content)

def create_static_files():
    """创建静态文件"""
    # CSS文件
    css_content = """
.message-card:hover {
    background-color: #f8f9fa;
}

.like-btn:hover {
    background-color: #e3f2fd;
}

.navbar-brand {
    font-weight: bold;
}

.card {
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
    """

    # JavaScript文件
    js_content = """
document.addEventListener('DOMContentLoaded', function() {
    // 点赞功能
    document.querySelectorAll('.like-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const messageId = this.getAttribute('data-message-id');
            const btnElement = this;

            fetch(`/api/messages/${messageId}/like`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    const currentLikes = parseInt(btnElement.textContent.split(' ')[1]);
                    btnElement.innerHTML = `👍 ${currentLikes + 1}`;
                }
            })
            .catch(error => {
                console.error('点赞失败:', error);
                alert('点赞失败，请稍后重试');
            });
        });
    });
});
    """

    with open('static/css/style.css', 'w', encoding='utf-8') as f:
        f.write(css_content)

    with open('static/js/app.js', 'w', encoding='utf-8') as f:
        f.write(js_content)

def main():
    """主函数"""
    # 创建必要的文件和目录
    create_templates()
    create_static_files()

    print("🚀 启动Python留言板Web应用...")
    print("📱 访问 http://localhost:5000 查看应用")
    print("🛑 按 Ctrl+C 停止服务器")
    print()

    # 启动Flask应用
    app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == "__main__":
    main()
