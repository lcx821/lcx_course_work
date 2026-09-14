# AGENTS.md: 给编程代理的项目说明（启动时自动加载到上下文）
## 环境
# Python 3.14，依赖装在 .venv，先 source .venv/bin/activate
## 工作规则
# 1. 修改任何 .py 文件后必须运行 mypy 类型检查
# 2. 所有函数必须带类型注解
# 3. 打包验证命令：python -m build
