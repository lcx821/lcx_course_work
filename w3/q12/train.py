import torch
from torch import nn

torch.manual_seed(20260907)

x = torch.linspace(-1, 1, 101).reshape(-1, 1)
y = 3 * x - 1

model = nn.Linear(1, 1)

loss_fn = nn.MSELoss()
opt = torch.optim.SGD(model.parameters(), lr=0.1)

for _ in range(200):
    pred = model(x)
    loss = loss_fn(pred, y)

    # 清空梯度
    opt.zero_grad()

    # 反向传播
    loss.backward()

    # 更新参数
    opt.step()

# 进入评估模式
model.eval()

# 计算并打印最终结果
with torch.no_grad():
    pred = model(x)
    final_loss = loss_fn(pred, y)

    print("Final loss:", final_loss.item())
    print("Weight:", model.weight.item())
    print("Bias:", model.bias.item())
