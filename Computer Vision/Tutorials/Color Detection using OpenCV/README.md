PROJECT TITLE - Color Detection using OpenCV

INTRODUCTION - 

We come across various searches online which involves filtering through colors. Also the filters to click images are mostly based on colors. To know how this process works, this is the project which shows the working of this procedure using python libraries.

PURPOSE - 

To extract colors from images using KMeans algorithm and filtered images from a collection of images based on RGB values of colors.
We’ve all seen that we can search online on the basis of certain filters one of which is color. Here's that process is being shown.

BRIEF EXPLANATION - 

Color detection is necessary to recognize objects, it is also used as a tool in various image editing and drawing apps. Here's a simple Python code to detect the color in the image using OpenCV and pandas. Color detection is the process of detecting the name of any color. For humans this is an extremely easy task but for computers, it is not straightforward. Human eyes and brains work together to translate light into color. Light receptors that are present in our eyes transmit the signal to the brain. Our brain then recognizes the color.

WORKING CONDITIONS:

- Importing the required libraries such as sklearn,numpy,pandas,os,collections,cv2,matplotlib and os.
- The color of the image looks a bit off when first read. This is because, by default, OpenCV reads image in the sequence Blue Green Red (BGR)
- Hence convert it to RGB format
- It must be converted to RGB mode for correct colours, the image can be converted to gray scale also.
- Further, now that we have found colours, a function is implemented to display the images having required colors
- There is a function to select those images, another function to display those images.
- In this project, there are images detected with 3 colours green, blue and yellow. 
- Other colors can also be implemented using their color proportions in RGB scale.

LIBRARIES USED - CV2 library, matplotlib library,sklearn, numpy,collections, skimage, os 

ADVANTAGES - 

Color detection in images
Converting it to gray scale
Resizing the image
Detecting hex code of colors along with their proportions in pie chart
Getting images with the required colors

APPLICATIONS - 

Image processing is made better
Light color detection
Filters can be found using the required colors

CONCLUSION - 

We got to know the methodology to extract colors from an image using KMeans algorithm and then use this to search images based on colors. How google search does it, how the image filters work. Its always better to know the process behind what we always look for in google searches.

REFERENCES :

https://medium.com/programming-fever/color-detection-using-opencv-python-6eec8dcde8c7#:~:text=Color%20detection%20is%20necessary%20to,and%20pandas%20(python%20libraries).
https://data-flair.training/blogs/project-in-python-colour-detection/
https://towardsdatascience.com/color-identification-in-images-machine-learning-application-b26e770c4c71

YOUR NAME - Vishva Rana

LinkedIN - https://www.linkedin.com/in/vishva-rana-bb60a1211/
