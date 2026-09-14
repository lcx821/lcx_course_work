"""用 torch.nn 定义神经网络并完成一个微型训练循环（对应「使用 torch.nn 创建并训练神经网络」）。"""
import torch
from torch import nn

torch.manual_seed(0)

# 1. 定义两层回归网络、损失函数与优化器
model = nn.Sequential(
    nn.Linear(1, 16),
    nn.ReLU(),
    nn.Linear(16, 1),
)
loss_fn = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.05)

# 2. 训练数据：目标函数 y = 3x - 2
X = torch.linspace(-1, 1, 32).unsqueeze(1)
y_true = 3 * X - 2

# 3. 训练循环：清零梯度 -> 前向 -> 反向 -> 更新参数
for step in range(501):
    optimizer.zero_grad()
    y_pred = model(X)
    loss = loss_fn(y_pred, y_true)
    loss.backward()
    optimizer.step()
    if step % 100 == 0:
        print(f"step {step:3d}  loss {loss.item():.6f}")

# 4. 训练后预测
with torch.no_grad():
    pred = model(torch.tensor([[0.5]])).item()
print(f"predict x=0.5 -> {pred:.4f} (目标 -0.5)")
