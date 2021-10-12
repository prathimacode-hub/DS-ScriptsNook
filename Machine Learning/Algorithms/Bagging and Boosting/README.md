# :pushpin: **BAGGING AND BOOSTING**
<p align="center">
 <img width="600" height="350" src="https://miro.medium.com/max/2000/1*zTgGBTQIMlASWm5QuS2UpA.jpeg">
</p>


## :page_facing_up: **ENSEMBLE LEARNING**
Ensemble learning is the process by which multiple models, such as classifiers or experts, are strategically generated and combined to solve a particular computational intelligence problem. Ensemble learning is primarily used to improve the (classification, prediction, function approximation, etc.) performance of a model, or reduce the likelihood of an unfortunate selection of a poor one. 
Other applications of ensemble learning include assigning a confidence to the decision made by the model, selecting optimal (or near optimal) features, data fusion, incremental learning, nonstationary learning and error-correcting.
<p align="center">
 <img width="600" height="350" src="https://machinelearningknowledge.ai/wp-content/uploads/2019/12/Ensemble-Learning-Intuition.gif">
</p>

## :dart: **BAGGING**
Bagging, also known as Bootstrap Aggregation is an Ensemble Learning technique that has two parts – i) Bootstrap and ii) Aggregation.

### **Bootstrap**
Bootstrap is a technique of random sampling of data with replacement. In the ensemble learning context, we prepare multiple training sets by this bootstrap method.

Just to give an example, if we have a data set  (a,b,c,d,e,f,g,h,i,j) then we can get following training set using bootstrap –

* (a,f,d,j,h,c)  (b,g,a,i,c,f)  (i,d,c,e,a,d)  (b,h,g,h,a,b)

### **Aggregation**
The different learners train on these various training sets that are obtained by bootstrapping method. The hypothesis of these individually trained learners are then aggregated to form a single consensus output.

* In the case of classification, the aggregation takes place by considering the maximum vote by the different learners. This means, that if 3 base learners classify as class A and the remaining 2 learners classify as class B, then the prediction will be considered as class A, based on the maximum vote it got.
* In case of regression, the aggregation takes place by taking average of the results. This means, that if the 5 base learners produce following results – 21.23, 20.67, 21.66, 21.01, 20.82 then the actual result will be 21.07

<p align="center">
 <img width="600" height="350" src="https://machinelearningknowledge.ai/wp-content/uploads/2019/12/Bagging-Bootstrap-Aggregation.gif">
</p>


## :dart: **BOOSTING**
Boosting is another popular ensemble learning method in which different learners are trained in an iterative manner one after another to finally create a strong learner.

One key characteristic of boosting is that when the learners are trained sequentially, each learner tries to work more on the weak predictions of the previous learner. At the intuition level, you can think that after the training of each learner, a feedback is generated which is used by the next learner to improve on the previous learner.

Once all learners are trained, boosting also relies on the voting of learners to get the combined prediction.

When it comes to better bias, boosting usually performs better than bagging.

<p align="center">
 <img width="600" height="350" src="https://machinelearningknowledge.ai/wp-content/uploads/2019/12/Boosting.gif">
</p>


There are 3 popular variants of Boosting. Lets us have a look at that –

### **Ada Boost**
1. In Ada Boost, in the beginning, each data is assigned an equal weight so that each has an equal probability of being selected in the training data set.
2. After the first learner is trained, the weight of data is increased whose prediction was done wrongly by the first learner.
3. When the next learner is trained, the data with higher weights are included in the training set. This ensures that the next learner can learn about the data which the previous learner failed to do.
4. The process of steps 1 and 3 keeps on getting repeated until we have all data properly predicted by the learners in the training phase.

### **Gradient Boosting**
In Gradient Boosting, each learner tries to reduce the loss of the previous learner by optimizing the loss function.

1. Initially, the first learner is trained and the loss is calculated.
2. Now, the next learner is added which focuses on reducing the loss obtained from the previous learner
3. The process in step 2 is repeated, till the loss function is properly optimized and data is fitted properly.

### **XGBoost**
* Gradient boosting technique is computationally slow. XGBoost is variant of gradient boosting which focuses on performance and fast computation.

* XGBoost actually stands for Extreme Gradient Boosting and relies on parallel and distributed computing to achieve fast much greater performance and results.

* XGBoost is the most widely used model by the winner of competitions and data scientists.

## :bulb: **Differences Between Bagging and Boosting –**
| Sr No.  | **Bagging** | **Boosting**  |   
|----|---|---|
|  1. | Simplest way of combining predictions that belong to the same type.  | A way of combining predictions thatbelong to the different types.  |   
|  2. | Aim to decrease variance, not bias.  | Aim to decrease bias, not variance.   |   
|  3. | Each model receives equal weight.  | Models are weighted according to their performance.  |  
|  4. |  Each model is built independently. | New models are influenced by performance of previously built models.  |   

## :thought_balloon: **PREREQUISITES**
All the dependencies and required libraries are included in the file <code>requirements.txt</code> [See here](./requirements.txt)

## :high_brightness: **CODING AND IMPLEMENTATION**
1. Import the libraries.
2. Load the dataset.
3. Create the training and test split.
4. Fit the model.
5. Print the test and training data score.

## :bar_chart: **OUTPUT**
 
![bagging](https://user-images.githubusercontent.com/36481036/136665234-c0d2ef95-27e9-40d2-be96-6c1b9106cb02.png)
![boosting](https://user-images.githubusercontent.com/36481036/136665240-56bd84ed-9948-41b0-b4bf-9f429d76719f.png)


## :bust_in_silhouette: **CREDITS**
* https://machinelearningknowledge.ai/gentle-introduction-to-ensemble-learning-for-beginners/
* https://www.i2tutorials.com/machine-learning-tutorial/bagging-boosting/
* http://www.scholarpedia.org/article/Ensemble_learning

**:sunglasses:** **CREATOR**- https://github.com/theshredbox

