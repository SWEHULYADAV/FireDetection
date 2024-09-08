**************************************************************************************************************************
File Structure
**************************************************************************************************************************
Branding/
│
├── fire/  # Main dataset folder
│   ├── train/  # Training data folder
│   │   ├── images/  # Contains training images
│   │   │   ├── image1.jpg
│   │   │   ├── image2.png
│   │   │   └── ...
│   │   ├── labels/  # Contains training labels (YOLO format)
│   │   │   ├── image1.txt
│   │   │   ├── image2.txt
│   │   │   └── ...
│   ├── val/  # Validation data folder
│   │   ├── images/  # Contains validation images
│   │   │   ├── image1.jpg
│   │   │   ├── image2.png
│   │   │   └── ...
│   │   ├── labels/  # Contains validation labels (YOLO format)
│   │   │   ├── image1.txt
│   │   │   ├── image2.txt
│   │   │   └── ...
│   ├── data.yaml  # YOLOv8 dataset configuration file
│
├── venv/  # Virtual environment for Python dependencies
│   ├── Scripts/
│   └── ...
│
├── model_output/  # Directory where the trained model will be saved
│   ├── runs/  # YOLO output logs and trained models
│   └── ...
│
├── Fire100/  # Folder containing the alarm sound
│   ├── alarm.mp3  # Alarm sound file to play when fire is detected
│
├── fire.py  # Python script to run training or inference
│
├── yolov10x.pt  # Pre-trained YOLO model (should be here for the current project)
│
└── README.md  # Documentation or project information (optional)
==========================================================================================================================
|                                                                                                                        |
|                                                                                                                        |
|                                                                                                                        |
|                                                                                                                        |
|                                                                                                                        |
**************************************************************************************************************************
Excecution Commands
**************************************************************************************************************************
1).
python -m venev venv

2).

./venv/Scripts/activate

3).

pip install -r requirements.txt

4).

yolo train data=fire/data.yaml model=yolov8x.pt epochs=50 imgsz=640             #Training Command

'''
Dataset Configuration:
The dataset configuration is provided in fire/data.yaml.
Pre-trained Model:
The training starts from the weights of the pre-trained YOLOv8x model (yolov8x.pt).
Training Duration:
The training will run for 50 epochs.
Image Size:
Input images will be resized to 640x640 pixels.
'''

5).

python fire.py

==========================================================================================================================
