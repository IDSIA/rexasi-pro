from ultralytics import YOLO

model = YOLO("yolov8n.yaml")
results = model.train(data="robomaster.yaml", epochs=10)

