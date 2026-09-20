import cv2

img = cv2.imread(r"D:\python\yolov11\pose5\train\images\frame_000000.jpg")

# 1. 转灰度（彩色3通道 -> 单通道灰度图）
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2. 高斯模糊（降噪，让边缘更平滑，缺陷检测前必做）
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# 3. 二值化（亮于127的变纯白，暗于127的变纯黑）
_, thresh = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY_INV)

# 保存三张对比图
cv2.imwrite(r"D:\python\yolov11\pose5\out_gray.jpg", gray)
cv2.imwrite(r"D:\python\yolov11\pose5\out_blur.jpg", blur)
cv2.imwrite(r"D:\python\yolov11\pose5\out_thresh.jpg", thresh)

print("原图:", img.shape)
print("灰度图:", gray.shape)
print("完成，去 pose5 文件夹看三张结果图")

# 反转：让后视镜变白、背景变黑（重要！）
thresh_inv = cv2.bitwise_not(thresh)
import numpy as np

kernel = np.ones((5, 5), np.uint8)       # 5×5 的小矩阵（"刷子"）

# 开运算：先腐蚀后膨胀 → 去掉小白噪点
opened = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

# 闭运算：先膨胀后腐蚀 → 填上物体内部的小黑洞
closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel)

cv2.imwrite(r"D:\python\yolov11\pose5\out_clean.jpg", closed)   # 看清洗后的二值图

# 找轮廓
contours, _ = cv2.findContours(thresh_inv, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("找到轮廓数:", len(contours))

result = img.copy()

for c in contours:
    area = cv2.contourArea(c)        # 算这个轮廓的面积
    if area < 5000:                   # 太小的（噪点）跳过
        continue
    x, y, w, h = cv2.boundingRect(c) # 取外接矩形：左上角+宽高
    cv2.rectangle(result, (x, y), (x + w, y + h), (0, 0, 255), 2)
    print("保留的轮廓面积:", area)

cv2.imwrite(r"D:\python\yolov11\pose5\out_contours.jpg", result)
print("完成，去看 out_contours.jpg")
