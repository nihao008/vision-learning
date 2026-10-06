# vision-learning

机器视觉工程师自学项目：从 Python 基础到 YOLO 训练与部署的完整练习记录。

## 技术栈
- Python、OpenCV、NumPy、PyTorch
- YOLO11（检测/姿态估计）
- 命令行工具（argparse）、配置文件（yaml）、日志（logging）
- 模型导出 ONNX 部署

## 目录结构
| 文件 | 内容 |
|---|---|
| 11.py | YOLO 标注解析与数据集统计 |
| 12.py | OpenCV 读图与可视化标注 |
| 13.py | 传统视觉：灰度/模糊/二值化/轮廓/形态学 |
| 14.py | YOLO 单图推理 |
| 15.py | 批量推理工具 |
| 16.py | NumPy 数组操作 |
| 17.py | PyTorch 张量与 GPU |
| 18.py | 手写最小训练循环（理解梯度下降） |
| 19.py | YOLO GPU 训练 |
| 20.py | 带日志与错误处理的批量推理 |
| 21.py | yaml 配置文件读取 |
| 22.py | 配置文件驱动训练 |
| 23.py | 模型导出 ONNX 并推理 |

## 硬件
- RTX 4060 Laptop GPU，CUDA 可用
