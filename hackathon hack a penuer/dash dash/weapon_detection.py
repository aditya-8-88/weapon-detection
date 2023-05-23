








































































# import cv2
# import numpy as np

# # Load YOLO weights and configuration
# net = cv2.dnn.readNetFromDarknet('yolov3.cfg', 'yolov3.weights')

# # Specify the names of classes that the YOLO model can detect
# classes = []
# with open('coco.names', 'r') as f:
#     classes = [line.strip() for line in f.readlines()]

# # Set the minimum confidence threshold for detection
# conf_threshold = 0.5

# # Set the non-maximum suppression threshold
# nms_threshold = 0.4

# # Load video file
# video_path = 'path/to/video/file.mp4'
# capture = cv2.VideoCapture(video_path)

# while True:
#     ret, frame = capture.read()
#     if not ret:
#         break
    
#     # Perform weapon detection
#     blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)
#     net.setInput(blob)
#     layer_names = net.getLayerNames()
#     output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
#     outs = net.forward(output_layers)

#     height, width, _ = frame.shape

#     class_ids = []
#     confidences = []
#     boxes = []

#     for out in outs:
#         for detection in out:
#             scores = detection[5:]
#             class_id = np.argmax(scores)
#             confidence = scores[class_id]

#             if confidence > conf_threshold and classes[class_id] == 'gun':
#                 center_x = int(detection[0] * width)
#                 center_y = int(detection[1] * height)
#                 w = int(detection[2] * width)
#                 h = int(detection[3] * height)

#                 x = int(center_x - w / 2)
#                 y = int(center_y - h / 2)

#                 boxes.append([x, y, w, h])
#                 confidences.append(float(confidence))
#                 class_ids.append(class_id)

#     # Apply non-maximum suppression to remove overlapping bounding boxes
#     indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)

#     # Draw bounding boxes and labels on the frame
#     for i in indices:
#         i = i[0]
#         x, y, w, h = boxes[i]
#         label = f'{classes[class_ids[i]]}: {confidences[i]:.2f}'
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#         cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

#     # Display the processed frame
#     cv2.imshow('Weapon Detection', frame)

#     if cv2.waitKey(1) == 27:
#         break

# # Release the capture and close any open windows
# capture.release()
# cv2.destroyAllWindows()

