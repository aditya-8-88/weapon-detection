import cv2
import numpy as np

# Load pre-trained YOLO model
config_path = "yolov3_testing.cfg"
weights_path = ""
net = cv2.dnn.readNetFromDarknet(config_path, weights_path)

# Load class labels
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Set minimum confidence threshold and non-maximum suppression threshold
confidence_threshold = 0.5
nms_threshold = 0.4

# Load input image or video
image_path = "image.jpg"
cap = cv2.VideoCapture("video.mp4")

while True:
    # Read frame from the video
    ret, frame = cap.read()

    if not ret:
        break

    # Preprocess input frame
    blob = cv2.dnn.blobFromImage(frame, 1 / 255, (416, 416), swapRB=True, crop=False)

    # Perform object detection
    net.setInput(blob)
    outputs = net.forward(get_output_layers(net))

    # Process the detected objects
    class_ids = []
    confidences = []
    boxes = []
    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > confidence_threshold and classes[class_id] == "gun":
                # Calculate bounding box coordinates
                center_x = int(detection[0] * frame.shape[1])
                center_y = int(detection[1] * frame.shape[0])
                width = int(detection[2] * frame.shape[1])
                height = int(detection[3] * frame.shape[0])
                left = int(center_x - width / 2)
                top = int(center_y - height / 2)

                class_ids.append(class_id)
                confidences.append(float(confidence))
                boxes.append([left, top, width, height])

    # Apply non-maximum suppression to eliminate overlapping boxes
    indices = cv2.dnn.NMSBoxes(boxes, confidences, confidence_threshold, nms_threshold)

    # Draw bounding boxes and labels
    for i in indices:
        i = i[0]
        box = boxes[i]
        left, top, width, height = box
        cv2.rectangle(frame, (left, top), (left + width, top + height), (0, 255, 0), 2)
        cv2.putText(frame, "Weapon", (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow("Weapon Detection", frame)
    if cv2.waitKey(1) == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()











# import cv2
# import numpy as np


# # Load Yolo
# # Download weight file(yolov3_training_2000.weights) from this link :- https://drive.google.com/file/d/10uJEsUpQI3EmD98iwrwzbD4e19Ps-LHZ/view?usp=sharing
# net = cv2.dnn.readNet("yolov3_training_2000.weights", "yolov3_testing.cfg")
# classes = ["Weapon"]
# # with open("coco.names", "r") as f:
# #     classes = [line.strip() for line in f.readlines()]

# layer_names = net.getLayerNames()
# output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
# colors = np.random.uniform(0, 255, size=(len(classes), 3))


# # Loading image
# # img = cv2.imread("room_ser.jpg")
# # img = cv2.resize(img, None, fx=0.4, fy=0.4)

# # Enter file name for example "ak47.mp4" or press "Enter" to start webcam
# def value():
#     val = input("Enter file name or press enter to start webcam : \n")
#     if val == "":
#         val = 0
#     return val


# # for video capture
# cap = cv2.VideoCapture(value())

# # val = cv2.VideoCapture()
# while True:
#     _, img = cap.read()
#     height, width, channels = img.shape
#     # width = 512
#     # height = 512

#     # Detecting objects
#     blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

#     net.setInput(blob)
#     outs = net.forward(output_layers)

#     # Showing information on the screen
#     class_ids = []
#     confidences = []
#     boxes = []
#     for out in outs:
#         for detection in out:
#             scores = detection[5:]
#             class_id = np.argmax(scores)
#             confidence = scores[class_id]
#             if confidence > 0.5:
#                 # Object detected
#                 center_x = int(detection[0] * width)
#                 center_y = int(detection[1] * height)
#                 w = int(detection[2] * width)
#                 h = int(detection[3] * height)

#                 # Rectangle coordinates
#                 x = int(center_x - w / 2)
#                 y = int(center_y - h / 2)

#                 boxes.append([x, y, w, h])
#                 confidences.append(float(confidence))
#                 class_ids.append(class_id)

#     indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
#     print(indexes)
#     if indexes == 0: print("weapon detected in frame")
#     font = cv2.FONT_HERSHEY_PLAIN
#     for i in range(len(boxes)):
#         if i in indexes:
#             x, y, w, h = boxes[i]
#             label = str(classes[class_ids[i]])
#             color = colors[class_ids[i]]
#             cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
#             cv2.putText(img, label, (x, y + 30), font, 3, color, 3)

#     # frame = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
#     cv2.imshow("Image", img)
#     key = cv2.waitKey(1)
#     if key == 27:
#         break
# cap.release()
# cv2.destroyAllWindows()
