"""PyTorch 入门：张量创建、属性与基本运算（对应教程「开始使用 PyTorch」）。"""
import torch

# 1. 从列表创建张量
x = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
print("x =")
print(x)
print("shape:", tuple(x.shape), " dtype:", x.dtype, " device:", x.device)

# 2. 特殊张量与逐元素运算
zeros = torch.zeros(2, 3)
print("zeros =")
print(zeros)
print("x + 10 =")
print(x + 10)
print("x.sum() =", x.sum().item())

# 3. 矩阵乘法
identity = torch.eye(2)
print("x @ I =")
print(x @ identity)
