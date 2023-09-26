#pip install ultralytics
from ultralytics import YOLO
from PIL import Image
model = YOLO('D:\SEM 7\MINI PROJECT\yolov8m_b8_50e2\weights\\best.pt')  # pretrained YOLOv8n model

# Run batched inference on a list of images
# results = model(['D:\SEM 7\MINI PROJECT\ADB03TE193684491_jpg.rf.270cedd023118d817d90f97e393bcfd5.jpg'],iou=0.2,save=True,show=True)  # return a list of Results objects

# # Process results list
# for result in results:
#     boxes = result.boxes  # Boxes object for bbox outputs
#     masks = result.masks  # Masks object for segmentation masks outputs
#     keypoints = result.keypoints  # Keypoints object for pose outputs
#     probs = result.probs  # Probs object for classification outputs
#     print(boxes)

# for r in results:
#     im_array = r.plot()  # plot a BGR numpy array of predictions
#     im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
#     im.show()  # show image
#     im.save('results.jpg')  # save image

import cv2


# Open the video file
video_path = "C:\\Users\Keertana\Downloads\stock-footage-pushkar-rajasthan-india-aug-tourism-camel-carts-and-traffic-on-august-in-pushkar.webm"
cap = cv2.VideoCapture(video_path)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        results = model(frame)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        cv2.imshow("YOLOv8 Inference", annotated_frame)