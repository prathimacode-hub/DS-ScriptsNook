### Data Pre-processing in ML

### GOAL
To get a basic understanding of how to pre-process the data before giving the data into the model.


### PURPOSE
Our machine learning models just cannot take in the real data as it is , since it may contain inconsistent values, missing values or wrong values. Therefore it is highly important to learn this section before moving further.


### DESCRIPTION
- Data pre-processing means to understand the data.
- Data preprocessing is a process of preparing the raw data and making it suitable for a machine learning model.

It is of 2 types:
- one handle numerical values
- other to handle categorical values


### WHAT I HAD DONE
1. Check for null values
- In order to proceed, we need to check if our data has any null values or not,
this can be checked with:

**Syntax:** 
data.isnull().sum()
This will give no of null values in each column

2. Handling missing values
- If you have less missing values and are not that important, then you can directly drop them ,

**Syntax:** 
d1 = data.dropna(how="any", axis=0), it drops rows which as any null values
d2  = data.dropna(subset=[column_name]), drops rows from the column name specified

If you want to fill missing values, then you can do them as following:
**Syntax:** 
d1 = data.fillna({"Age": data["Age"].mean()}), for numerical data
d2 = data.fillna({"Position": "Unallocated"}), for categorical data

3. Handling categorical values
- As we know that our model cannot work with categorical values, we have to convert them into numerical data and this can be done using pandas library

**Syntax:** 
features = pd.get_dummies(data.place) , eg: place is a column name in the data
It will convert the categorical data in 0,1,2.. format

new_features = pd.get_dummies(data.place, drop_first=True)
About **drop_first=True**, i've explained in detailed in Handling_categorical_data.ipynb


### WORKFLOW OF YOUR PROJECT FILES
1. Load the data using pandas
2. Understand the data, if any null values are present or not.
3. If there are some null values in numerical column, then they can be dropped of filled with mean/median
4. If there are some null values in categorical column, we can allocate a default value in them.
5. Lastly, if the data contains some categorical column, then they should be converted into numerical using the **get _dummies** function in pandas


### STATE YOUR PROCEDURE AND UNDERSTANDING FROM YOUR WORK
- This is a simple approach towards data pre-processing and very easy for the beginners to learn and therefore i chose this methodology.
- With this approach as well the cleaning of the data can be done.
- With this repo, I got to revise the ML Skills again

### USAGE

Data pre-processing should be first step for any ml enthisiast since your model cannot take in noisy data and hence it is highly important to learn this.

## USE CASES

This step should be done compulsorily in all cases before developing an ml model.

### LIBRARIES USED

- pandas (pip install pandas)

**ADVANTAGES**
- Data pre-processing helps us in giving the data into model without any problems

**DISADVANTAGES**

None

**APPLICATIONS**
- Data preprocessing is used database-driven applications such as customer relationship management and rule-based applications 

**SCREENSHOTS**

<img src="E:\github\DS-ScriptsNook\Machine Learning\Libraries\Data Preprocessing in ML\Images\img1.PNG" alt="None">
<img src="E:\github\DS-ScriptsNook\Machine Learning\Libraries\Data Preprocessing in ML\Images\img3.PNG" alt="None">
<img src="E:\github\DS-ScriptsNook\Machine Learning\Libraries\Data Preprocessing in ML\Images\img5.PNG" alt="None">

### CONCLUSION

Therefore, before building any ml model, one must take take about the data preprocessing section because the real-world data is often incomplete, inconsistent, and/or lacking in certain behaviors or trends, and is likely to contain many errors.

### REFERENCES
https://scikit-learn.org/stable/modules/preprocessing.html
https://towardsdatascience.com/preprocessing-with-sklearn-a-complete-and-comprehensive-guide-670cb98fcfb9
https://www.javatpoint.com/data-preprocessing-machine-learning

### YOUR NAME
Karakattil Dilrose Reji


