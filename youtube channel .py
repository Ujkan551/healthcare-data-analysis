import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("top-5000-youtube-channels.csv")
print(data.columns)
#print(data.head(20))
#print(data.tail(10))
#print(data.isnull().sum())
#print(data.shape)
#print("rows: " ,data.shape[0])
#print("rows: " ,data.shape[1])
#print(data.info())
# #print(data.describe())

# DATA CLEANING(REPLACE"-" TO NAN)
"""data=data.replace("--", np.nan,regex= True)
print(data)
print(data.head(20))"""

# data cleaning (rank column)
print(data.dtypes)
print*