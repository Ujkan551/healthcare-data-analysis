import pandas as pd
import numpy as np
"""l=["a","b","c"]
m_l=[10,20,30]
arr = np.array([10,20,30])
d={"a" :10 ,"b":20,"c":30}

a=pd.Series(data=m_l)
print(a)
b= pd.Series(data=m_l,index=l)
print(b)

ser1= pd.Series([3,4,5,6],index=["Gem","USA","ARG","Jap"])
ser2 = pd.Series([1,2,3,4],index=["AUS", "ARG","USA","chin"])
g= ser1+ser2
print(g)
k= ser1-ser2
print(k)
"""
df= pd.DataFrame(
    np.random.randint(0,99,size=(6,4)),
    index=["A", "B", "C", "D","E","F"],
      columns=["W","X","t","y"])
"""print(df)
df["new"]=df["X"]+df["W"]
print(df)
#df.drop("A",axis=0)

df.loc["A"]
print(df.loc["A"])
print(df.iloc[2])
q= df.loc[["A","B"],["W","X"]]
print(q)"""
"""
#r = df.loc[df["W"] > 50]
#print(r)
result = df[(df["W"]>50) & (df["X"]>50)]
#result = df[(df["W"] > 50) & (df["x"] > 50)]
print(result)
r1 = df[(df["W"]> 5)| (df["X"]>50)]
print(r1)"""
"""
#NEW COLUMN
newint = "CA NY WV OR CD EF".split()
df["States"] = newint
print(df)

df= pd.DataFrame({
    'A':[1,2,np.nan],
    'B':[5,np.nan,np.nan],
    'C':[1,2,3]
})

print(df)
#e=df.dropna()
#print(e)
df.fillna(df.mean(),inplace=True)
print(df)

print(df.groupby("A").mean())
print(df.groupby("A").max())

# Fix for the DataFrame creation
left = pd.DataFrame({
    'Key': ['A0', 'B2', 'C0', 'D0', 'E0'],
    'A': ['A1', 'B2', 'C3', 'D3', 'E3'],
  'B':['B0','B1','B2','B3','B4']})

print(left)

right = pd.DataFrame({
    'Key': ['A0', 'B0', 'C0', 'D0', 'E3'],
    'D': ['D1', 'D2', 'D3', 'D4', 'D5'],
  'D':['C0','C1','C2','C3','C4']})

print(right)


a= pd.merge(left,right,how='inner',on='Key')
print(a)
"""
left = pd.DataFrame({
    'StudentID': [101, 102, 103, 104],
    'Name': ['Aman', 'Neha', 'Ravi', 'Simran'],
    'Age': [21, 22, 20, 23],
    'City': ['Delhi', 'Mumbai', 'Banaras', 'Pune']
})
right = pd.DataFrame({
    'StudentID': [101, 102, 104, 105],
    'Subject': ['Math', 'Science', 'English', 'Math'],
    'Marks': [88, 92, 75, 80]
})
#left= left.join(right)
#print(left)
#print(df.head(2))
print(left["StudentID"].unique())
print(left["StudentID"].nunique())
print(left["StudentID"].value_counts())