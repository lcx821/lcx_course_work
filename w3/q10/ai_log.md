# ai_log
1. 核心提示：修复纯空白 --name 仍输出问候并以 0 退出的缺陷；目标 main 对空白姓名以 SystemExit(2) 结束；约束只改实现不改测试；测试命令：cd q10 后运行 PYTHONPATH=src python -m pytest -v。
2. 智能体改动：cli.py 的 main 增加 argv 参数，parse 后校验 a.name.strip()，空白时调用 p.error 使退出码为 2。
3. 人工验证：diff 确认仅 cli.py 有预期改动且无无关修改；再次运行 pytest 全部通过。
