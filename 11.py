import os

label_dir = r"D:\python\yolov11\pose5\train\labels"
files = os.listdir(label_dir)
print(files)
first = files[0]                       # 取列表里第一个文件名
path = os.path.join(label_dir, first)  # 拼成完整路径

with open(path, "r", encoding="utf-8") as f:
    for line in f:
        parts = line.split()           # 按空格拆成列表
        print("类别:", parts[0])       # 第一个数
        print("整行拆开:", parts)      # 看全部
        break                          # 只看第一行就停

print("文件路径:", path)
txt_files = [f for f in files if f.endswith(".txt")]          # 空1：只要 .txt 结尾的（第10题技能！）

class_obj_count = {}    # 类别 -> 目标总数
class_img_count = {}    # 类别 -> 图片数

for txt in txt_files:
    seen = set()        # "本文件出现过的类别"记录器
    with open(os.path.join(label_dir, txt), "r", encoding="utf-8") as f:
        for line in f:
            parts = line.split()
            cls = int(parts[0])                                # 字符串转数字
            class_obj_count[cls] = class_obj_count.get(cls, 0) + 1
            seen.add(cls)                                      # 记进"出现过的"
    for cls in seen:
        class_img_count[cls] = class_img_count.get(cls, 0) + 1

print("目标数统计:", class_obj_count)
print("图片数统计:", class_img_count)
print("总标注文件数:", len(txt_files))
