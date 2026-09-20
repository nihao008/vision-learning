import numpy as np
import cv2
a = np.array([1,2,3,4,5])
print("a=",a)
print("形状：",a.shape)
print("数据类型：",a.dtype)

zeros = np.zeros((3,4))
ones = np.ones((2,5))
print("3行4列全0：\n",zeros)
print("2行5列全1：\n",ones)
b = np.array([10,20,30,40,50])
print("a+b=",a+b)
print("a*2=",a*2)

img = cv2.imread(r"D:\python\yolov11\pose5\train\images\frame_000000.jpg")

# 1. 把左上角一块矩形涂成纯红（BGR: 蓝0 绿0 红255）
img[100:300, 200:500] = [0, 0, 255]

# 2. 单独把红色通道整个抠出来看
red_channel = img[:, :, 2]
print("红色通道形状:", red_channel.shape)

# 3. 画一条竖绿线（第600列，所有行）
img[:, 600, :] = [0, 255, 0]

cv2.imwrite(r"D:\python\yolov11\pose5\numpy_edit.jpg", img)
print("完成，去看 numpy_edit.jpg")
