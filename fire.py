import cv2
import pygame
from ultralytics import YOLO
import os

# Define paths
base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, 'runs', 'detect', 'train', 'weights', 'best.pt')
alarm_path = os.path.join(base_dir, 'Fire100', 'alarm.mp3')

# Check if model file exists
if not os.path.isfile(model_path):
    raise FileNotFoundError(f"Model file {model_path} not found.")

# Check if alarm file exists
if not os.path.isfile(alarm_path):
    raise FileNotFoundError(f"Alarm file {alarm_path} not found.")

# Load trained YOLOv8 model
model = YOLO(model_path)

# Initialize pygame mixer
pygame.mixer.init()
pygame.mixer.music.load(alarm_path)

# Function to detect fire
def detect_fire(frame):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    try:
        results = model(frame_rgb)
    except Exception as e:
        print(f"Error during inference: {e}")
        return False, frame

    detected = False
    try:
        for result in results:
            # Access the detection boxes and other attributes
            boxes = result.boxes  # This is an instance of the Boxes class
            if boxes is not None and len(boxes) > 0:
                for box in boxes:
                    class_id = int(box.cls[0])
                    class_name = model.names[class_id]
                    if class_name == 'fire':  # Ensure 'fire' matches the class name in your model
                        detected = True
                        # Draw bounding box and label
                        x1, y1, x2, y2 = map(int, [box.xyxy[0][0], box.xyxy[0][1], box.xyxy[0][2], box.xyxy[0][3]])
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                        cv2.putText(frame, f'{class_name} {box.conf[0]:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                        break
    except Exception as e:
        print(f"Error processing results: {e}")
    return detected, frame

# Initialize camera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise RuntimeError("Error: Could not open video capture device.")

alarm_played = False

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break
    
    # Detect fire
    detected, frame = detect_fire(frame)
    if detected:
        print("Fire detected!")
        if not alarm_played:
            pygame.mixer.music.play()
            alarm_played = True
    else:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        alarm_played = False

    # Display the video feed
    cv2.imshow('Fire Detection', frame)
    
    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
