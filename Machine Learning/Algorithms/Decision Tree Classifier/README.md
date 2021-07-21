## **DECISION TREE CLASSIFIER**

**INTRODUCTION**

Decision Tree is one of the efficient and highly used alorithm in machine learning.

We can use decision tree algorithm in two types as:

Decision Tree Classifier (for classification tasks)

Decision Tree Regressor (for regression tasks)

**PURPOSE**

The main prupose is to give a clear understanding on what basically Decision Tree Classifier algorithm is all about, its working, usage, libaries used, advantages, disadvantages etc.


**BRIEF EXPLANATION**
- Let's understand Decision Tree Classifier algorithm with help of the problem statement given below:

Bob has started his own mobile company. He wants to give tough fight to big companies like Apple,Samsung etc.

He does not know how to estimate price of mobiles his company creates. In this competitive mobile phone market you cannot simply assume things. To solve this problem he collects sales data of mobile phones of various companies.

Bob wants to find out some relation between features of a mobile phone(eg:- RAM,Internal Memory etc) and its selling price. But he is not so good at Machine Learning. So he needs your help to solve this problem.

In this problem you do not have to predict actual price but a price range indicating how high the price is.

**WORKING CONDITIONS**
1.  Data preprocessing and exploration to understand what kind of data will we working on.

- Here we work on preprocessing and exploring the data to understand what kind of data we are working on, it's shape, memory usage, columns, data types etc.

![](https://github.com/ayushi424/DS-ScriptsNook/blob/main/Machine%20Learning/Algorithms/Decision%20Tree%20Classifier/Images/dtc1.jpg)
![](https://github.com/ayushi424/DS-ScriptsNook/blob/main/Machine%20Learning/Algorithms/Decision%20Tree%20Classifier/Images/dtc2.jpg)

2.  Data visualization to draw insights and get better underdstanding on different columns present in the dataset.
![](https://github.com/ayushi424/DS-ScriptsNook/blob/main/Machine%20Learning/Algorithms/Decision%20Tree%20Classifier/Images/dtc3.jpg)
![](https://github.com/ayushi424/DS-ScriptsNook/blob/main/Machine%20Learning/Algorithms/Decision%20Tree%20Classifier/Images/dtc4.jpg)



3. Data training using train-test-split method from sklearn to split the data into training and testing data and then  Model creation using decision tree classifier algorithm, where we import the model, then initialize it and fit training data into it and lastly perform predictions on the test data.
 ![](https://github.com/ayushi424/DS-ScriptsNook/blob/main/Machine%20Learning/Algorithms/Decision%20Tree%20Classifier/Images/dtc5.jpg)

5.  Checking performance by error and accuracy check to find how efficient algorithm performed for this project.
![](https://github.com/ayushi424/DS-ScriptsNook/blob/main/Machine%20Learning/Algorithms/Decision%20Tree%20Classifier/Images/dtc6.jpg)

   For the dataset being used [click here](https://www.kaggle.com/iabhishekofficial/mobile-price-classification?select=train.csv)

**USAGE**
- It is basically used for CLASSIFICATION TASKS.
- It is a class capable of performing multi-class classification on a dataset.

**USE CASES**
- Classification tasks.
- Mainly used for complex projects.
- Used in projects where there are more number of features.

**LIBRARIES USED**
- pandas
- matplotlib
- seaborn
- sklearn
- numpy

**ADVANTAGES**
- Requires little data preparation. Other techniques often require data normalisation, dummy variables need to be created and blank values to be removed. Note however that this module does not support missing values.
- Easy understand & interpret
- Good for classification tasks


**DISADVANTAGES**
- Decision-tree learners can create over-complex trees that do not generalise the data well. This is called overfitting. Mechanisms such as pruning, setting the minimum number of samples required at a leaf node or setting the maximum depth of the tree are necessary to avoid this problem.
- Relationship between features should be well understood or else it might give low performance efficiency.
- Can give low accuracy if features are not identified properly.
- Cannot be used for regression projects.

**APPLICATIONS**

- Used in different classification tasks.
- Decision trees are used for handling non-linear data sets effectively.
- The decision tree tool is used in real life in many areas, such as engineering, civil planning, law, and business.
- Can help in improving business plan by providing fruitful insights and prediction analysis.

**CONCLUSION**

*  Decision Tree Classifier is one of the most efficient classification algorithm which is highly used for classification tasks.

*  For this project i.e. mobile price range classification, accuracy of decision tree classifier is 1.00 i.e. 100%

*  It Can help in improving business plan by providing fruitful insights and prediction analysis.


**REFERENCES**

- For the dataset being used [click here](https://www.kaggle.com/iabhishekofficial/mobile-price-classification?select=train.csv)
- https://scikit-learn.org/stable/modules/tree.html
- https://www.javatpoint.com/machine-learning-decision-tree-classification-algorithm
- https://www.datacamp.com/community/tutorials/decision-tree-classification-python


**Author**

[Ayushi Shrivastava](https://github.com/ayushi424)

**Happy Learning :)**
