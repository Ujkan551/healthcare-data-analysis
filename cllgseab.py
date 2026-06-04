import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the built-in tips dataset
tips = sns.load_dataset("tips")

# Display first 10 rows
print("First 10 rows of tips dataset:")
print(tips.head(10))
"""
# Create distribution plot
plt.figure(figsize=(10, 6))
sns.histplot(data=tips, x="total_bill", kde=False)
plt.title("Distribution of Total Bill Amounts")
plt.xlabel("Total Bill ($)")
plt.ylabel("Count")
"""
#scatter plot
"""
plt.figure(figsize=(10, 6))
sns.scatterplot(data=tips, x="total_bill",y="tip",hue="size")
plt.title("tips vs Total Bill")
plt.xlabel("Total Amount ($)")
plt.ylabel("Tips Amount ($)")
"""
#RUGPLOT

# Load the tips dataset
tips = sns.load_dataset("tips")

# Create figure
plt.figure(figsize=(10, 6))

# Create rug plot with distribution
sns.rugplot(data=tips, 
            x="total_bill",
            height=0.05,          # Height of the lines
            color="red",          # Color of the lines
            alpha=0.5)           # Transparency


# Customize plot
plt.title("Distribution of Total Bills with Rug Plot")
plt.xlabel("Total Bill ($)")
plt.ylabel("Count")

# Show the plot
plt.show()

# Show the plot
plt.show()