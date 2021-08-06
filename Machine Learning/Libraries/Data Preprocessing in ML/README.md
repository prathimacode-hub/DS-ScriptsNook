### Data Pre-processing in ML

Data pre-processing means to understand the data.
- Data preprocessing is a process of preparing the raw data and making it suitable for a machine learning model.
- Real-world data is often incomplete, inconsistent, and/or lacking in certain behaviors or trends, and is likely to contain many errors.
- Data preprocessing is a proven method of resolving such issues.

It is of 2 types:
- one handle numerical values
- other to handle categorical values

Our ML model cannot work with either null values or categorical values

*---------------------------------Handling missing values----------------------------------*

If you have less missing values and are not that important, then you can directly drop them 
**Syntax:** 
d1 = data.dropna(how="any", axis=0), it drops rows which as any null values
d2  = data.dropna(subset=[column_name]), drops rows from the column name specified

If you want to fill missing values, then you can do them as following:
**Syntax:** 
d1 = data.fillna({"Age": data["Age"].mean()}), for numerical data
d2 = data.fillna({"Position": "Unallocated"}), for categorical data


*------------------------------Handling categorical values-------------------------------*
As we know that our model cannot work with categorical values, we have to convert them into numerical data and this can be done using pandas library
**Syntax:** 
features = pd.get_dummies(data.place) , eg: place is a column name in the data
It will convert the categorical data in 0,1,2.. format

new_features = pd.get_dummies(data.place, drop_first=True)
About **drop_first=True**, i've explained in detailed in Handling_categorical_data.ipynb


