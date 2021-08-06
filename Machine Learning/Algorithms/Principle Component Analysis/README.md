# PRINCIPLE COMPONENT ANALYSIS(PCA)

![](https://www.analyticsvidhya.com/wp-content/uploads/2016/03/1-1.png)

GOAL

The main goal of this project is to give complete guide to principle component analysis with implementation.

PURPOSE

As you all know, we often come across the problems of storing and processing huge data in machine learning tasks, as it’s a time-consuming process and difficulties to interpret also arises. Not every feature of the data is necessary for predictions. These noisy data can lead to bad performances and overfitting of the model. Through this project, let me introduce you to an unsupervised learning technique PCA(Principal Component Analysis) that can help you deal effectively with these issues to an extent and provide more accurate prediction results.


DATASET 

You can download the dataset from [here](https://www.kaggle.com/uciml/breast-cancer-wisconsin-data)

DESCRIPTION

Principal Component Analysis(PCA) is one such technique by which dimensionality reduction(linear transformation of existing attributes) and multivariate analysis are possible. 

How is this done?

Initially, you need to find the principal components from different points of view during the training phase, from those you pick up the important and less correlated components and ignore the rest of them, thus reducing complexity. The number of principal components can be less than or equal to the total number of attributes.

WHAT I HAD DONE

I have created a detailed .ipynb notebook with concept explanation and implementation with code.


USAGE

The most important use of PCA is to represent a multivariate data table as smaller set of variables (summary indices) in order to observe trends, jumps, clusters and outliers. This overview may uncover the relationships between observations and variables, and among the variables.


ADVANTAGES

It has several advantages, which include reduction of data size(hence faster execution), better visualizations with fewer dimensions, maximizes variance, reduces overfitting, etc.

DISADVANTAGES

You must note that data standardization ( which also includes converting categorical variables to numerical) is a must before using PCA. On applying PCA, the independent features become less interpretable because these principal components are also not readable or interpretable. 
There are also chances that you lose information while PCA.

APPLICATIONS

- Spike-triggered covariance analysis in Neuroscience
- Quantitative Finance
- Medical Data correlation
- facial recognition
- computer vision
- image compression

![](https://iq.opengenus.org/content/images/2020/03/pca_classic.png)



CONCLUSION

- PCA helps in Dimensionality reduction. Converts set of correlated variables to non-correlated variables.
- It finds a sequence of linear combinations of variables.
- PCA also serves as a tool for better data visualization of high dimensional data. We can create a heat map to show the correlation between each component. 
- It is often used to help in dealing with multi- collinearity before a model is developed.
- It describes that data is a good story teller of its own.
- These models are useful in data interpretation and variable selection.


# Author :
Name : Shivani Rana | [LinkedIn](https://www.linkedin.com/in/shivani-rana-b833a91a3/) | [Github](https://github.com/shivani6320)



