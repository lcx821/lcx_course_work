# communication.md

## Issue
- 环境：macOS，greetlab 0.1.0（是否仅 Windows 复现：待确认）
- 复现命令：sdt-greet --name " "
- 期望结果：拒绝空白姓名，退出码 2
- 实际结果：输出 "Hello, ！"，退出码 0

## 提交信息
fix: 空白姓名改为报错退出
sdt-greet 对纯空白 --name 仍输出问候并以 0 退出，易被误判为成功。在 main 校验 name.strip()，空白时以退出码 2 终止。

## 评审意见
- [Blocking] 空白姓名未校验，输出 "Hello, ！" 且退出码 0，调用方无法区分成败；建议校验后以退出码 2 拒绝。
- [Suggestion] 错误提示补充期望的合法输入；[Nit] 校验逻辑可抽成独立函数便于单测。
