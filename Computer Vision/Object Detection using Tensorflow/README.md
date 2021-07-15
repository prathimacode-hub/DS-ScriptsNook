# <center>OBJECT DETECTION USING TENSORFLOW</center>

**INTRODUCTION**

TensorFlow Object Detection API.The TensorFlow object detection API is a software framework used for object detection tasks. Tensorflow Object Detection API and other similar APIs (Keras RCNN, YOLO) uses pre trained CNNs inside the framworks for predictions. Most of those pretrained models are trained using, the COCO dataset, the KITTI dataset, and the Open Images Dataset. These models are trained to detect some fixed type of categories of objects such as, persons, cars, dog, tooth brush and etc. If you want to detect custom objects you can retrain those models using your own datasets.

**PURPOSE**

The main purpose of this project is to detect objects in images using pre-trained SSD MobileNet model from tensorflow API.

**WHAT IS OBJECT DETECTION?**

Object detection is a computer vision technique in which a software system can detect, locate, and trace the object from a given image or video.It identifies the class of object (person, table, chair, etc.) and their location-specific coordinates in the given image. The location is pointed out by drawing a bounding box around the object. The bounding box may or may not accurately locate the position of the object. The ability to locate the object inside an image defines the performance of the algorithm used for detection. Face detection is one of the examples of object detection.

**HOW DOES OBJECT DETECTION WORKS?**

Generally, the object detection task is carried out in three steps:

- Generates the small segments in the input as shown in the image below. As you can see the large set of bounding boxes are spanning the full image:
  ![AL](https://d1m75rqqgidzqn.cloudfront.net/wp-data/2020/07/23225454/121-905x420.jpg)
- Feature extraction is carried out for each segmented rectangular area to predict whether the rectangle contains a valid object.
  ![](https://d1m75rqqgidzqn.cloudfront.net/wp-data/2020/07/23225516/2-432x420.jpg)
- Overlapping boxes are combined into a single bounding rectangle (Non-Maximum Suppression)
  ![](https://d1m75rqqgidzqn.cloudfront.net/wp-data/2020/07/23225538/3-437x420.jpg)
  
**WHAT IS AN API? WHY DO WE NEED AN API?**
- API stands for Application Programming Interface. An API provides developers a set of common operations so that they don’t have to write code from scratch.
  
**WHAT IS TENSORFLOW OBJECT DETECTION API**
- The TensorFlow Object Detection API is an open-source framework built on top of TensorFlow that makes it easy to construct, train and deploy object detection models.

  - There are already pre-trained models in their framework which are referred to as Model Zoo. 
       - It includes a collection of pre-trained models trained on various datasets such as the 
            - COCO (Common Objects in Context) dataset, 
            - the KITTI dataset, 
            - and the Open Images Dataset.
      - They are also useful for initializing your models when training on the novel dataset. The various architectures used in the pretrained model are described in this table:
       
          ![](https://cdn.analyticsvidhya.com/wp-content/uploads/2020/04/9.jpeg)
          
  -    ### We will be using **MobileNet-SSD** pre-trained model here for Object Detection.
            
## **MobileNet-SSD**

- MobilenetSSD is an object detection model that computes the bounding box and category of an object from an input image. 
- This Single Shot Detector (SSD) object detection model uses Mobilenet as backbone and can achieve fast object detection optimized for mobile devices.
- The SSD architecture is a single convolution network that learns to predict bounding box locations and classify these locations in one pass. Hence, SSD can be trained end-to-end. 
- By using SSD, we only need to **take one single shot to detect multiple objects within the image**, while regional proposal network (RPN) based approaches such as R-CNN series that need two shots, one for generating region proposals, one for detecting the object of each proposal. 
- Thus, SSD is much faster compared with two-shot RPN-based approaches.
- The SSD network consists of base architecture (MobileNet in this case) followed by several convolution layers:
- ![](https://cdn.analyticsvidhya.com/wp-content/uploads/2020/04/10.png)
- SSD operates on feature maps to detect the location of bounding boxes. Remember – a feature map is of the size Df * Df * M. For each feature map location, k bounding boxes are predicted. Each bounding box carries with it the following information:
     - 4 corner bounding box offset locations (cx, cy, w, h)
     - C class probabilities (c1, c2, …cp)
- SSD does not predict the shape of the box, rather just where the box is. The k bounding boxes each have a predetermined shape. The shapes are set prior to actual training. For example, in the figure above, there are 4 boxes, meaning k=4.
- Boxes contains offset values (cx,cy,w,h) from the default box. Scores contains confidence values for the presence of each of the object categories.




**WORKING CONDITIONS**

Follow these steps to run this project :
- Download Tensorflow object detection API from this link : https://github.com/tensorflow/models
 (Clone the Zip of directory into your local machine.) You can find the folder models/research/object detection
 - Install the following dependencies for Windows:
   - Open the Anaconda Prompt and install the dependencies for windows,
        - pip install tensorflow==2.4.1
        - pip install Cython
        - pip install contextlib2
        - pip install pillow
        - pip install lxml
        - pip install jupyter
        - pip install matplotlib
        - pip install tf_slim
        - pip install opencv-python
  - We need Protobuff Compiler in order to compile the model.
    -  Download protobuff compiler- protoc-3.17.3-win64.zip from here: https://github.com/protocolbuffers/protobuf/releases/tag/v3.17.3
    -  From the zip folde, in bin folder move the file protoc.exe into models/research/
  - Open command prompt into the Models/research folder and run this code:
     - for /f %i in ('dir /b object_detection\protos\*.proto') do protoc object_detection\protos\%i --python_out=.
  - Move the main Model Notebook to the folder models/research/
  - Copy the test images from Images folder(in the repo) and move it to models/research/object detection/test-images
  - You are good to go now! Run this Notebook.


**USE CASES**

 Object detection and recognition is applied in many areas of computer vision, including image retrieval, security, surveillance, automated vehicle systems and machine inspection.

**LIBRARIES USED**
- NumPy
- OS
- Tensorflow
- urllibs
- pathlib
- zipfile
- PIL
- IPython

**CONCLUSION**
- The model can precisely detect objects in the picture with good score and recognise the correct label of the objects.

**REFERENCES**
- https://www.mygreatlearning.com/blog/object-detection-using-tensorflow/
- https://medium.com/axinc-ai/mobilenetssd-a-machine-learning-model-for-fast-object-detection-37352ce6da7d
- https://medium.com/@techmayank2000/object-detection-using-ssd-mobilenetv2-using-tensorflow-api-can-detect-any-single-class-from-31a31bbd0691

**Created By :**

- --> Name : Shivani Rana
- --> Connect with me on [Github](https://github.com/shivani6320), [LinkedIn](https://www.linkedin.com/in/shivani-rana-b833a91a3/) and [Kaggle](https://www.kaggle.com/shivanirana63) 
