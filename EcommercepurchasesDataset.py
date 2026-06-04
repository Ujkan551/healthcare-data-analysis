import pandas as pd

# Open the CSV file by just its name (assuming it's in the current working directory)
data = pd.read_csv("Ecommerce Purchases")
#to see top 10 rows
#print(data.head(10))
#to see last 10 rows
#print(data.tail(10))
#data type of each column
#print(data.dtypes)
#to check null values
#print(data.isnull())
#print(data.isnull().sum())
#count how many rows and columns in data set
#print(data.columns)
#print(len(data.columns))
#print(len(data))
# info of our data
#print(data.info())

#HIGHEST AND LOWEST PURCHASE

#print(data.columns)
#print(data["Purchase Price"].max())
#print(data["Purchase Price"].min())

#AVERAGE PURCHASE PRICE
#print(data["Purchase Price"].mean())

#  HOW MANY PEOPLE AS FRENCH THEIR LANGUAGE
#print(data["Language"])
#print(data[data["Language"]=="fr"])
#print(len(data[data["Language"]=="fr"]))
#print(data[data["Language"]=="fr"].sum())
#count = data.groupby("Language").size().loc["fr"]
#print(count)
#JOB TITLE CONTAINS ENGINEER
#print(data.columns)
#print(data["Job"]) 
#print(data[data["Job"]=="Energy engineer"])
#print("Total engineeris are",data["Job"].str.contains("engineer",case = False).sum())
#print(data[data["Job"].str.contains("engineer",case=False)])
#print(len(data[data["Job"].str.contains("engineer",case=False)]))

#E-MAIL OF FOLLOWING PERSON WITH THE FOLLOWING IP ADDRESS ; 132.207.160.22
#print(data.columns)
#print(data["IP Address"]=="132.207.160.22")
#print(data[data["IP Address"]=="132.207.160.22"]["Email"])
#print(data.query('`IP Address` == "132.207.160.22"')['Email'])

# HOW MANY PEOPLE HAVE MSTERCARD AS THEIR CREDIT CARD PROVIDER AND MADE A PURCHASE ABOVE 50?
#print(data.columns)
#print(data["CC Provider"])
#print(data["CC Provider"]=="Mastercard")
#print((data["CC Provider"] == "Mastercard") & (data["Purchase Price"] > 50))
#count = ((data["CC Provider"] == "Mastercard") & (data["Purchase Price"] > 50)).sum()
#print(count)
#print(len(data[(data["CC Provider"] == "Mastercard") & (data["Purchase Price"] > 50)]))

# E-MAIL OF A PERSON WITH FOLLOWING CC NUMBER
#print(data.columns)
#print(data['Credit Card'])
#print(data['Credit Card']=="4664825258997302")
#print(data[data["Credit Card"] == "4664825258997302"]["Email"])
#print(data.query('`Credit Card` == 4664825258997302')['Email'])


#HOW MANY PEOPLE PURCHASE DURING AM AND PM
#print(data.columns)
#print(data["AM or PM"].value_counts())
print(data["AM or PM"].between("AM","PM"))
# HOW MANY PEOPLE CC EXPIRES IN 2020
#print(len(data[data["CC Exp Date"].apply(lambda x:x[3:]=="20")]))
#import pandas as pd
#print(dir(pd))
#print(dir(pd.DataFrame))
#print(dir(pd.Series))