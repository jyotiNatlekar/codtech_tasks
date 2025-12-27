ML_SPAM_DETECTION

COMPANY : CODTECH IT SOLUTIONS

NAME : JYOTI VIJAY NATLEKAR

INTERN ID : CT04DR2389

DOMAIN : PYTHON PROGRAMMING

DURATION : 4 WEEKS

MENTOR : NEELA SANTOSH


The **Machine Learning Model Implementation (Spam Classification)** task was completed as part of the **CODTECH Python & Machine Learning Internship – Task 4**. The main objective of this task was to understand how machine learning models are built, trained, and used to make predictions on real-world data. This project focuses on **SMS Spam Detection**, which is a very common and practical application of machine learning in everyday life.

Spam detection is an important problem because people receive a large number of unwanted messages such as promotional offers, fake prizes, and fraud messages. Manually filtering such messages is not possible, so automated systems are required. This project helped me understand how machine learning can be used to automatically classify messages as **spam** or **ham (not spam)**.

In this project, I worked with a dataset containing SMS messages. Each message is labeled either as spam or ham. The dataset was first loaded using the **Pandas** library, which made it easy to view and manage the data. The dataset contained two main columns: one for the message label and one for the message text. Working with a real dataset helped me understand how machine learning is applied in real applications.

The next step was **data preprocessing**, which is a very important part of any machine learning project. Since machine learning models cannot directly understand text labels, the message labels were converted into numeric form, where ham was represented as 0 and spam as 1. This step helped me understand how data must be prepared before training a model.

After preprocessing, the dataset was divided into **training and testing sets** using the `train_test_split` function from Scikit-learn. About 80% of the data was used for training the model, and 20% was used for testing. This helped me understand why testing data is important to check how well a model performs on unseen data.

Since the data consisted of text messages, it could not be directly given to the machine learning algorithm. Therefore, **TF-IDF Vectorization** was used to convert text messages into numerical feature vectors. I learned that TF-IDF measures how important a word is in a message compared to all other messages. Stop words were removed to improve the accuracy of the model. This step helped me understand how text data is transformed into numbers that a machine learning model can understand.

For model training, I used the **Multinomial Naive Bayes** algorithm. This algorithm is especially suitable for text classification problems like spam detection. I learned how the Naive Bayes algorithm works based on probability and how it is effective for large text datasets. Training the model helped me understand how patterns are learned from data.

After training the model, I evaluated its performance using different evaluation metrics such as **accuracy score, classification report, and confusion matrix**. The model achieved an accuracy of approximately **97.8%**, which shows that it performs very well. The confusion matrix showed that most messages were classified correctly, and both spam and ham classes had high precision and recall. This helped me understand how to interpret model results instead of relying only on accuracy.

An important part of this project was creating a **prediction function** called `check_spam(text)`. This function takes a new message as input and predicts whether it is spam or not spam. This step helped me understand how trained models are used in real applications to make predictions on new data.

This project has many real-world applications. Similar spam classification models are used in **email spam filters**, **SMS filtering systems**, **fraud detection**, **customer support systems**, and **cybersecurity applications**. The same model structure can also be adapted for other text classification tasks such as sentiment analysis, fake news detection, toxicity detection, and complaint categorization.

Overall, this task helped me understand the **complete machine learning pipeline**, including data loading, preprocessing, feature extraction, model training, evaluation, and prediction. It improved my understanding of machine learning concepts and gave me confidence in using **Scikit-learn** for real-world problems. This project was simple to understand but very powerful and practical, making it an excellent learning experience during my internship.


Just tell me 😊
