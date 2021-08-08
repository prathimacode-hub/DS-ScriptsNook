# Social Distance Detection
Social distancing in Real-Time using live camera feed using OpenCV.

- Count the number of people in the stores/buildings, malls  etc., in real-time.
- Sending an alert to the staff if the people are way over the social distancing limits.
- Optimizing the real-time stream for better performance (with threading).
- Acts as a measure to tackle COVID-19.

---

## References
***Main:***
- YOLOv3 paper: https://arxiv.org/pdf/1804.02767.pdf
- YOLO original paper: https://arxiv.org/abs/1506.02640
- YOLO TensorFlow implementation (darkflow): https://github.com/thtrieu/darkflow

***Optional:***
- More theory: https://www.pyimagesearch.com/2018/11/12/yolo-object-detection-with-opencv/
- Other trained model weights from official doc: https://pjreddie.com/darknet/yolo/

---
## Requirements:

    You will need the following to run this code:
    Python 3.5.2
    Opencv(CV2) 4.2.0
    numpy 1.14.5
    argparse
    
    For human detection:
    yolov3.weights, yolov3.cfg files (weights file in not present because of size issue. It can be downloaded from 
    here : https://pjreddie.com/media/files/yolov3.weights)
    
    For running: 
    Good GPU, for faster results. CPU is also fine(I have tried it on CPU).
    

