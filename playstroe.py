import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data= pd.read_csv("googleplaystore.csv")
print(data.columns)
"""print(data.head(5))
print(data.tail(3))
print(data.shape)
print("rows",data.shape[0])
print("columns",data.shape[1])"""

#GET INFORMATION OF ABOUT DATASET LIKES TOTAL ROWS,COL,DATATYPES
#print(data.info())
#GET OVERALL STATISTICS
#print(data.describe(include="all"))

#TOTAL NO OF APP TITLES CONTAIN ASTROLOGY
#print(data[data["App"].str.contains("Astrology", case=False, na=False)])
# AVG APP RATINGS
#print(data["Rating"].mean())
# FIND TOTAL NO OF UNIQUE CATEGORY
#print(data["Category"].unique())
#print(data["Category"].value_counts())


# WHICH CATEGORY GETTING HIGHEST AVG SALARY
highest_avg_category = data.groupby("Category")["Rating"].mean().idxmax()
print(highest_avg_category)
# or we can use sort_values(ascending= False) instead of idmax()

#print(data.groupby("Category")["Rating"].mean())
# FIND TOTAL NO OF APPS HAVING 5 STAR RATINGS
#print(data[data["Rating"] == 5].groupby("App")["Rating"].count())
#print(len(data[data["Rating"]==5.0]))


#FIND AVG VALUES OF REVIEWS
#print(data[data["Reviews"]=="3.0M"])
#data["Reviews"]= data["Reviews"].replace("3.0M","3.0")
#print(data["Reviews"])
#data["Reviews"]= data["Reviews"].astype("float")
#data["AVG_Reviews"]=data["Reviews"].mean()
#print(data.columns)

#FIND TOTAL NO OF FREE AND PAID APPS
#print(data["Type"].value_counts())

#WHICH APP HAS MAXIMUM REVIEWS
#print(data[data["Reviews"].max()==data["Reviews"]]["App"])

#DISPLAY TOP5 APPS HAVING HIGHEST REVIEWS
#indexx=print(data["Reviews"].sort_values(ascending=False).head(5))
#print(data.loc[indexx])

#AVG RATING OF FREE AND PAID APPS
#print(data.groupby("Type")["Rating"].mean())

#DISPLAY TOP5 HAVING MAXIMUM INSTALLS
print(data["Installs"])
data["Installs"]= data["Installs"].str.replace(".","")
print(data.head(1))
data["Installs"]= data["Installs"].str.replace("+","")
data["Installs"]= data["Installs"].str.replace(",","")
print(data["Installs"].unique())
data["Installs"]= data["Installs"].str.replace("Free","0")
print(data["Installs"].astype(float))
print(data["Installs"].dtype)
#k=data["Installs"].sort_values(ascending=False).head(5)
#print(k["App"])
# Sort the "Installs" column in descending order and select the top 5 values
k = data["Installs"].sort_values(ascending=False).head(5)
# Use the .loc method to get the "App" column for the top 5 rows
print(data.loc[k.index, "App"])
