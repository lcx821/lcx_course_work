核心提示：要求 --name 只含空白字符时 main 以 SystemExit(2) 结束，并限制只修改必要文件。
智能体改动：在 cli.py 中增加空白字符串检查，使用 argparse error 触发 SystemExit(2)。
智能体验证：运行 python3 -m pytest，测试通过。
人工验证：检查 diff 并测试正常输入 Alice，再次运行 python3 -m pytest，最终通过。

