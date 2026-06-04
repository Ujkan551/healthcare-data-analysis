import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

data= pd.read_csv("adult.csv")

#print(data)
"""
print(data.head(10))
print(data.tail(10))
print(data.shape)
print("rows:", data.shape[0])
print("cols:", data.shape[1])
print(data.info())"""
print(data.info())

#FETCH RANDOM SAMPLES FROM DATASET(50%)
"""print(data.sample(frac=0.50))"""
# we get random samples everytime we print
#to get same sequence everytime
"""print(data.sample(frac=0.50,random_state=100))"""

#CHECK NULL VALUES
print(data.isnull().sum())

#FOR VISULATIZATION
"""print(sns.heatmap(data.isnull()))
plt.show()"""



#PERFORM DATA CLEANING [ REPLACE "?" with NAN]
print(data.isin(["?"]).sum())
import numpy as np 

"""data["workclass"] = data["workclass"].replace("?", np.nan)
data["occupation"] = data["occupation"].replace("?", np.nan)
data["native-country"] = data["native-country"].replace("?", np.nan)
#print(data)

sns.heatmap(data.isnull())
plt.show()"""

#DROP ALL THE MISSING VALUES
"""drop=data.isnull().sum()*100/len(data)
print(drop)
print(data.dropna(how="any",inplace=True))
print(data.shape)"""

#CHECK DUPLICATE AND DROP
"""dup=data.duplicated().any()
#print(dup)
drp=data.drop_duplicates()
print(drp)"""


#OVERALL STATISTCS
"""print(data.describe())"""
#print(data.describe(include="all"))


#DROP THE COLUMNS EDUCATION-NUM,CAPITAL-GAIN AND CAPITAL-LOSS

"""print(data.columns)
print(data["education"].unique())
print(data["educational-num"].unique())
data.drop(["educational-num", "capital-gain", "capital-loss"], axis=1, inplace=True)
print(data)
"""

#UNIVARIATE ANALYSIS
#what is the distribution of age column?
"""print(data.columns)
print(data['age'].describe)
# to use non numeric columns use include="all"
# you can also specify include = ["object"] or include = ["float64"] or include =["number]
print(data["age"].hist())
plt.show()""" 
# bins refers to range of values in each bar 

#TOTAL PERSONS HAVING AGE BETWEEN 17 TO 48(INCLUSIVE)
"""print(sum((data["age"]>=17) & (data["age"]<=48)))
print(sum((data["age"].between(17,48))))"""
# if u want to be exclusive then use .between(17,48, inclusive ="neither")

#DISTRIBUTION OF WORKCLASS COLUMN
"""print(data["workclass"].describe(include="all"))
print(data["workclass"].hist())
plt.figure(figsize=(10,10))
plt.show()"""

# HOW MANY PERSONS HAVING BACHELORS OR MASTERS DEGREE

"""print(data.columns)
print(data["education"].unique())
print(data["education"].value_counts())
print(data[data["education"].isin(["Bachelors", "Masters"])].shape[0])"""

"""f1= data["education"]== "Bachelors"
f2= data["education"]== "Masters"
f3= sum(f1|f2)
print(f3)"""

#BIVARITE ANALYSIS- TO FIND RELATIONSHIP BETWEEN TWO DIFFERENT VARIABLES
"""print(data.columns)
sns.boxplot(x="income", y = "age",data= data)

plt.show()"""

#REPLACE SALARY VALUES[<=50K AND >50K] WITH 0 AND 1

"""print(data["income"].unique())
data["income"]=data["income"].replace(["<=50K", ">50K"], [0,1])
print(data["income"].value_counts())
sns.countplot(x="income", data= data)
plt.show()"""

#WHICH WORKCLASS GETTING HIGHEST SALARY

"""print(data.columns)
print(data["workclass"].value_counts())
print(data.groupby("workclass")["income"].mean())
sns.barplot(x="workclass", y="income", data=data)
plt.show()"""
