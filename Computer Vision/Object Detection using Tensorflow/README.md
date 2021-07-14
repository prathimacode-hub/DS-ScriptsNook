# <center>OBJECT DETECTION USING TENSORFLOW</center>

**INTRODUCTION**

TensorFlow Object Detection API.The TensorFlow object detection API is a software framework used for object detection tasks. Tensorflow Object Detection API and other similar APIs (Keras RCNN, YOLO) uses pre trained CNNs inside the framworks for predictions. Most of those pretrained models are trained using, the COCO dataset, the KITTI dataset, and the Open Images Dataset. These models are trained to detect some fixed type of categories of objects such as, persons, cars, dog, tooth brush and etc. If you want to detect custom objects you can retrain those models using your own datasets.

**PURPOSE**

The main purpose of this project is to detect objects in images using pre-trained SSD MobileNet model from tensorflow API.

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

**Created By :**

- --> Name : Shivani Rana
- --> Connect with me on [Github](https://github.com/shivani6320), [LinkedIn](https://www.linkedin.com/in/shivani-rana-b833a91a3/) and [Kaggle](https://www.kaggle.com/shivanirana63) 
