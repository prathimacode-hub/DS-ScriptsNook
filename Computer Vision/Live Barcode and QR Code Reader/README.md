## **PROJECT TITLE**
Live Barcode and QR Code Reader

## **INTRODUCTION**
In this tutorial we will be performing a QR/Barcode scanner task which detects, scans and saves link in the `.txt` file. This task will be performed in the local enviornment.

## **PURPOSE**
Our aim here is to import the required dependencies, I think Barcodes/QR codes are very cool and interesting because they store information in a different format. The fun part about them is we can’t really tell what they are storing until we scan them.

## **BRIEF EXPLANATION**
If you are wondering how barcode and QR code readers work, let’s do a quick real-life practice. Turn on your phone’s camera and show the featured image of this article. You will see a link show up, it’s very simple to use. Today, we will create our own reader, without losing any time let’s get started!

## **WORKING CONDITIONS**
<ol>
    <li><strong>Setting up the enviornment</strong></li> </br>
     I recommend to perform the task in the local enviornment and not on the online enviornments because it might cause issues in loading your local camera. </br>
  <img src="" width=700> 
</br>
</br>
</div>
    <li><strong> Importing required Packages</strong></li> </br>
    Importing all the packages needed for the further processing of the model. </br>
    <img src="https://github.com/DevIncept-Contribution-Program-21/DS-ScriptsNook/blob/main/Machine%20Learning/Algorithms/K-Means%20Clustering/Images/packages.jpeg" width=700>
</div> </br>
Here we imported all the required packages required for the model.
</br>
</br>
</div>
    <li><strong> Data Visualization </strong></li> </br>
    We then, perform the exploratory data analysis and visualize the data. </br>
  <img src="https://github.com/DevIncept-Contribution-Program-21/DS-ScriptsNook/blob/main/Machine%20Learning/Algorithms/K-Means%20Clustering/Images/dataviz1.jpeg" width=700>
  </br>
  <img src="https://github.com/DevIncept-Contribution-Program-21/DS-ScriptsNook/blob/main/Machine%20Learning/Algorithms/K-Means%20Clustering/Images/dataviz2.jpeg" width=700>
  </br>
</div>
    <li><strong>Preparation of the dataset (Arrangement and Cleaning)</strong></li> </br>
    Then we use the different parameters which helps in data cleaning. Eg: kmeans.fit(), means.cluster_centers_ , etc.  </br>
  <img src="https://github.com/DevIncept-Contribution-Program-21/DS-ScriptsNook/blob/main/Machine%20Learning/Algorithms/K-Means%20Clustering/Images/dataprep.jpeg" width=700> </br>
</div>
  </br>

</div>
    <li><strong>Setting up the variables</strong></li> </br>
    Once the data visualization is done, Now we will convert our dataset in a format suitable for our model.  </br>
  <img src="https://github.com/DevIncept-Contribution-Program-21/DS-ScriptsNook/blob/main/Machine%20Learning/Algorithms/K-Means%20Clustering/Images/setvar.jpeg" width=700>
  </br>
  </br>
</div>
    <li><strong>Then Finally, Testing</strong></li> </br>
    </br>
    Here, we have achieved a weak classification accuracy of 1% with k=2 by our unsupervised model. So, I changed the value of k and find relatively higher classification accuracy of 88% with k=4. Hence, we can conclude that k=4 being the optimal number of clusters. </br>
  <img src="https://github.com/DevIncept-Contribution-Program-21/DS-ScriptsNook/blob/main/Machine%20Learning/Algorithms/K-Means%20Clustering/Images/testing.jpeg" width=700>
</div>
</ol>
</br>

## **USAGE**
- The K-means clustering algorithm is used to find groups which have not been explicitly labeled in the data. This can be used to confirm business assumptions about what types of groups exist or to identify unknown groups in complex data sets.

## **USE CASES**
- K-means algorithm is very popular and used in a variety of applications such as market segmentation, document clustering, image segmentation and image compression, etc.

## **LIBRARIES USED**
- Pandas
- Numpy
- matplotlib.pyplot
- seaborn
- kmeans

## **ADVANTAGES**

- Relatively simple to implement.
- Scales to large data sets.
- Guarantees convergence.
- Can warm-start the positions of centroids.
- Easily adapts to new examples.

## **DISADVANTAGES**
- Being dependent on initial values.
- Choosing k manually.
- Clustering data of varying sizes and density.
- Scaling with number of dimensions.


## **APPLICATIONS**
K-Means clustering is used in a variety of examples or business cases in real life, like:

- Academic performance 
- Diagnostic systems 
- Search engines 
- Wireless sensor networks

## **CONCLUSION**

1. In this tutorial, I have implemented the most popular unsupervised clustering technique called K-Means Clustering.

2. I have applied the elbow method and find that k=2 (k is number of clusters) can be considered a good number of cluster to cluster this data.

3. I have find that the model has very high inertia of 237.7572. So, this is not a good model fit to the data.

4. I have achieved a weak classification accuracy of 1% with k=2 by our unsupervised model.

5. So, I have changed the value of k and find relatively higher classification accuracy of 88% with k=4.

5. Hence, we can conclude that k=4 being the optimal number of clusters.</br>
<img src="" width=700>


## **REFERENCES**
- [Introduction to K-means Clustering](https://www.simplilearn.com/tutorials/machine-learning-tutorial/k-means-clustering-algorithm)
- [Pros and Cons of K-means](https://developers.google.com/machine-learning/clustering/algorithm/advantages-disadvantages)
- [Dataset Used](https://archive.ics.uci.edu/ml/datasets/Facebook+Live+Sellers+in+Thailand)

## **YOUR NAME**

Hey, This is Hrugved Kolhe.

<a href="https://github.com/hrugved06"><img src="https://avatars.githubusercontent.com/u/59966943?s=400&u=445f4a7598547c0ecdeb22a265dd1a3dad9e297d&v=4" width="100px;" alt=""/><br /><sub><b> Hrugved Kolhe</b></sub></a>
</br>

[![GitHub followers](https://img.shields.io/github/followers/hrugved06.svg?label=Follow%20@hrugved06&style=social)](https://github.com/hrugved06)  [![Twitter Follow](https://img.shields.io/twitter/follow/HrugVed_?style=social)](https://twitter.com/HrugVed_)

</br>
<hr style="height:2px;#8080ffborder-width:0;border-radius: 5px;color:gray;background-color:#8080ff">
</br>