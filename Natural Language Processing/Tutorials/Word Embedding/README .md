## PROJECT TITLE
# :dart: **Word Embedding Techniques**
Word embedding implements language modeling and feature extraction based techniques to map a word to vectors of real numbers.

<img src="https://cdn.analyticsvidhya.com/wp-content/uploads/2019/11/Word-Vectors.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />
  ## GOAL
The goal of this project is brief understanding of Word Embedding Techniques
     
##  :page_facing_up: INTRODUCTION
What is word embedding with example?

Understanding the intuition behind word embedding creation with deep learning.For example, words like “mom” and “dad” should be closer together than the words “mom” and “ketchup” or “dad” and “butter”. Word embeddings are created using a neural network with one input layer, one hidden layer and one output layer

## What have I done?

1.Importing all the required libraries.

2.Brief explanatio of word embedding techniques.
  * TF-IDF Encoding
  * One Hot Encoding
  * Word2Vec
  * Continuous Bowl of Words(CBOW)
  * skip Gram
  * Bag of Words
  * Glove
  * Embedding Layer
 
4.Pratical Implementation of word embedding techniques.

5.Upload  the Jupyter Notebook file.

## :page_facing_up:  **BRIEF EXPLANATION**
In this I have cover various word embedding techniques.


 # :pushpin: Binary Encoding
 
 
 The representation of symbols in a source alphabet by strings of binary digits, i.e. a binary code. The most commonly occurring source alphabet consists of the set of    alphanumeric characters.
 
 
 ![image](https://user-images.githubusercontent.com/70129990/137106374-944c8906-9922-4dd0-a306-3f086f376bf8.png)

 
 # :pushpin: TF-IDF Encoding


TF-IDF (term frequency-inverse document frequency) is a statistical measure that evaluates how relevant a word is to a document in a collection of documents. This is done by multiplying two metrics: how many times a word appears in a document, and the inverse document frequency of the word across a set of documents
 ![image](https://user-images.githubusercontent.com/70129990/137114847-4b9d28b7-f67f-4035-8b80-1bf272940f12.png)

 
 # :pushpin: One Hot Encoding
 
 
One hot encoding is one method of converting data to prepare it for an algorithm and get a better prediction. With one-hot, we convert each categorical value into a new categorical column and assign a binary value of 1 or 0 to those columns. Each integer value is represented as a binary vector.
 ![image](https://user-images.githubusercontent.com/70129990/137106524-97195f01-76b2-481a-9d51-c40538f7a7d8.png)

 
 # :pushpin: Word2Vec
 
 
  Word2vec is a technique for natural language processing published in 2013. The word2vec algorithm uses a neural network model to learn word associations from a large corpus of text. Once trained, such a model can detect synonymous words or suggest additional words for a partial sentence.
  
 # :pushpin: Continuous Bowl of Words(CBOW)
 
  In the CBOW model, the distributed representations of context (or surrounding words) are combined to predict the word in the middle. While in the Skip-gram model, the distributed representation of the input word is used to predict the context.
 # :pushpin: skip Gram
 
 
The Skip-gram model architecture usually tries to achieve the reverse of what the CBOW model does. It tries to predict the source context words (surrounding words) given a target word (the center word). Thus the model tries to predict the context_window words based on the target_word.

 ![image](https://user-images.githubusercontent.com/70129990/137114319-d76a8175-8baf-4a63-a0db-c5031b49ae44.png)

 # :pushpin: Bag of Words
 
 
 
 Bag of Words (BOW) is a method to extract features from text documents. ... It creates a vocabulary of all the unique words occurring in all the documents in the training set. In simple terms, it's a collection of words to represent a sentence with word count and mostly disregarding the order in which they appear
 
 
 ![image](https://user-images.githubusercontent.com/70129990/137116436-da8d441d-a888-459f-82d6-83e24e750546.png)

 
 # :pushpin: Glove
 
  ![image](https://user-images.githubusercontent.com/70129990/137114756-e506f4c0-743b-48ad-b033-7741fa8d6b10.png)

 # :pushpin: Embedding Layer
 
 
 Embedding layer is one of the available layers in Keras. This is mainly used in Natural Language Processing related applications such as language modeling, but it can also be used with other tasks that involve neural networks. While dealing with NLP problems, we can use pre-trained word embeddings such as GloVe.
 


# :bar_chart: **Pratical Implementation**

<code>Code</code> [See here](./word_embeddings.ipynb)
* Word Embedding Techniques using Embedding Layer in Keras.
* One Hot Encoding.
* Word2Vec.

 
## :key: LIBRARIES USED

* Pandas
* Numpy
* tensorflow
* keras
* sklearn
* nltk
* gensim

# :bulb:  CONCLUSION
We can use any one of the text feature extraction based on our project requirement. Because every method has their advantages  like a Bag-Of-Words suitable for text classification, TF-IDF is for document classification and if you want semantic relation between words then go with word2vec.


#  :thought_balloon: REFERENCES
https://machinelearningmastery.com/what-are-word-embeddings/

https://dataaspirant.com/word-embedding-techniques-nlp/













## Author
Code Contributed by Tanvi Deshmukh.
![MIT License](https://img.shields.io/badge/Made_With_Jupyter-2CA5E0?style=for-the-badge_Color=whit)

  
