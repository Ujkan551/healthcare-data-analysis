import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("IMDB-Movie-Data.csv")
print(data.head(10))
"""
print(data.head(10))
print(data.tail(10))
print(data.shape)
print("rows",data.shape[0])
print("columns",data.shape[1])
#. Getting Information About Our Dataset Like Total Number Rows, Total Number of 
# Columns, Datatypes of Each Column And Memory Requirement
print(data.info())"""

# Check Missing Values In The Dataset

#print(data.isnull().sum())

#Drop All The  Missing Values

#data = data.dropna()

#print(data.isnull().sum())

#Check For Duplicate Data

#print(data.duplicated().sum())

#Get Overall Statistics About The DataFrame
#print(data.describe())

#Display Title of The Movie 
# Having Runtime Greater Than or equal 
# to 180 Minutes
#print(data.columns)
#print( data["Runtime (Minutes)"])
#k = data.loc[data["Runtime (Minutes)"] > 180, "Title"]
#print(k)
#which year There Was The Highest Average Voting?

#print(data.groupby("Year")["Votes"].mean().head(1))

#. In Which Year There Was The Highest Average Revenue?

#print(data.groupby("Year")["Revenue (Millions)"].mean())

#Find The Average Rating For Each Director
#data["DIRECTOR AVG RATING"]= data.groupby("Director")["Rating"].transform("mean")
#print(data)

#Display Top 10 Lengthy Movies Title and Runtime

#print(data.sort_values(by="Runtime (Minutes)", ascending=False).head(10))

#Display Number of Movies Per Year
#print(data["Year"].value_counts().sort_index(ascending=False).head(10))

#Find Most Popular Movie Title (Highest Revenue)
#print(data.groupby("Revenue (Millions)").max().sort_index(ascending=False)["Title"])

# Display Top 10 Highest Rated Movie Titles And its Directors

#print(data.sort_values(by="Rating", ascending=False).head(10)[["Title","Director"]])

