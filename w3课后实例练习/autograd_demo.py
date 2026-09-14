"""autograd 自动微分：requires_grad、backward 与 .grad（对应「理解 requires_grad」教程）。"""
import torch

# requires_grad=True 表示需要跟踪该张量上的运算
x = torch.tensor(3.0, requires_grad=True)
w = torch.tensor(2.0, requires_grad=True)
b = torch.tensor(1.0, requires_grad=True)

y = w * x + b
loss = y ** 2
print("y =", y.item(), " loss =", loss.item())

# 反向传播：自动算出 loss 对各叶子张量的梯度
loss.backward()
print("d(loss)/dx =", x.grad.item(), " (手算 2*y*w =", 2 * y.item() * w.item(), ")")
print("d(loss)/dw =", w.grad.item())
print("d(loss)/db =", b.grad.item())
