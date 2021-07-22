## **PROJECT TITLE**
YouTube Comments Classifier

## **INTRODUCTION**
In this tutorial we will be using Google colab to train our model. In this model we will be classifying the nature of the comments posted on youtube videos and will be removing the spammed links.

## **PURPOSE**
Aim of this tutorial is to make a model which classifies the YT comments and remove the spam links from the comments.

## **BRIEF EXPLANATION**
In this tutorial, I will be creating a harmful comments filter using multinomial naive bayes algorithm without sci-kit learn, to filter out harmful comments from Youtube videos. We have data of labelled youtube comments in five seperate files. So we'll train our model with four of them and use the fifth file for prediction and testing for accuracy.

## **WORKING CONDITIONS**
<ol>
    <li><strong> Mounting the drive </strong></li> </br>
    Mount the drive and enter the path to the folder where your dataset is stored, so you can access it. </br>
  <img src="https://github.com/DevIncept-Contribution-Program-21/DS-ScriptsNook/blob/main/Machine%20Learning/Tutorials/YT%20comments%20classifier/Images/Drive%20Mounting.jpeg" width=700> 
</br>
</br>
</div>
    <li><strong> Importing required Packages</strong></li> </br>
    Importing all the packages needed for the further processing of the model. </br>
    <img src="https://github.com/DevIncept-Contribution-Program-21/DS-ScriptsNook/blob/main/Machine%20Learning/Tutorials/YT%20comments%20classifier/Images/Importing%20and%20concatinating%20the%20Dataset.jpeg" width=700>
</div> </br>
Here we imported all the required packages and concatinated all the .csv files present in the folder 
</br>
</br>
</div>
    <li><strong>Preparation of the dataset (Arrangement and Cleaning)</strong></li> </br>
    Then we use the different parameters which helps in data cleaning. Eg: str.replace()  </br>
  <img src="https://github.com/DevIncept-Contribution-Program-21/DS-ScriptsNook/blob/main/Machine%20Learning/Tutorials/YT%20comments%20classifier/Images/Data%20Preparation%201.jpeg" width=700> </br>
Here, with the help of str.replace() function we replace all the unwanted/promoted links with the text "htmllink". </br>
  <img src="https://github.com/DevIncept-Contribution-Program-21/DS-ScriptsNook/blob/main/Machine%20Learning/Tutorials/YT%20comments%20classifier/Images/Data%20Preparation%202.jpeg" width=700>
</div>
    <li><strong> Data Visualization </strong></li> </br>
    We then, take a look at 10 random rows of our original dataset which has spam links (Before Processing) </br>
  <img src="https://github.com/DevIncept-Contribution-Program-21/DS-ScriptsNook/blob/main/Machine%20Learning/Tutorials/YT%20comments%20classifier/Images/Before%20Processing.jpeg" width=700> </br>
  Here, after processing all the harmful/spam links are converted to the specified text "htmllink". </br>
  <img src="https://github.com/DevIncept-Contribution-Program-21/DS-ScriptsNook/blob/main/Machine%20Learning/Tutorials/YT%20comments%20classifier/Images/After%20Processing.jpeg" width=700> 
  </br>
  </br>
</div>
    <li><strong>Setting up the variables</strong></li> </br>
    Once the data visualization is done, Now we will convert our dataset in a format suitable for our model. Basically we will concatenate responses in one string for each row (additionally we will add special ‘end of string’ token between responses, so the model will understand the end of each response in a string). </br>
  <img src="https://github.com/DevIncept-Contribution-Program-21/DS-ScriptsNook/blob/main/Machine%20Learning/Tutorials/YT%20comments%20classifier/Images/Setting%20up%20Variables.jpeg" width=700>
  </br>
  </br>
</div>
    <li><strong>Training and Evaluatuing the model</strong></li> </br>
    Now its time to train our model, we need not to worry further as we have given the data in correct format to the model. </br>
  <img src="https://github.com/DevIncept-Contribution-Program-21/DS-ScriptsNook/blob/main/Machine%20Learning/Tutorials/YT%20comments%20classifier/Images/Training%20and%20Evaluation.jpeg" width=700>
</div>
</br>
</br>
    <li><strong>Then Finally, Testing</strong></li> </br>
    After thae training process, the model is ready, now you can add comments and test the model. Here are some examples tried to test the model. </br>
  <img src="https://github.com/DevIncept-Contribution-Program-21/DS-ScriptsNook/blob/main/Machine%20Learning/Tutorials/YT%20comments%20classifier/Images/Testing.jpeg" width=700>
</div>
</ol>
</br>

## **USAGE**
- This model can be handy to filter the comments posted on the youtube videos.

## **USE CASES**
Many times the comments section in some YouTube videos is not very great to read because of some harmful comments and harmful links floated. This model classifies the harmful commemts and converts the all unwanted links to normal text.

## **LIBRARIES USED**
- Pandas
- Numpy
- Glob
- Html

## **ADVANTAGES**
- Useful to classify the comments
- Removes unwanted/harmful links
- Concatination of multiple datasets helps the model in training more data which results in better accuracy.

## **DISADVANTAGES**
- Accuracy of the model can be low if single .csv data file is used or data is too less

## **APPLICATIONS**
Can be used in:
- Kids Applications
- Youtube Kids Application

## **CONCLUSION**
Congo! Your model is ready with no longer training period or with no longer steps involved.🥳 </br>
</br>
Accuracy of our model is 93.14 % which is pretty good. This is the improved accuracy achieved by concatinating the datasets.</br>
<img src="https://github.com/DevIncept-Contribution-Program-21/DS-ScriptsNook/blob/main/Machine%20Learning/Tutorials/YT%20comments%20classifier/Images/Testing.jpeg" width=700>


Using the given approach you can use different datasets and check working of this model on them. </br>
</br>

## **REFERENCES**
- [Classification using Naive Multi-label Classification](https://www.kaggle.com/datasets?search=youtube+spam+comments)
- [Dataset Used](https://www.kaggle.com/prashant111/youtube-spam-collection)
- [Optional Dataset](https://www.kaggle.com/datasets?search=youtube+spam+comments)

## **YOUR NAME**

Hey, This is Hrugved Kolhe.

<a href="https://github.com/hrugved06"><img src="https://avatars.githubusercontent.com/u/59966943?s=400&u=445f4a7598547c0ecdeb22a265dd1a3dad9e297d&v=4" width="100px;" alt=""/><br /><sub><b> Hrugved Kolhe</b></sub></a>
</br>

[![GitHub followers](https://img.shields.io/github/followers/hrugved06.svg?label=Follow%20@hrugved06&style=social)](https://github.com/hrugved06)  [![Twitter Follow](https://img.shields.io/twitter/follow/HrugVed_?style=social)](https://twitter.com/HrugVed_)

</br>
<hr style="height:2px;#8080ffborder-width:0;border-radius: 5px;color:gray;background-color:#8080ff">
</br>