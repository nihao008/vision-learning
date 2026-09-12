class ImageData:
    def __init__(self, name, label):
        self.name = name    # 空1
        self.label = label   # 空2

    def print_info(self):
        print(self.name, self.label)    # 空3：打印两个属性

# 下面创建 3 个实例并调用 print_info()
img1 = ImageData("img_001.jpg", "划痕")
img1.print_info()
img2 =  ImageData("什么","答案")
img2.print_info()
img3 =  ImageData("名字","类别")
img3.print_info()
# ...再补 2 个实例（换数据）
