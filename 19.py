from ultralytics import YOLO

# 加载你的 pose 模型配置
model = YOLO(r"D:\python\yolov11\ultralytics\cfg\models\11\yolo11-pose.yaml")

# 先看模型结构（层数、参数量、计算量）
print(model.info())

# 用 GPU 训练（先跑 10 轮看看速度）
results = model.train(
    data="pose_train.yaml",
    epochs=10,
    imgsz=640,
    batch=8,          # GPU 显存够，开 8（CPU 时只能 2）
    device='cuda'      # 关键改动：cpu → cuda
)
