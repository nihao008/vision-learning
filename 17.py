import torch
import numpy as np

# 1. 造张量（和 NumPy 几乎一样）
t = torch.tensor([1.0, 2.0, 3.0])
print("张量:", t)
print("形状:", t.shape)

# 2. 全0全1矩阵
zeros = torch.zeros(3, 4)
ones = torch.ones(2, 5)
print("3行4列全0:\n", zeros)

# 3. 运算（和 NumPy 一样，不用循环）
print("t * 2 =", t * 2)
print("t + t =", t + t)

# 4. 和 NumPy 互转（重点！）
arr = np.array([4.0, 5.0, 6.0])
t2 = torch.from_numpy(arr)
print("从NumPy转张量:", t2)
back = t2.numpy()
print("转回NumPy:", back)

# 5. 看你有没有 GPU
print("CUDA（显卡）可用吗:", torch.cuda.is_available())
