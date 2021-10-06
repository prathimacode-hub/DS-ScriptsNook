
# :fleur_de_lis: Implementation of RANSAC Algorithm 
## :nazar_amulet:  Objective:
 To clean dataset from noise using RANSAC Algorithm
## :nazar_amulet:  what is RANSAC Algorithm?
The RANSAC algorithm is a learning technique to estimate parameters of a model by random sampling of observed data. The RANSAC algorithm is essentially composed of two steps that are iteratively repeated:

:sparkle:In the first step, a sample subset containing minimal data items is randomly selected from the input dataset. fitting model and the corresponding model parameters are computed using only the elements of this sample subset. The cardinality of the sample subset is the smallest sufficient to determine the model parameters.

:sparkle:In the second step, the algorithm checks which elements of the entire dataset are consistent with the model instantiated by the estimated model parameters obtained from the first step. A data element will be considered as an outlier if it does not fit the fitting model instantiated by the set of estimated model parameters within some error threshold that defines the maximum deviation attributable to the effect of noise.
<p align="center">
  <img width="300" height="200" src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Line_with_outliers.svg/383px-Line_with_outliers.svg.png">
  </p>
  
 #### A data set with many outliers for which a line has to be fitted
 
 <p align="center">
  <img width="300" height="200" src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Fitted_line.svg/383px-Fitted_line.svg.png">
  </p>
  
  #### Fitted line with RANSAC; outliers have no influence on the result.
 

## :nazar_amulet:  Implementation:
I have used Cafe dataset where it detects the outlier in the image. X axis is taken as avg no of cafes opened and Y axis as total cafes in the city.
## :nazar_amulet:  Output:
<p align="center">
  <img width="600" height="500" src="https://user-images.githubusercontent.com/66861391/136230373-20d5144d-47d1-4506-a48b-4234be563953.png">
  </p>
  
## :nazar_amulet: Applications:
The RANSAC algorithm is often used in computer vision, e.g., to simultaneously solve the correspondence problem and estimate the fundamental matrix related to a pair of stereo cameras; see also: Structure from motion, scale-invariant feature transform, image stitching, rigid motion segmentation.
