import cv2

img = cv2.imread(r"D:\python\yolov11\pose5\train\images\frame_000000.jpg")
h, w = img.shape[:2]   # 取高和宽

with open(r"D:\python\yolov11\pose5\train\labels\frame_000000.txt", "r") as f:
    line = f.readline()

parts = line.split()
x_c, y_c, bw, bh = float(parts[1]), float(parts[2]), float(parts[3]), float(parts[4])

# 核心：归一化坐标(0~1比例) → 像素坐标
x1 = int((x_c - bw / 2) * w)    # 框左上角 x
y1 = int((y_c - bh / 2) * h)    # 框左上角 y
x2 = int((x_c + bw / 2) * w)    # 框右下角 x
y2 = int((y_c + bh / 2) * h)    # 框右下角 y

cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)   # 画绿框

kpts = parts[5:]                # 第5个开始全是关键点数据
for i in range(0, len(kpts), 3):        # 每3个数一组（x, y, v）
    kx = int(float(kpts[i]) * w)        # 关键点 x → 像素
    ky = int(float(kpts[i + 1]) * h)    # 关键点 y → 像素
    cv2.circle(img, (kx, ky), 6, (0, 0, 255), -1)   # 画红点

cv2.imwrite(r"D:\python\yolov11\pose5\check_frame_000000.jpg", img)
print("画完了，去 D:\\python\\yolov11\\pose5\\ 找 check_frame_000000.jpg")

