from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import AdaBoostClassifier
#
# Load the breast cancer dataset
#
bc = datasets.load_breast_cancer()
X = bc.data
y = bc.target
#
# Create training and test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.85, random_state=1, stratify=y)

# Pipeline Estimator
#
pipeline = make_pipeline(StandardScaler(),
                        DecisionTreeClassifier(criterion='entropy', max_depth=1, random_state=1))
#
# Fit the model
#
pipeline.fit(X_train, y_train)
#
# Model scores on test and training data
#
print('Model test Score: %.3f, ' %pipeline.score(X_test, y_test),
      'Model training Score: %.3f' %pipeline.score(X_train, y_train))

# Model fit using AdaBoostClassifier
# Standardize the dataset
#
sc = StandardScaler()
X_train_std = sc.fit_transform(X_train)
X_test_std = sc.transform(X_test)
#
# Creating a decision tree classifier instance
#
dtree = DecisionTreeClassifier(criterion='entropy', max_depth=1, random_state=1)
#
# Instantiate the bagging classifier
#
adbclassifier = AdaBoostClassifier(base_estimator=dtree,
                                   n_estimators=100,
                                   learning_rate=0.0005,
                                   algorithm = 'SAMME',
                                   random_state=1)
#
# Fit the AdaBoost classifier
#
adbclassifier.fit(X_train, y_train)
#
# Model scores on test and training data
#
print('Model test Score: %.3f, ' %adbclassifier.score(X_test, y_test),
      'Model training Score: %.3f' %adbclassifier.score(X_train, y_train))