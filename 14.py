import argparse
import cv2
from ultralytics import YOLO

def main():
    parser = argparse.ArgumentParser(description="YOLO 推理工具")
    parser.add_argument("--source", type=str,
                        default=r"D:\python\yolov11\pose5\train\images\frame_000000.jpg",
                        help="要检测的图片")
    parser.add_argument("--model", type=str,
                        default=r"D:\python\yolov11\runs\pose\train32\weights\best1.pt",
                        help="训练好的模型权重")
    args = parser.parse_args()

    # 加载模型
    model = YOLO(args.model)

    # 推理
    results = model(args.source)

    # 把结果画出来（ultralytics 自带画框）
    plotted = results[0].plot()

    # 保存
    cv2.imwrite(r"D:\python\yolov11\pose5\predict_out.jpg", plotted)
    print("完成，去看 predict_out.jpg")

if __name__ == "__main__":
    main()
