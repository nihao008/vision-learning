import argparse
import os
import cv2
from ultralytics import YOLO

def main():
    parser = argparse.ArgumentParser(description="批量推理工具")
    parser.add_argument("--source_dir", type=str,
                        default=r"D:\python\yolov11\pose5\train\images",
                        help="图片文件夹")
    parser.add_argument("--model", type=str,
                        default=r"D:\python\yolov11\runs\pose\train32\weights\best1.pt",
                        help="模型权重")
    parser.add_argument("--out_dir", type=str,
                        default=r"D:\python\yolov11\pose5\batch_out",
                        help="输出文件夹")
    parser.add_argument("--limit", type=int, default=10, help="只跑前N张（先少量试）")
    args = parser.parse_args()

    os.makedirs(args.out_dir, exist_ok=True)
    model = YOLO(args.model)

    # 空1：列出文件夹里所有 .jpg（第10题 + 任务1.3技能）
    images = [ f for f in os.listdir(args.source_dir) if f.endswith(".jpg") ]
    images = images[:args.limit]    # 只跑前 limit 张

    for img_name in images:
        # 空2：拼图片完整路径
        img_path = os.path.join(args.source_dir, img_name)

        results = model(img_path)
        plotted = results[0].plot()

        # 空3：拼输出路径（保存到 out_dir，文件名和原图一样）
        out_path = os.path.join(args.out_dir, img_name)
        cv2.imwrite(out_path, plotted)
        print("已处理:", img_name)

    print("全部完成，共", len(images), "张，输出在", args.out_dir)

if __name__ == "__main__":
    main()
