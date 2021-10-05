# :nazar_amulet: Feature Extraction using Hough Transform
## :round_pushpin: Objective:
To demonstrate image feature Extraction using Hough Transform

## :round_pushpin: What is Feature Extraction?
Feature extraction is the process of defining a set of features, or image characteristics, which will most efficiently or meaningfully represent the information that is important for analysis and classification.

<p align="center">
  <img width="400" height="300" src="https://miro.medium.com/max/693/1*zUATaXMAmKof27rPyBRWsg.png">
  </p>
  
## :round_pushpin: What is Hough Transform?
The Hough transform is a popular feature extraction technique that converts an image from Cartesian to polar coordinates. Any point within the image space is represented by a sinusoidal curve in the Hough space. In addition, two points in a line segment generate two curves, which are overlaid at a location that corresponds with a line through the image space. Even though this model form is very easy, it is deeply complicated for the case of complex shapes due to noise and shape imperfection, as well as the problem of finding slopes of vertical lines.
<p align="center">
  <img width="300" height="200" src="https://ars.els-cdn.com/content/image/3-s2.0-B9780128020456000302-f30-03-9780128020456.jpg">
  </p>
  In automated analysis of digital images, a subproblem often arises of detecting simple shapes, such as straight lines, circles or ellipses. In many cases an edge detector can be used as a pre-processing stage to obtain image points or image pixels that are on the desired curve in the image space. Due to imperfections in either the image data or the edge detector, however, there may be missing points or pixels on the desired curves as well as spatial deviations between the ideal line/circle/ellipse and the noisy edge points as they are obtained from the edge detector. For these reasons, it is often non-trivial to group the extracted edge features to an appropriate set of lines, circles or ellipses. The purpose of the Hough transform is to address this problem by making it possible to perform groupings of edge points into object candidates by performing an explicit voting procedure over a set of parameterized image objects.
  <p align="center">
  <img width="300" height="200" src="https://scikit-image.org/docs/0.11.x/_images/plot_line_hough_transform_1.png">
  </p>
  
## :round_pushpin: How Feature Extraction is done using Hough Transform? 
The Circular Hough Transform (CHT) is one of the modified versions of the HT. The purpose of using CHT is to find the circular patterns within an image scene. The CHT is used to transform a set of feature points in the image space into a set of accumulated votes in a parameter space. Then, for each feature point, votes are accumulated in an accumulator array for all parameter combinations. The array elements that contain the highest number of votes indicate the presence of the shape.
## :round_pushpin: Implementation and Results:
In this code, the experimental work is implemented using python libraries linked with pycharm. Libraries like CV2 , numpy and os are really efficient and has fast processing and less time consumption for performing computer vision tasks. Pycharm is adopted as an implementation tool in our method. 

### :star2: The final result :
 <p align="center">
  <img width="600" height="450" src="https://user-images.githubusercontent.com/66861391/135981127-2be210cc-c804-4061-abad-040d194e41bb.png">
 </p>

  
## :round_pushpin: Application:
 It can be used for medical purpose to study the imperfection
## :round_pushpin: conclusion:
In this code, Binary cross image is taken for feature extraction and hough transform was implemented to find imperfect instances of objects.
