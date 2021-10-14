
# :fleur_de_lis: Introduction to Keras

<p align="center">
  <img width="350" height="200" src="https://njtrainingacademy.com/wp-content/uploads/2019/02/keras-1.png">
  </p>


## :nazar_amulet: Aim:
  To explain Keras by building a deep learning model.

## :nazar_amulet: Introduction:

Keras is an open source Neural network library used for deep learning models. Keras was originally created by François Chollet. Historically, Keras was a high-level API that sat on top of one of three lower level neural network APIs and acted as a wrapper to to these lower level libraries. These libraries were referred to as Keras backend engines.
You could choose TensorFlow, Theano, or CNTK as the backend engine you'd like to work with.

:stars: TensorFlow

:stars: Theano

:stars: CNTK

Ultimately, TensorFlow became the most popular backend engine for Keras.
Later, Keras became integrated with the TensorFlow library and now comes completely packaged with it.



## :nazar_amulet: Implementation
1.Have Python 2 or 3 installed and configured
2.SciPy (including NumPy) should be installed and configured.
3. Install Keras using this command

      $ pip install keras

 4. Then Load Data for building deep learning model(Load any dataset (csv or excel file) of your choice( I prefer taking dataset from kaggle) ) Read CSV file using pandas dataframe
 5. Perform feature selection , outlier detection( basically data exploration)
 6. Test the model using .test() and compile it
 7. Next , fit the model on training data.
 8. Finally , Evaluate the Neural network model on testing data.

Here, I have predicted heart rate prediction using Keras.


## :nazar_amulet: Output:
<p align="center">
  <img width="450" height="300" src="https://user-images.githubusercontent.com/66861391/137299979-04aaa6ad-9ace-414a-9ce8-ce0863504bb5.png">
  </p>
  
  <p align="center">
  <img width="450" height="300" src="https://user-images.githubusercontent.com/66861391/137300293-9a7dbfe0-efeb-40b4-bbce-7e9f6724cdec.png">
  </p>


## :nazar_amulet: Advantages of Keras:
 1. They are user friendly
 2. Multiple backend and modularity
 3. Multiple GPU support

## :nazar_amulet: Disadvantages of Keras:
 1.Sometimes there's low level backend errors.
 2.  It is not so good to build some basic machine learning algorithms like clustering and PCM (principal component analysis). It does not have features of dynamic chart creation.

## :nazar_amulet: Applications:
These models can be used for 

:stars: Prediction

:stars: Feature extraction

:stars: Fine tuning

:stars: Keras was developed with a focus on enabling fast experimentation. Because of this, it's very user friendly and allows us to go from idea to implementation with only a few steps.

## :nazar_amulet: Conclusion:
Keras contains numerous implementations of commonly used neural-network building blocks such as layers, objectives, activation functions, optimizers, and a host of tools to make working with image and text data easier to simplify the coding necessary for writing deep neural network code.
In this documentation , I explained how to install Keras and use it using a deep learning model that aims to predict heart rate using keras.

## :nazar_amulet: References used:
https://data-flair.training/blogs/python-keras-advantages-and-limitations/

https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/
