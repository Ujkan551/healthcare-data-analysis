import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("train.csv")
#DISPLAY TOP 5 ROWS OF DATA SET
#print(data)
#print(data.head(5))
#CHECK LAST 3 ROWS OF DATA SET
#print(data.tail(3))

#FIND SHAPE OF OUR DATASET
"""print(data.shape)
print("rows:", data.shape[0])
print("column:", data.shape[1])"""

#GET INFORMATION ABOUT THE DATASET
"""print(data.info())"""

#GET OVERALL STATISTICS ABOUT DATAFRAME
"""print(data.describe())"""
"""print(data.describe(include="all"))"""
# DATA FILTERING
"""print(data.columns)
print(data[["Name","Age"]])"""
# FOR MORE THAN ONE COLUMN WE NEED TWO SQUARE BRACKETS


"""print(sum([data["Sex"]=="male"]))
print(data[data['Sex']=="female"])"""

#HOW MANY PEOPLE SURVIVED IN TITANIC
"""print(sum(data['Survived']==1))
print(data[data['Survived']==1])"""

#FIND UNIQUE VALUES
"""print(data.isnull().sum())
sns.heatmap(data.isnull())
plt.show()"""

#PERCENTAGE OF NULL VALUES
"""per= data.isnull().sum()*100/len(data)
print(per,"%")"""

#DROP THE COLUMN
"""k= data.drop("Age",axis=1,inplace= True)
print(k)"""

#HANDLE MISSING VALUES
"""print(data["Embarked"].mode()) #mode function prints the most frequently occurring values
#fillna
print(data["Embarked"].fillna("s", inplace=True))"""

# CATEGORICAL DATA ENCODING
"""print(data["Sex"].unique())
data["GENDER"]= data["Sex"].map({"male":1,"female":2})
print(data)"""


"""x=data["Sex"].map({"male":1,"female":2})
# IF WE WANT TO CHANGE COLUMN POSITION
print(data.insert(5,"GENDERnew",x))
print(data.head(1))"""

"""print(data["Embarked"].unique())
print(data["Embarked"].dropna(axis=0,inplace= True))

print(data["Embarked"].unique())

ab=pd.get_dummies(data,columns=["Embarked"])
print(ab)
s= pd.get_dummies(data,columns=["Sex"])
print(s)

ab=pd.get_dummies(data,columns=["Embarked"],drop_first= True)"""

#WHAT IS UNIVARIATE ANALYSIS
"""Univariate analysis is a statistical technique that involves analyzing one variable at a time. It's a foundational step in data analysis to understand the individual characteristics of each variable within your dataset"""
"""print(data.columns)
#HOW MANY SURVIVED AND HOW MANY DIED
print(data["Survived"].value_counts())
sns.catplot(data["Survived"])
plt.show()"""

#HOW MANY PASSENGERS WHERE IN FIRST CLASS AND THIRD CLASS
"""print(data["Pclass"].unique())
print(data["Pclass"].value_counts())

plt.plot(data["Pclass"])
plt.show()"""

#NO OF MALE AND FEMALE PASSENGERS
"""print(data.columns)
print(data["Sex"].unique())
print(data["Sex"].value_counts())
sns.boxplot(data["Sex"],orient="h")
plt.show()"""

"""#plt.hist(data["Age"])
#plt.show()
sns.boxplot(data["Age"],orient="h")
plt.show()"""

#BIVARIATE ANALYSIS

#WHO HAS BETTER CHANCE OF SURVIVAL
#sns.barplot(x="Sex",y="Survived",data=data)
#plt.show()
#WHICH CLASS HAS BETTER CHANCE OF SURVIVAL FIRST,SECOND OR THIRD CLASS
#sns.barplot(x="Pclass",y="Survived",data=data)
#plt.show()

#FEATURE ENGINEERING
print(data.columns)
#CREATE NEW COLUMNS WITH EXISTING COLUMNS
data["new_family"]= data["SibSp"]+data["Parch"]
print(data)
k= data.insert


