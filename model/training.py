from ultralytics import YOLO

# model = YOLO('yolov8s.pt')
# model.train(data='./dataset1/data.yaml', epochs=20, imgsz=640, batch=8)
model2 = YOLO('runs/detect/train/weights/best.pt')
model2.train(data='./dataset2/data.yaml', epochs=20, imgsz=640, batch=8)
model3 = YOLO('runs/detect/train2/weights/best.pt')
model3.train(data='./dataset3/data.yaml', epochs=20, imgsz=640, batch=8)

