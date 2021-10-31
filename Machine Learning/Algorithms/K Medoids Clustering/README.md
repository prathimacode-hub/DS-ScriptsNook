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


## Advantages
<ul>
  <li>It outputs the final clusters of objects in a fixed number of iterations</li>
 <li>It is simple to understand and easy to implement.</li>
  <li>K-Medoid Algorithm is fast and converges in a fixed number of steps.</li>
  <li>PAM is less sensitive to outliers than other partitioning algorithms.</li>
</ul>  

## Disadvantages
<ul>
  <li>The main disadvantage of K-Medoid algorithms is that it is not suitable for clustering non-spherical (arbitrary shaped) groups of objects. This is because it relies on minimizing the distances between the non-medoid objects and the medoid (the cluster center) – briefly, it uses compactness as clustering criteria instead of connectivity.</li>
  <li>It may obtain different results for different runs on the same dataset because the first k medoids are chosen randomly.</li>
</ul> 

## Complexity
The time complexity of the algorithm is O(k * (n-k)2) , where k is th enumber of clusters.

## Comparison with K Means
The k-medoids method is more robust than k-means in the presence of noise and outliers because a medoid is less influenced by outliers or other extreme values than a mean. However, the complexity
of each iteration in the k-medoids algorithm is O(k(n − k)<sup>2</sup>). For large values of n
and k, such computation becomes very costly, and much more costly than the k-means
method.Both methods require the user to specify k, the number of clusters.

## **IMAGES**
<img src = "https://github.com/photon149/DS-ScriptsNook/blob/56c53773376f4f8d12231bfb50eb63ddb05c8f03/Machine%20Learning/Algorithms/K%20Medoids%20Clustering/Images/data_cluster.png">
<img src = "https://github.com/photon149/DS-ScriptsNook/blob/56c53773376f4f8d12231bfb50eb63ddb05c8f03/Machine%20Learning/Algorithms/K%20Medoids%20Clustering/Images/kmedoids_cluster.png">

## **CONCLUSION**

1. In this , I have implemented unsupervised clustering technique called K-Medoids Clustering.
2. In this , I have created a random dataset using make_blobs functions present in the scikit learn library
3. Then , we implemented the KMedoids clustering model , using scikit learn extra library
4. After implementation we got a silhouette score of around 63.7%
5. Then we have compared the same with two other clustering technique used in the markets that is KMeans and Birch Alogrithm 

Model	Scores<br>
KMedoids	0.637642<br>
KMeans	0.594127<br>
Birch	0.571567






