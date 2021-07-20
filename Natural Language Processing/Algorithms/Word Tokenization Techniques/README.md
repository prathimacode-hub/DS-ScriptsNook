# Word Tokenization Techniques 


**INTRODUCTION**

There are various Word tokenization techniques available which can be applicable based on the language and purpose of modeling.Here I have explained few of the tokenization techniques used in NLP.


**BRIEF EXPLANATION**

### What is Tokenization?
Tokenization is breaking the raw text into small chunks. Tokenization breaks the raw text into words, sentences called tokens. These tokens help in understanding the context or developing the model for the NLP. The tokenization helps in interpreting the meaning of the text by analyzing the sequence of the words.
Tokenization can be done to either separate words or sentences. If the text is split into words using some separation technique it is called **Word Tokenization**

There are various tokenization techniques used in NLP.
![](https://miro.medium.com/max/945/1*FTEu803GEsNrNslvY1RbXQ.png)

**WORKING CONDITIONS**
- I have breifly explained all the Word tokenization techniques in detail with examples in this Notebook.


**USAGE**

 This is a requirement in natural language processing tasks where each word needs to be captured and subjected to further analysis like classifying and counting them for a particular sentiment etc.


**LIBRARIES USED**
 - NLTK
 - Spacy
 - Genism
 - Keras

**ADVANTAGES**

As tokens are the building blocks of Natural Language, the most common way of processing the raw text happens at the token level.It’s a fundamental step in both traditional NLP methods.


**DISADVANTAGES**

- One of the biggest challenges in the tokenization is the getting the boundary of the words. In English the boundary of the word is usually defined by a space and punctuation marks define the boundary of the sentences, but it is not same in all the languages. 
- One of the major issues with word tokens is dealing with Out Of Vocabulary (OOV) words. OOV words refer to the new words which are encountered at testing. These new words do not exist in the vocabulary. Hence, these methods fail in handling OOV words.

**APPLICATIONS**
- Sentiment analysis
- Language translation
- Fake news detection
- Grammatical error detection etc.

**CONCLUSION**

Tokenization is a powerful way of dealing with text data. We saw a glimpse of that in this script and also implemented tokenization using Python.

**REFERENCES**

- NLTK documentation: https://www.nltk.org/
- https://www.analyticsvidhya.com/blog/2020/05/what-is-tokenization-nlp/
- https://neptune.ai/blog/tokenization-in-nlp

**Created By :**

--> Name : Shivani Rana
--> LinkedIn : https://www.linkedin.com/in/shivani-rana-b833a91a3/
--> Kaggle : https://www.kaggle.com/shivanirana63
