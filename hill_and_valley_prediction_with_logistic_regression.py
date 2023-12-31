# -*- coding: utf-8 -*-
"""Hill and valley prediction with logistic Regression

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11RjNqZmEEj0pSTjS9Zvg5LNXb12Wohsz

**Title of project**
 Hill and valley prediction with logistic regression

import library
"""

import pandas as pd

import numpy as np

"""import dataset"""

df=pd.read_csv("https://github.com/YBI-Foundation/Dataset/raw/main/Hill%20Valley%20Dataset.csv")

"""Get the first five rows of the dataset"""

df.head()

"""Get information of the dataset"""

df.info()

df.describe()

df.columns

df.shape

df["Class"].value_counts()

df.groupby("Class").mean()



"""Define y(depentdent or label variableor target variable ) And X (independent or feature or attribute variable)"""

y=df["Class"]

y.shape

y

x=df[["V1","V2","V3","V4","V5","V6","V7","V8","V9","V10","V11","V12","V13","V14","V15","V16","V17","V18","V19","V20","V21","V22","V23","V24","V25","V26","V27","V28","V29","V30","V31","V32","V33","V34","V35","V36","V37","V38","V39","V40","V41","V42","V43","V44","V45","V46","V47","V48","V49","V50","V51","V52","V53","V54","V55","V56","V57","V58","V59","V60","V61","V62","V63","V64","V65","V66","V67","V68","V69","V70","V71","V72","V73","V74","V75","V76","V77","V78","V79","V80","V81","V82","V83","V84","V85","V86","V87","V88","V89","V90","V91","V92","V93","V94","V95","V96","V97","V98","V99","V100"]]

x=df.drop("Class",axis=1)

x.shape

x

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y, test_size=0.3, stratify=y, random_state=2529)

x_train.shape,x_test.shape,y_train.shape,y_test.shape

"""Get model train"""

from sklearn.linear_model import LogisticRegression

lr=LogisticRegression()

lr.fit(x_train,y_train)

"""Get model prediction"""

y_pred=lr.predict(x_test)

y_pred.shape

y_pred

"""Get model evalution"""

from sklearn.metrics import confusion_matrix, classification_report

print(confusion_matrix(y_test,y_pred))

print(classification_report(y_test,y_pred))