import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data= pd.read_csv("udemy_courses.csv",parse_dates=["published_timestamp"])
print(data.columns)
"""print(data.dtypes)

print(data.head(10))
print(data.tail(5))
print(data.shape)
print("rows",data.shape[0])
print("col",data.shape[1])
print(data.info())
print(data.isnull().sum())
#print(data.duplicated().any())
data=data.drop_duplicates()
print(data.duplicated().any())"""

#FIND OUT NUMBER OF COURSES PER SUBJECT
"""print(data["subject"].nunique())
print(data["course_title"].nunique())
sns.countplot(data["subject"])
plt.xlabel("Subjects",fontsize=13)
plt.ylabel("Course Title",fontsize=13)
plt.xticks(rotation=65)
plt.show()"""
# for which levels udemy courses providing the courses
"""print(data["level"].value_counts())
sns.countplot(data["level"])
plt.xlabel("level",fontsize=13)
plt.ylabel("ss",fontsize=13)
plt.xticks(rotation=65)
plt.show()"""

#DISPLAY COUNT OF PAID AND FREE COURSES
#print(data["is_paid"].value_counts())

# WHICH COURSE HAS MORE LECTURES(FREE OR PAID)
#print(data.groupby(["is_paid"]).mean())
# Group by "is_paid" and calculate the mean for numerical columns
#print(data.groupby("is_paid").mean(numeric_only=True))

#WHICH GROUP HAS HIGHEST SUBSCRIBER
#sns.barplot(x="is_paid", y="num_subscribers",data=data)
#plt.show()
# WHICH LVL HAS HIGHEST NUMBERS OF SUBSCRIBERS
#sns.barplot(x="level", y="num_subscribers", data= data)
#plt.show()


# FIND MOST POPULAR COURSE TITLE
#print(data["course_title"].value_counts())
#group= data.groupby(["course_title"]["num_subscribers"].max())
#group = data.groupby("course_title")["num_subscribers"].max().reset_index()
#print(group["course_title"])
#print(group["course_title"].head(10))

# FIND COURSE HAVING HIGHEST NUMBER OF REEVIEWS
print(data.groupby("course_title")["num_reviews"].max().head(1).reset_index())
#sns.barplot(x="course_title", y="num_reviews", data= data)
#plt.show()

#does price effect no of reviews
#sns.scatterplot(x="price", y="num_reviews", data= data)
#plt.show()

#FIND TOTAL NO OF COURSES HAVING PYTHON
#print(data[data["course_title"].str.contains("python",case=False)])
#print(data[data["Job"].str.contains("engineer",case=False)])

#DISPLAY TOP 10 MOST POPULAR PYTHON COURSE HAVING HIGHEST NUMBER OF SUBSCRIBERS
pythons=(data[data["course_title"].str.contains("python",case=False)].
      sort_values(by="num_reviews", ascending=False).head(10))
sns.barplot(x="num_subscribers",y="course_title",data=pythons)
plt.show()
