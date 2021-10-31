## **PROJECT TITLE**
K-Means Clustering

## **INTRODUCTION**
In this tutorial we will be using Jupyter Notebook to learn how to use K Medoids Clustering algorithm. In this tutorial we will be learning how K Medoids clustering works.

## **PURPOSE**
Our aim here is to process the learning data, the K-Medoids algorithm in data mining is a Clustering Algorithm in Machine Learning that uses Medoids (i.e. Actual Objects in a Cluster) to represent the Cluster.We will understand deeper about the same in this code.

## **BRIEF EXPLANATION**
K Medoid is a Clustering Algorithm in Machine Learning that uses Medoids (i.e. Actual Objects in a Cluster) to represent the Cluster.

## K Medoid Clustering Process
<ol>
  <li>Initialize: select k random points out of the n data points as the medoids.</li>
  <li>Associate each data point to the closest medoid by using any common distance metric methods.</li>
  <li>While the cost decreases:<br>
        For each medoid m, for each data o point which is not a medoid:
    <ol>
      <li>Swap m and o, associate each data point to the closest medoid, recompute the cost.</li>
      <li>If the total cost is more than that in the previous step, undo the swap.</li>
    </ol>
  </li>
</ol>  


## **LIBRARIES USED**
- Pandas
- Numpy
- matplotlib.pyplot
- scikit-learn
- scikit-learn-extra

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


## **IMAGES**
<img src = "https://github.com/photon149/DS-ScriptsNook/blob/56c53773376f4f8d12231bfb50eb63ddb05c8f03/Machine%20Learning/Algorithms/K%20Medoids%20Clustering/Images/data_cluster.png">
<img src = "https://github.com/photon149/DS-ScriptsNook/blob/56c53773376f4f8d12231bfb50eb63ddb05c8f03/Machine%20Learning/Algorithms/K%20Medoids%20Clustering/Images/kmedoids_cluster.png">
## **CONCLUSION**

1. In this , I have implemented unsupervised clustering technique called K-Medoids Clustering.
2. In this , I have created a random dataset using make_blobs functions present in the scikit learn library
3. Then , we implemented the KMedoids clustering model , using scikit learn extra library
4. After implementation we got a silhouette score of around 63.7%
5. Then we have compared the same with two other clustering technique used in the markets that is KMeans and Birch Alogrithm






