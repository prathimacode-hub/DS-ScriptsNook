# :fleur_de_lis: Data Fitting using RANSAC Algorithm 
## :nazar_amulet:  Objective:
 To clean dataset from noise and detect outliers using RANSAC Algorithm.
## :nazar_amulet:  Introduction
  The RANSAC algorithm was first introduced by Fischler and Bolles in 1981 as a method to estimate the parameters of a certain model, starting from a set of data contaminated by large amounts of outliers. It is an iterative, non-deterministic algorithm which uses least-squares to estimate model parameters. The basic premise of RANSAC is the presence in the data set of both observations that fit the model (inliers) and those which differ from the values (outliers). The sources of data that do not fit into the model are gross errors (measurement errors), noise or other disturbances.
  The input data of the algorithm are: a set of data and a mathematical model that will be matched to the data set. The advantage of this method is that the percentage of outliers which can be handed by RANSAC can be larger than 50% of the entire data set.
  The RANSAC algorithm is a learning technique to estimate parameters of a model by random sampling of observed data. The RANSAC algorithm is essentially composed of two steps that are iteratively repeated.

:sparkle:In the first step, a sample subset containing minimal data items is randomly selected from the input dataset. fitting model and the corresponding model parameters are computed using only the elements of this sample subset. The cardinality of the sample subset is the smallest sufficient to determine the model parameters.

:sparkle:In the second step, the algorithm checks which elements of the entire dataset are consistent with the model instantiated by the estimated model parameters obtained from the first step. A data element will be considered as an outlier if it does not fit the fitting model instantiated by the set of estimated model parameters within some error threshold that defines the maximum deviation attributable to the effect of noise.
<p align="center">
  <img width="300" height="200" src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Line_with_outliers.svg/383px-Line_with_outliers.svg.png">
  </p>
  
 #### A data set with many outliers for which a line has to be fitted
 
 <p align="center">
  <img width="300" height="200" src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Fitted_line.svg/383px-Fitted_line.svg.png">
  </p>
  
  #### Fitted line with RANSAC outliers have no influence on the result.
 

## :nazar_amulet:  Implementation:
I have used Cafe dataset where it detects the outlier in the image. X axis is taken as avg no of cafes opened and Y axis as total cafes in the city.

:sparkle: Select a random number of examples to be inliers and train the model. 

:sparkle: Test all other data points against the trained model

:sparkle: Out of all the data points tested in step 2, select the points as inliers which fall within a user-given tolerance. In scikit-learn, median absolute deviation (MAD) is used for selecting the new points as inliers.

:sparkle: Retrain the model with all inliers data

:sparkle: Estimate the error of the retrained model versus the inliers.

:sparkle: Follow step 1 to step 5

:sparkle: Terminate the algorithm execution if the model performance meets a certain user-defined threshold or if a fixed number of iterations were reached
 
<p align="center">
  <img width="300" height="200" src="https://www.researchgate.net/profile/Mehrdad-Heydarzadeh/publication/313472923/figure/fig3/AS:663973812776960@1535315101199/Illustration-of-the-threshold-value-determined-by-RANSAC-algorithm-to-detect-outliers.png">
  </p>


## :nazar_amulet:  Output:
<p align="center">
  <img width="600" height="500" src="https://user-images.githubusercontent.com/66861391/136230373-20d5144d-47d1-4506-a48b-4234be563953.png">
  </p>
  
## :nazar_amulet: Applications:
The RANSAC algorithm is often used in computer vision, e.g., to simultaneously solve the correspondence problem and estimate the fundamental matrix related to a pair of stereo cameras; see also: Structure from motion, scale-invariant feature transform, image stitching, rigid motion segmentation.

## :nazar_amulet: Limitations
Despite the advantages of this method, it has some flows. It is not an efficient method from a computational point of view. Number of iterations increases with the number of outliers in the data set and with required probability of successful selection of two inliers. It requires much iterations and many operations which sometimes (especially in the case of large sets) take a longer time than the standard procedure. 

## :nazar_amulet: Conclusion:
The algorithm was able to find a correct solution and to eliminate outliers from estimation process. Therefore, the effectiveness of RANSAC algorithm applied to estimation of coordinate transformation parameters is confirmed.

 :stars: RANSAC regression algorithm takes care of removing outliers from the training data set while fitting the model.
 
 :stars:Some of the important hyper parameters for the RANSAC algorithm includes maximum number of iterations, minimum number of samples, loss function, residual threshold.
 
 :stars: Python Sklearn implementation of RANSAC regression takes into account median absolute deviation for handling inliers and outliers.
 
 :stars: RANSAC regression requires a base estimator to be set. With Python Sklearn implementation RANSACRegressor, the default base estimator is LinearRegression.
