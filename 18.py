import torch

# 1. 造数据：真实关系是 y = 2*x + 3，加点噪声
x = torch.rand(100, 1) * 10
y = 2 * x + 3 + torch.randn(100, 1)

# 2. 随机猜一个 w 和 b（电脑一开始瞎猜）
w = torch.randn(1, 1, requires_grad=True)   # requires_grad=True = "这个参数要学"
b = torch.randn(1, 1, requires_grad=True)

# 3. 训练 100 轮
for i in range(100):
    pred = x @ w + b                  # 用当前 w,b 预测
    loss = ((pred - y) ** 2).mean()   # 误差（预测和真实差多少）

    loss.backward()                   # 自动算梯度（反向传播）

    with torch.no_grad():             # 更新参数时不算梯度
        w -= 0.01 * w.grad            # 沿着梯度方向调一点
        b -= 0.01 * b.grad
        w.grad.zero_()                # 梯度清零（下一轮重算）
        b.grad.zero_()

    if i % 20 == 0:
        print(f"第{i:3d}轮  loss={loss.item():8.3f}  w={w.item():.2f}  b={b.item():.2f}")

print("--- 结果 ---")
print(f"学到的 w = {w.item():.2f} （真实是 2）")
print(f"学到的 b = {b.item():.2f} （真实是 3）")
