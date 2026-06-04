import pandas as pd

data= pd.read_csv("Salaries.csv")
#print(data)

#print(data.shape)
#print(data.columns)
#print(data.head(5))
#print(data.tail(5))
#print(data.describe())
#print(data.info())
#print(data.isnull().sum())

#DROP ID,NOTES,AGENCY AND STATUS COLUMNS
#data= data.drop(["Id","Notes","Agency","Status"],axis=1)
#print(data)


#STATISTICS ABOUT DATAFRAME
#print(data.describe())
#print(data.describe(include="all"))
#includes string ,boolean etc also
#FIND OCCURENCE OF TOP5 EMPLOYEE NAME
#print(data.columns)
#print(data["EmployeeName"])
#print(data["EmployeeName"].value_counts().head(5))


#FIND NO OF UNIQUE JOB TITLES
#print(data.columns)
#print(data["JobTitle"].nunique())


#TOTAL JOB TITLES THAT CONTAIN CAPTAIN
#print(len(data[data["JobTitle"].str.contains("CAPTAIN",case=False)]))


#DISPLAY ALL EMPLOYEE NAMES FROM FIRE DEPARTMENT

#print(data.columns)
#print(data[data["JobTitle"].str.contains("fire",case=False)]["EmployeeName"])


# REPLACE "NOT PROVIDED" IN EMPLOYEE NAME COLUMN TO NAN
#import numpy as np

# Ensure the column is stripped of whitespace and case-consistent
#data["EmployeeName"] = data["EmployeeName"].str.strip()  # Remove leading/trailing spaces
#data["EmployeeName"] = data["EmployeeName"].str.upper()  # Convert to uppercase for consistent matching

# Replace "NOT PROVIDED" with NaN
#data["EmployeeName"] = data["EmployeeName"].replace("NOT PROVIDED", np.nan)

# Print the updated column
#print(data["EmployeeName"])

#DROP THE ROWS HAVING 5 MISSING VALUES
#print(data.drop(data[data.isnull().sum(axis=1)==5].index,axis=0,inplace=True))


#JOB TITLE OF ALBERT PARDINI
#print(data[data["EmployeeName"]=="ALBERT PARDINI"]["JobTitle"])

#HOW MUCH ALBERT PARDINI MAKES INCLUDES BENEFITS
#print(data[data["EmployeeName"]=="ALBERT PARDINI"]["TotalPayBenefits"])


#NAME OF THE PERSON HAVING HIGHEST BASEPAY
#print(data.columns)


#AVERAGE BASEPAY OF ALL EMPLOYEE PER YEAR
#print(data.columns)
#print(data.groupby("Year").mean()["BasePay"])


#AVG BASEPAY OF ALL EMPLOYEE PER JOB TITLE
#print(data.groupby("JobTitle").mean()["BasePay"])


# Convert "BasePay" to numeric, forcing errors to NaN
#data["BasePay"] = pd.to_numeric(data["BasePay"], errors="coerce")

# Group by "JobTitle" and compute the mean of "BasePay"
#print(data.groupby("JobTitle")["BasePay"].mean())


#AVG BASEPAY OF ALL EMPLOYEE HAVING JOB TITLE ACCOUNTANT

#print(data.columns)
#print(data[data["JobTitle"]=="ACCOUNTANT"]["BasePay"].mean())


#FIND TOP 5 MOST COMMON JOBS
#print(data.columns)
#print(data["JobTitle"].value_counts().head(5))